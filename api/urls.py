from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')

urlpatterns = [
path('todos/completed',views.TodoCompletedList.as_view(),name='apicompleted'),
path('todos', views.TodoListCreate.as_view(),name='apicurrent'),
path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
path('todos/<int:pk>/complete', views.TodoComplete.as_view()),

path('all/', include(router.urls)),

path('signup',views.signup),
path('login',views.login),
]
