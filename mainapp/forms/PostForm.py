from pyexpat import model
from django.forms import ModelForm
from mainapp.models import Like, Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ( 'foto', 'mensaje' ) 
        
class LikeForm(ModelForm):
    class Meta:
        model = Like
        fields = ('post_id',)