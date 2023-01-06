from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from rest_framework.serializers import(CharField,EmailField,HyperlinkedIdentityField,ModelSerializer,SerializerMethodField,ValidationError)


User = get_user_model()

class userDetailsSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name'

        ]

class UserCreateSerializer(ModelSerializer):
    password2 = CharField(label="Confirm password")

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password2'
        ]

        extra_kwargs = {"password":{"write_only":True},"password2":{"write_only":True}}
        
    def validate_password(self,value):
        data = self.get_initial()
        password = data.get("password2") 
        password2 = value

        if password != password2:
            raise ValidationError("Passwords must match")
        return value
    def validate_password2(self,value):
        data = self.get_initial()
        password = data.get("password") 
        password2 = value

        if password != password2:
            raise ValidationError("Passwords must match")
        return value

    def create(self,validated_data):
        username = validated_data['username']
        password = validated_data['password']

        user_obj = User (
            username = username,

        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True,read_only=True)
    username = CharField()

    class Meta:
        model = User

        fields = [
            'username',
            'password',
            'token'
        ]

        extra_Kwargs = {"password":{"write_only":True}}