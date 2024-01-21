from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Listing, LikedListing, Bid
from .forms import ListingForm, BidForm
from users.forms import LocationForm
from django.contrib import messages
from .filters import ListingFilter
from imp import reload
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def main_view(request):
    return render(request, "views/main.html", {"name": "AutoMax"})


@login_required
def home_view(request):
    listings = Listing.objects.all()
    listing_filter = ListingFilter(request.GET, queryset=listings)
    user_liked_listings = LikedListing.objects.filter(
        profile=request.user.profile).values_list('listing')
    liked_listings_ids = [l[0] for l in user_liked_listings]
    context = {
        'listing_filter': listing_filter,
        'liked_listings_ids': liked_listings_ids,
    }
    return render(request, "views/home.html", context)

@login_required
def list_view(request):
    if request.method == 'POST':
        try:
            listing_form = ListingForm(request.POST, request.FILES)
            location_form = LocationForm(request.POST)
            
            if listing_form.is_valid() and location_form.is_valid():
                listing = listing_form.save(commit=False)
                listing_location = location_form.save()
                listing.seller = request.user.profile
                listing.location = listing_location
                listing.save()
                messages.info(request, f'{listing.model} Listing posted successfully')
                return redirect('home')
            else:
                raise Exception()
        except Exception as e:
            print(e)
            messages.error(request, 'An error occured while posting the listing')
    elif request.method == 'GET':
        listing_form = ListingForm()
        location_form = LocationForm()
    return render(request, 'views/list.html',{'listing_form':listing_form, 'location_form':location_form})


@login_required
def listing_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        bid_data = get_max_bid(item_id = id)
        max_bid = bid_data[0]
        bid_count = bid_data[1]
        if(max_bid == None):
            max_bid = listing.bid_value
        if listing is None:
            raise Exception
        # bid_form = BidForm(request.POST, request.FILES, instance=listing)
        return render(request, 'views/listing.html', {'listing': listing, 'max_bid': max_bid, 'bid_count':bid_count})
    except Exception as e:
        messages.error(request, f'Invalid UID {id} was provided for listing.')
        return redirect('home')
    


@login_required
def edit_view(request, id):
    try:
        listing = Listing.objects.get(id = id)
        if listing is None:
            raise Exception
        if request.method == 'POST':
            listing_form = ListingForm(request.POST, request.FILES, instance=listing)
            location_form = LocationForm(request.POST, instance=listing.location)

            if listing_form.is_valid() and location_form.is_valid():
                listing_form.save()
                location_form.save()
                messages.info(request, f'Listing {id} updated successfully!')
                return redirect('home')
            else:
                messages.error(request, f'An error occured while trying to edit the listing.')
                return reload()

        else:
            listing_form = ListingForm(instance=listing)
            location_form = LocationForm(instance=listing.location)
        context = {
            'location_form': location_form,
            'listing_form': listing_form
        }
        return render(request, 'views/edit.html', context)
    except Exception as e:
        messages.error(request, f"An error occured while trying to edit the listing.")
        return redirect('home')
    # return render(request, 'views/edit.html', context)

@login_required
def like_listing_view(request, id):
    listing = get_object_or_404(Listing, id = id)
    liked_listing, created = LikedListing.objects.get_or_create(profile=request.user.profile, listing=listing) #get_or_create returns tuple 1st value gets the actual instance of the model and second value whether the object already existed or was created

    if not created:
        liked_listing.delete()
    else:
        liked_listing.save()
    return JsonResponse({
        'is_liked_by_user': created,
    })


@login_required
def inquire_listing_using_email(request, id):
    listing = get_object_or_404(Listing, id=id)
    try:
        emailSubject = f'{request.user.username} is interested in {listing.model}'
        emailMessage = f'Hi {listing.seller.user.username}, {request.user.username} is interested in your {listing.model} listing on AutoMax'
        from_email = settings.EMAIL_HOST_USER
        send_mail(emailSubject, emailMessage, settings.EMAIL_HOST_USER,
                  [listing.seller.user.email, ], fail_silently=True)
        return JsonResponse({
            "success": True,
        })
    except Exception as e:
        print(e)
        return JsonResponse({
            "success": False,
            "info": e,
        })
    
@login_required
def place_bid(request, id):
    item = Listing.objects.get(pk=id)
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.profile = request.user.profile if hasattr(request.user, 'profile') else None
            bid.item = item
            bid.save()
            return redirect('home')  # Redirect to item detail page
    else:
        form = BidForm()

    return render(request, 'views\place_bid.html', {'form': form, 'item': item})

def get_max_bid(item_id):
    max_bid = Bid.objects.filter(item_id=item_id).order_by('-amount').first()
    bid_count = Bid.objects.filter(item_id=item_id).count()
    data = [max_bid, bid_count]
    return data