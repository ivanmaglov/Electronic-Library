from django.shortcuts import redirect,render
from django.views.generic import TemplateView, DetailView,ListView
from .models import Book,Quote
from django.core.paginator import Paginator
from django.db.models import Q

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def home(request):
    if request.user.is_authenticated:
        if request.user.is_writer:
            return redirect('writers:writerhome')
        else:
            return redirect('readers:readerhome')
    else:
        projects_list = Book.objects.all().order_by('-created')[:40]
        paginator = Paginator(projects_list, 3)  # Show 3 books per page
        page = request.GET.get('page')
        books = paginator.get_page(page)
        return render(request, 'all_books.html', {'books': books})

def allbooks(request):
    projects_list = Book.objects.all().order_by('-created')[:4000]
    paginator = Paginator(projects_list, 3)  # Show 3 books per page
    page = request.GET.get('page')
    books = paginator.get_page(page)
    return render(request, 'all_books.html', {'books': books})

class BookDetailViewForAll(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'library/writers/book_detail.html'
    slug_field = 'url_address'
    slug_url_kwarg = 'url_address'

def allquotes(request):
    quotes_list = Quote.objects.all().order_by('-created')[:4000]
    paginator = Paginator(quotes_list, 6)  # Show 3 quotes per page
    page = request.GET.get('page')
    quotes = paginator.get_page(page)
    return render(request, 'all_quotes.html', {'quotes': quotes})

class SearchResultsView(ListView):
    model = Book
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        book_list = Book.objects.filter(

            Q(title__icontains=query) | Q(owner__username__icontains=query) | Q(genre__name__icontains=query)
        )
        return book_list
