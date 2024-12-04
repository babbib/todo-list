from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ToDo
from .serializers import ToDoSerializer

class ToDoListCreateAPIView(APIView):
    """
    API view to retrieve the list of todos or create a new todo.
    """
    
    def get(self, request):
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Assuming a user is logged in
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ToDoRetrieveUpdateDestroyAPIView(APIView):
    """
    API view to retrieve, update or delete a specific todo.
    """

    def get_object(self, pk):
        try:
            return ToDo.objects.get(pk=pk)
        except ToDo.DoesNotExist:
            return None

    def get(self, request, pk):
        todo = self.get_object(pk)
        if todo is not None:
            serializer = ToDoSerializer(todo)
            return Response(serializer.data)
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        todo = self.get_object(pk)
        if todo is not None:
            serializer = ToDoSerializer(todo, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        todo = self.get_object(pk)
        if todo is not None:
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
