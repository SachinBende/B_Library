"""
URL configuration for B9_Library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import welcome_page, show_all_books, show_single_book, add_single_book, edit_single_book, delete_single_book,soft_delete_single_book, form_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", welcome_page, name="home_page"),
    path("show-books/", show_all_books, name="show_books"),
    path ("show-single-book/<int:bid>/", show_single_book, name = "show_single_book"),
    path ("add-book/", add_single_book, name = "add_single_book"),
    path ("edit-book/<int:bid>/", edit_single_book, name ="edit_single_book"),
    path ("delete-book/<int:bid>/", delete_single_book, name ="delete_single_book"),
    path ("soft-delete-book/<int:bid>/", soft_delete_single_book, name ="soft_delete_single_book"),
    path("form-view/", form_view, name="form_view"),
]


# urls /urls patterns/patterns/endpoints----names
# http://127.0.0.1:8000/admin
# http://127.0.0.1:8000/home 
# http://127.0.0.1:8000/show-books 
# http://127.0.0.1:8000/show-single-book/<int:bid> # will pass id
# http://127.0.0.1:8000/add-book 
# http://127.0.0.1:8000/edit-book/<int:bid>/ 
# http://127.0.0.1:8000/delete-book/<int:bid>/ 
# http://127.0.0.1:8000/soft-delete-book/<int:bid>/ 
# http://127.0.0.1:8000/form-view/<int:bid>/ 