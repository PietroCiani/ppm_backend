from django.urls import path
from . import views
from .views import SignUpView

# used to map urls to view functions
# path(route, view)

# URLconf
urlpatterns = [
    path('', views.home, name='home'),  #TODO: show only todos assigned_to the logged in user
    path('signup/', SignUpView.as_view(), name='signup'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('edit_todo/<int:pk>/', views.edit_todo, name='edit_todo'),
]