from . import views
from django.urls import path
from .views import addHashView, addLinkView, allHashesView, confirmView, detailView, enterCodeView, hashAddedView, hashLinkView, hashedDetailView, indexView, loginView, notloggedInView, wrongCodeView


urlpatterns = [
    path('', indexView, name='home'),
    path('stories/<slug:slug>/', detailView, name="post_detail"),
    path('login/', loginView, name="login"),
    path('not-logged-in/', notloggedInView, name="not-logged-in"),
    path('link-with-hash/<slug:slug>/', hashLinkView, name="link-with-hash"),
    path('add-link/', addLinkView, name='add-link'),
    path('enter-code/', enterCodeView, name='enter-code'),
    path('confirm-message/', confirmView, name='confirm-view'),
    path('add-hash/', addHashView, name='add-hash'),
    path('wrong-code/', wrongCodeView, name='wrong-code'),
    path('hash-added', hashAddedView, name="hash-added"),
    path('all-hashes/', allHashesView, name="all-hashes"),
    path('all-hashes/<slug:slug>', hashedDetailView, name="hashed-detail")
]
