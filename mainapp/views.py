from datetime import date
from django.http import JsonResponse
from django.shortcuts import redirect, render
from mainapp.forms.PostForm import LikeForm, PostForm
from mainapp.models import Perfil, Post, Like 

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    for post in posts:
        post.like_counter = Like.objects.filter(post_id = post.id).count()
    likeForm = LikeForm()
    context = {'posts' : posts, 'likeForm': likeForm}
    return render(request, 'homepage.html', context)

def profile(request):
    # Vista para el perfil de usuario
    return render(request, 'profile.html', {})
    
def newPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        profile = Perfil.objects.get(pk = 1)
        if form.is_valid():
            auxForm = form.save(commit=False)
            auxForm.fecha = date.today()
            auxForm.perfil_id = profile
            auxForm.save()
            return redirect('homepage')
    else:
        form = PostForm()
        context = { 'form': form  }
        return render(request, 'newPost.html', context)

def handleLike(request):
    if request.method == 'POST':
        form = LikeForm(request.POST)
        # perfil = Perfil.objects.get(user_id = request.user) Esta seria la forma correcta  
        perfil = Perfil.objects.get(user_id = 2)
        if form.is_valid():
            like = form.save(commit=False)
            like.perfil_id = perfil
            like.save()
            like_counter = Like.objects.filter(post_id = like.post_id).count()
            return JsonResponse({'status':'false','contador':like_counter}, status=200)
        else:
            return JsonResponse({'status':'false','error':"Error Al guardar"}, status=500)

            
        
        
