from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ['id','title','memo','created','datecompleted','important','datedue','progress']

class TodoCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        read_only_fields = ['title','memo','created','datecompleted','important','datedue','progress']
        fields = ['id']
