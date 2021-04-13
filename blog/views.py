from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from . import models


def post_list(request):
    posts = models.Post.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})