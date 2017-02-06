"""Define URL patterns for users."""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # Login Page - Use Django default login page
    url(r'^login/$', login,
        {'template_name' : 'users/login.html'}, name='login'),

    # Log out.
    url(r'^logout/$', views.logout_view, name='logout'),

    # User register.
    url(r'^register$', views.register, name='register'),
]