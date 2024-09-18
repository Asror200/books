from django.urls import path

from books import views

urlpatterns = [
    path('', views.BooksListView.as_view(), name='index'),
]