from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import  ListView , DetailView
from .models import Like, Post

class PostView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

class DetailView(DetailView):
    model = Post
    template_name = 'blog/details.html'
    context_object_name = 'posts'
    def get_context_data(self , *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated == True:
            if self.request.user.likes.filter(posts__title = self.object.title , users_id = self.request.user.id).exists():
                context['is_liked'] = True
            else:
                context['is_liked'] = False
        else:
            pass
        return context 

def like(request , slug , pk):
    try:
        like = Like.objects.get(posts__slug = slug , users_id=request.user.id)
        like.delete()
        # return JsonResponse({"response" : "unliked"})
    except:
        Like.objects.create(posts_id=pk , users_id = request.user.id)
        # return JsonResponse({"response" : "liked"})
    return redirect('blog:details' , slug)