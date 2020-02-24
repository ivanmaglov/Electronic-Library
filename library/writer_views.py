from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from .decorators import writer_required
from .forms import WriterSignUpForm
from .models import User,Book

def writerhome(request):
    return render(request, 'library/writers/writer_home.html')

class WriterSignUpView(CreateView):
    model = User
    form_class = WriterSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'writer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

@method_decorator([login_required, writer_required], name='dispatch')
class BookCreateView(CreateView):
    model = Book
    fields = ('title', 'genre','picture', 'Overview','download', )
    template_name = 'library/writers/book_add_form.html'

    def form_valid(self, form):
        book = form.save(commit=False)
        book.owner = self.request.user
        book.save()
        messages.success(self.request, 'Good job.')
        return redirect('writers:book_list')

@method_decorator([login_required, writer_required], name='dispatch')
class BookListView(ListView):
    model = Book
    template_name = 'library/writers/book_list.html'
    context_object_name = 'all_books_by_user'
    ordering = ['-created']

    def get_queryset(self):
        queryset = self.request.user.books \
            .select_related('owner') \

        return queryset

@method_decorator([login_required, writer_required], name='dispatch')
class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'library/writers/book_detail.html'
    slug_field = 'url_address'
    slug_url_kwarg = 'url_address'

    def get_queryset(self):
        queryset = self.request.user.books \
            .select_related('owner') \

        return queryset

@method_decorator([login_required, writer_required], name='dispatch')
class BookUpdateView(UpdateView):
    model = Book
    fields = ('title','genre', 'picture', 'Overview', 'download', )
    template_name = 'library/writers/update_book.html'
    success_url = reverse_lazy('writers:book_list')

@method_decorator([login_required, writer_required], name='dispatch')
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'library/writers/book_confirm_delete.html'
    success_url = reverse_lazy('writers:book_list')

