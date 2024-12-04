from django.urls import path
from .views import ToDoListCreateAPIView, ToDoRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('todos/', ToDoListCreateAPIView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', ToDoRetrieveUpdateDestroyAPIView.as_view(), name='todo-detail'),
]
