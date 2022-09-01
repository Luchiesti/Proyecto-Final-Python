from django.urls import path

from UserThatBeer.views import login_request

urlpatterns = [
    path('login/', login_request, name='UserThatBeerLogin')
]