from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from .models import Post, Like


class UserPosts(TemplateView):
    """Display the users posts"""
    template_name = 'blog/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user=self.request.user)
        context['top_posts'] = Post.objects.order_by('-like')[:5]
        context['your_top_posts'] = Post.objects.filter(user=self.request.user).order_by('-like')[:5]
        return context


class CreatePost(CreateView):
    """Allow a user to create a post"""
    model = Post
    fields = ['title', 'body', 'tags', 'image']

    def form_valid(self, form):
        """Validate the form"""
        data = form.save(commit=False)
        data.user = self.request.user
        data.save()
        all_tags = form.cleaned_data['tags']
        for tag in all_tags:
            data.tags.add(tag)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


class PostDetail(DetailView):
    """Display the post in detail"""
    model = Post


class CreateLike(View):
    """Allow a user to like a post"""
    def get(self, request, pk):
        new_like = Like(username=self.request.user)
        post = Post.objects.get(pk=pk)
        new_like.save()
        post.likes.add(new_like)
        post.like += 1
        post.save()
        return render(request, 'blog/add_like.html')


class Dislike(View):
    """Allow a user to dislike a post"""
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.like -= 1
        post.save()
        return reverse('home')


class ActiveUsers(ListView):
    """Show all the active users using the website"""
    model = User


class UserPostDetail(ListView):
    """Show a list of all the posts made by a particular user"""
    model = Post
    template_name = 'blog/user_posts.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.kwargs['pk'])


class TagSearch(View):
    """Allow a user to search for posts by tag"""
    def post(self, request):
        search = self.request.POST['query']
        posts = Post.objects.filter(tags__name=search)
        return render(request, 'blog/results.html', {'posts': posts})

    def get(self, request):
        return render(request, 'blog/search.html')
