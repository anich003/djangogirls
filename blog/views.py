from django.shortcuts import render
from django.utils import timezone

from . import models


def post_list(request):
    posts = models.Post.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')
    return render(request, 'blog/post_list.html', {'posts': posts})
