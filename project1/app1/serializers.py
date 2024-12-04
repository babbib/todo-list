from rest_framework import serializers
from .models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'user', 'title', 'description', 'timestamp', 'duedate', 'tag', 'status']
        read_only_fields = ['id', 'timestamp']