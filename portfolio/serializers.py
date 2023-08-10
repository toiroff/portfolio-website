from .models import *
from rest_framework.serializers import ModelSerializer

class BotUserSerializer(ModelSerializer):
    class Meta:
        model = BotUser
        fields = ('name','username','user_id','created_at')


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('user_id','body','created_at')


class AboutMeSerializer(ModelSerializer):
    class Meta:
        model = AboutMe
        fields = ('information','projects','happy_clients','customers')

class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title','description')


class PortfolioSerializer(ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('name','img','description','github','project_url')