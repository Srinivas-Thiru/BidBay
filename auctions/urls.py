from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("displayCategory", views.displayCategory, name = "displayCategory"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("removeWatch/<int:id>", views.removeWatch, name="removeWatch"),
    path("addWatch/<int:id>", views.addWatch, name="addWatch"),
    path("displayWatchlist", views.displayWatchlist, name= "displayWatchlist"),
    path("addComment/<int:id>",views.addComment, name = "addComment" ),
    path("addBid/<int:id>", views.addBid, name = "addBid"),
    path("closeAuction/<int:id>", views.closeAuction, name= "closeAuction")
]
