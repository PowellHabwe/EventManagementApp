import stripe
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.conf import settings
from django.http import JsonResponse
from django.views import View   
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'events/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'events/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'events/user_posts.html'
    context_object_name = 'posts' 
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')
       


class PostDetailView(DetailView):
    model = Post  
    
    
    
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'header_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):   
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):   
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
   

def about(request):
    return render(request, 'events/about.html', {'title': 'About'}) 

def cancel(request):
    return render(request, 'events/cancel.html', {'title': 'Cancel'}) 


def success(request):
    return render(request, 'events/about.html', {'title': 'Success'}) 



# class ProductLandingPageView(TemplateView):
#     template_name = "landing.html"

# class CancelView(TemplateView):
#     template_name = "cancel.html"

# class SuccessView(TemplateView):
#     template_name = "success.html"



# class CreateCheckoutSessionView(DetailView):
#      model = Post 
#      theid = Post.objects.get(pk)
#      print(theid)
   
