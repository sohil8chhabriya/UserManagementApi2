from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('/register', views.RegisterFormView.as_view())
]