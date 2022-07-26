from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .forms import BookForm
from .models import Book


# create book view
def create_book(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "app/create_book.html", context)


# list books view
def list_books(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    context['dataset'] = Book.objects.all()

    return render(request, "app/list_books.html", context)


# detail book view
def detail_book(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    context['data'] = Book.objects.get(id=id)

    return render(request, "app/detail_book.html", context)


# update book view
def update_book(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Book, id=id)

    # pass the object as instance in form
    form = BookForm(request.POST or None, instance=obj)

    # save the data from the form end
    # redirect to detail_book view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/list_books/"+id)

    context["form"] = form

    return render(request, "app/update_book.html", context)


# delete book view
def delete_book(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Book, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()

        # after deleting redirect to home page
        return HttpResponseRedirect("/")

    return render(request, "app/delete_book.html", context)
