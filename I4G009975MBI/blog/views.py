#from django.shortcuts import render
from django.views import generic;
from .models import Post;
from django.urls import reverse_lazy

# Create your views here.

class PostListView(generic.ListView):
    """
    View for a Post's list
    """
    model = Post
    #fields = "__all__"
    #success_url = reverse_lazy("blog: all")
    

class PostCreateView(generic.CreateView):
    """
    View for a Post's create
    """
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog: all")
    

class PostDetailView(generic.DetailView):
    """
    View for a Post's details
    """
    model = Post
    

class PostUpdateView(generic.UpdateView):
    """
    View for a Post's update
    """
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog: all")
    

class PostDeleteView(generic.DeleteView):
    """
    View for a Post's delete
    """
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog: all")
    










