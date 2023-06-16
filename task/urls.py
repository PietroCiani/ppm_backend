from django.urls import path
from . import views
from .views import SignUpView

# used to map urls to view functions
# path(route, view)

# URLconf
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('edit/<int:pk>/', views.edit_todo, name='edit_todo'),
    path('todo/delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('add_tag/', views.add_tag, name='add_tag')
]