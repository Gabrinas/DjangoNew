from django.shortcuts import render

# Create your views here.

class PostListView(ListView):
    """
    View for a Post's list
    """
    model = Post
    

class PostCreateView(CreateView):
    """
    View for a Post's create
    """
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog: all")
    

class PostDetailView(DetailView):
    """
    View for a Post's details
    """
    model = Post
    

class PostUpdateView(UpdateView):
    """
    View for a Post's update
    """
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog: all")
    

class PostDeleteView(UpdateView):
    """
    View for a Post's delete
    """
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog: all")
    










