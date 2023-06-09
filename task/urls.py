from django.urls import path
from . import views
from .views import SignUpView
from django.views.generic.base import TemplateView

# used to map urls to view functions
# path(route, view)

# URLconf
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
]