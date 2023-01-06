from rest_framework.serializers import(HyperlinkedIdentityField,ModelSerializer,SerializerMethodField)
from .models import Post
from accounts.serializer import userDetailsSerializer


class PostSerializer(ModelSerializer):
    user = userDetailsSerializer(read_only=True)

   
    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'content',
            'picture',
            'published',
            'updated',
            
        ]




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
        
            


