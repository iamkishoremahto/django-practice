
from django.urls import path
from .views import crudViews, loginLogoutViews



urlpatterns = [
    path('', crudViews.home, name= 'home'),
    path('addStudent/', crudViews.addStudent, name = 'addStudent'),
    path('Student/<int:pk>/', crudViews.updateStudent, name = 'updateStudent'),
    path('deleteStudent/<int:pk>/', crudViews.deleteStudent, name = 'deleteStudent'),
    path('login/', loginLogoutViews.login, name = 'login'),
    path('logout/', loginLogoutViews.logout , name= 'logout')
]