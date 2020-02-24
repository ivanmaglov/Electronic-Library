from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .decorators import reader_required
from django.shortcuts import redirect, render
from .models import User
from .forms import ReaderSignUpForm,My_Favorite_Book_Genre_Form
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from .models import Reader,Quote
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator

def readerhome(request):
    return render(request, 'library/readers/reader_home.html')

class ReaderSignUpView(CreateView):
    model = User
    form_class = ReaderSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'reader'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('readers:readerhome')

@method_decorator([login_required, reader_required], name='dispatch')
class UpdateMyFavoriteBookGenres(UpdateView):
    model = Reader
    form_class = My_Favorite_Book_Genre_Form
    template_name = 'library/readers/genres_form.html'
    success_url = reverse_lazy('readers:quote_list')

    def form_valid(self, form):
        return super().form_valid(form)

@method_decorator([login_required, reader_required], name='dispatch')
class QuoteCreateView(CreateView):
    model = Quote
    fields = ('from_writer', 'from_book','Overview', )
    template_name = 'library/readers/add_quote_form.html'

    def form_valid(self, form):
        quote = form.save(commit=False)
        quote.owner = self.request.user
        quote.save()
        #messages.success(self.request, 'Good job.')
        return redirect('readers:readerhome')

@method_decorator([login_required, reader_required], name='dispatch')
class QuateListView(ListView):
    model = Quote
    template_name = 'library/readers/quote_list.html'
    context_object_name = 'all_quotes_by_user'
    ordering = ['-created']

    def get_queryset(self):
        queryset = self.request.user.quotes \
            .select_related('owner') \

        return queryset

class QuateListUpdate(UpdateView):
    model = Quote
    fields = ('from_writer','from_book', 'Overview', )
    template_name = 'library/readers/update_quote.html'
    success_url = reverse_lazy('readers:quote_list')

class QuateDelete(DeleteView):
    model = Quote
    template_name = 'library/readers/quate_confirm_delete.html'
    success_url = reverse_lazy('readers:quote_list')

@method_decorator([login_required, reader_required], name='dispatch')
class QuoteDetailView(DetailView):
    model = Quote
    context_object_name = 'quote'
    template_name = 'library/readers/quote_detail.html'
    slug_field = 'url_address'
    slug_url_kwarg = 'url_address'

    def get_queryset(self):
        queryset = self.request.user.quotes \
            .select_related('owner') \

        return queryset