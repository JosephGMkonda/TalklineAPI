from rest_framework.serializers import(HyperlinkedIdentityField,ModelSerializer,SerializerMethodField)
from .models import Post
from accounts.serializer import userDetailsSerializer

from comments.serializer import CommentSerializer
from comments.models import Comment
class PostSerializer(ModelSerializer):
    user = userDetailsSerializer(read_only=True)
    comments = SerializerMethodField()
   
    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'content',
            'picture',
            'published',
            'updated',
            'comments'
        ]

    def get_comments(self, obj):
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(c_qs, many=True).data
        return comments



class PostDetailSerializer(ModelSerializer):
    
    picture = SerializerMethodField()
    html = SerializerMethodField()
    class Meta:
        model = Post

        fields = [
            
            'id',
            'content',
            'picture',
            'published',
            'html' 
        ]
    def get_html(self, obj):
        return obj.get_markdown()
    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image
        
            


