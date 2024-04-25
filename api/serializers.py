from rest_framework import serializers
from todo_app.models import TodoModel


class TodoListSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    
    class Meta:
        model = TodoModel
        fields = '__all__'

    def get_owner(self, obj):
        return obj.owner.username

    
class TodoAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ['title']



class TodoPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ['description']
        extra_kwargs = {'description': {'required': True}}