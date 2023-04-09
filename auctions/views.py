from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *


def index(request):
    
    return render(request, "auctions/index.html", {
        "activeListing" : Listing.objects.filter(isActive = True),
        "categories" : Categories.objects.all()
    })

def displayCategory(request):
    
    if request.method =="POST":
        categoryName = request.POST["category"]
        category = Categories.objects.get(categoryName = categoryName)
        return render(request, "auctions/index.html",{
            "activeListing" : Listing.objects.filter(isActive = True, category = category),
            "categories" : Categories.objects.all()
        } )

def create(request):
    if request.method == "GET":
        return render(request, "auctions/create.html",{
            "categories" : Categories.objects.all()
        })
    elif request.method == "POST":
        
        #get the data
        title = request.POST["title"]
        description = request.POST["description"]
        imageUrl = request.POST["imageUrl"]
        price = request.POST["price"]
        category = request.POST["category"]
        currentUser = request.user
        bid = Bid(bid = float(price), user = currentUser)
        bid.save()
        categoryObj = Categories.objects.get(categoryName=category)
        #create a listing obj
        newListing = Listing(
            title = title,
            description = description,
            price = bid,
            imageUrl = imageUrl,
            category = categoryObj,
            owner = currentUser
        )
        #insert obj in db
        newListing.save()
        #redirect to index
        return HttpResponseRedirect(reverse("index"))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    
def listing(request, id):
    listingObj = Listing.objects.get(pk = id)
    isListingInWatchlist = request.user in listingObj.watchlist.all()
    allComments = Comment.objects.filter(listing=listingObj)
    isOwner = request.user.username == listingObj.owner.username
    
    return render(request, "auctions/listing.html",{
        "listing" : listingObj,
        "isListingInWatchlist" :isListingInWatchlist,
        "allComments" : allComments,
        "leastBid": float(listingObj.price.bid) + 0.05,
        "isOwner" : isOwner
    })

def closeAuction(request, id):
    listingObj = Listing.objects.get(pk = id)
    listingObj.isActive = False
    listingObj.save()
    isListingInWatchlist = request.user in listingObj.watchlist.all()
    allComments = Comment.objects.filter(listing=listingObj)
    isOwner = request.user.username == listingObj.owner.username
    return render(request, "auctions/listing.html",{
        "listing" : listingObj,
        "isListingInWatchlist" :isListingInWatchlist,
        "allComments" : allComments,
        "leastBid": float(listingObj.price.bid) + 0.05,
        "isOwner" : isOwner,
        "AuctionUpdate" : True,
        "message" : "Congrats!! Your Auction is Closed Successfully"
        
    })


def removeWatch(request, id):
    currenUser = request.user
    listingData = Listing.objects.get(pk=id)
    listingData.watchlist.remove(currenUser)
    return HttpResponseRedirect(reverse("listing", args=(id,)))

def addWatch(request, id):
    currenUser = request.user
    listingData = Listing.objects.get(pk=id)
    listingData.watchlist.add(currenUser)
    return HttpResponseRedirect(reverse("listing", args=(id,)))
    
def displayWatchlist(request):
    currentUser = request.user
    watch = currentUser.listingwatchlist.all()
    return render(request, "auctions/displayWatchlist.html", {
        "listings": watch
    })
    
    
def addComment(request, id):
    currentUser = request.user
    listingData = Listing.objects.get(pk=id)
    message = request.POST["newComment"]
    newComment = Comment(author = currentUser, listing=listingData, message=message)
    newComment.save()
    return HttpResponseRedirect(reverse("listing", args=(id,)))
    
def addBid(request, id):
    newBid = request.POST["newBid"]
    listingData = Listing.objects.get(pk = id)
    isListingInWatchlist = request.user in listingData.watchlist.all()
    allComments = Comment.objects.filter(listing=listingData)
    isOwner = request.user.username == listingData.owner.username
    
    if not newBid:
        return render(request, "auctions/listing.html",{
        "listing" : listingData,
        "isListingInWatchlist" :isListingInWatchlist,
        "allComments" : allComments,
        "leastBid": float(listingData.price.bid) + 0.05,
        "isOwner" : isOwner,
        "message" : "Please Place a Valid Bid",
        "update" : False
    })
    else:
        updateBid= Bid(user = request.user, bid = newBid)
        updateBid.save()
        listingData.price = updateBid
        listingData.save()
        return render(request, "auctions/listing.html",{
        "listing" : listingData,
        "isListingInWatchlist" :isListingInWatchlist,
        "isOwner" : isOwner,
        "allComments" : allComments,
        "leastBid": float(listingData.price.bid) + 0.05,
        "message" : "Bid Placed Succesfully",
        "update" : True
    })