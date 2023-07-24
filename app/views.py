from django.shortcuts import render, HttpResponse, redirect
from.models import Book

# Create your views here.

# FBV - Function based Views

# def welcome_page(request):
#     return HttpResponse("Welcome to Library Application")



def welcome_page(request):
    return render(request, "welcome.html")

import datetime

def show_all_books(request):
    books =Book.objects.filter(is_active=True)   # show only active book
    return render(request, "showbooks.html", {"allbooks": books, "data": "ghhghgghhG", "today" : datetime.datetime.now()})


# def show_single_book(request, bid):
#     book_obj = Book.objects.get(id =bid)
#     return render (request= request,template_name= "bookdetail.html",context =  {"book" : book_obj})


def show_single_book(request, bid):
    try:
       book_obj = Book.objects.get(id =bid)
    except Book.DoesNotExist:
        return HttpResponse("Book doesnot exist")
    return render (request= request,template_name= "bookdetail.html",context =  {"book" : book_obj})

def common_var(req):
    final_dict = req.POST
    # print(final_dict)
    book_name = final_dict.get("nm")
    book_price = final_dict.get("prc")
    book_qty = final_dict.get("qty")
    book_is_pub = final_dict.get("ispub")
    return book_name, book_price, book_qty, book_is_pub





def add_single_book(request):
    
    if request.method == "POST":
        book_name,book_price, book_qty, book_is_pub =common_var(request)
        if book_is_pub == "YES":
            is_pub = True
        else:
            is_pub = False

        Book.objects.create(name=book_name, price=book_price, qty=book_qty, is_published=is_pub) 
        return redirect("show_books")
    

    elif request.method == "GET":
       return render(request, "addbook.html")
    
def edit_single_book(request,bid):  
    book_obj = Book.objects.get(id=bid) 

    if request.method == "GET":
       return render(request, "bookedit.html", {"single_book": book_obj})
    elif request.method == "POST":
        book_name,book_price, book_qty, book_is_pub = common_var(request)

        if book_is_pub == "YES":
            is_pub = True
        else:
            is_pub = False
         # for updating daata
        book_obj.name = book_name
        book_obj.price = book_price
        book_obj.name = book_name
        book_obj.qty = book_qty
        book_obj.is_published = is_pub
        book_obj.save()
        return redirect("show_books")
    




def delete_single_book(request,bid):   
    book_obj = Book.objects.get(id=bid) 
    book_obj.delete()    # this is for hard delete(delete from data completely)post request
    return redirect("show_books")

def soft_delete_single_book(request,bid):
    book_obj = Book.objects.get(id=bid) 
    book_obj.is_active = False    # for soft delete means is active will be 0 nd temporay delte
    book_obj.save()
    return redirect("show_books")

# -----------------------------------for forms
from .forms import GeeksForm, BookForm, AddressForm

# Create your views here.
def form_view(request):
	# context ={}
	# context['form']= GeeksForm()
    # print(GeeksForm())
    # return render(request, "form_test.html", {"form": GeeksForm()})
    # return render(request, "form_test.html", {"form": BookForm()})
    # return render(request, "form_test.html", {"form": AddressForm()})
      if request.method == "POST":
        pass
      elif request.method == "GET":
        return render(request, "book_form_test.html", {"bookform": BookForm()})


# this is from book_form_test.html----paste this side
# <!-- <form action = "" method = "post">
# 	{% csrf_token %}
#    <div class="form-row">
# 	<div class="form-group col-md-6 mb-0">
# 		{{ form.email|as_crispy_field }}
# 	</div>
# 	<div class="form-group col-md-6 mb-0">
# 	  {{ form.password|as_crispy_field }}
# 	</div>
#   </div>
#   {{ form.address_1|as_crispy_field }}
#   {{ form.address_2|as_crispy_field }}
#   <div class="form-row">
# 	<div class="form-group col-md-6 mb-0">
# 	  {{ form.city|as_crispy_field }}
# 	</div>
# 	<div class="form-group col-md-4 mb-0">
# 	  {{ form.state|as_crispy_field }}
# 	</div>
# 	<div class="form-group col-md-2 mb-0">
# 	  {{ form.zip_code|as_crispy_field }}
# 	</div>
#   </div>
#   {{ form.check_me_out|as_crispy_field }}
#   <button type="submit" class="btn btn-primary">Sign in</button>
	
# </form> -->





    
