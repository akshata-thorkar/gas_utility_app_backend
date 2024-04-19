from django.urls import path
from .views import submit_request, request_tracking
from .views import user_login
from .views import user_signup
from .views import account_info

urlpatterns = [
    path('submit_request/', submit_request, name='submit_request'),
    path('request_tracking/', request_tracking, name='request_tracking'),
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('account/', account_info, name='account_info'),
]