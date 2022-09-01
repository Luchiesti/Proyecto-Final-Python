from django.contrib.auth.views import LogoutView
from django.urls import path

from UserThatBeer.views import login_request, register

urlpatterns = [
    path('login/', login_request, name='UserThatBeerLogin'),
    path('register/', register, name='UserThatBeerRegister'),
    path('logout/', LogoutView.as_view(template_name='UserThatBeer/logout.html'), name='UserThatBeerLogout'),
]