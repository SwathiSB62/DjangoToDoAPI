from django.urls import path
from . import views

urlpatterns =[
    path('signup/',views.RegisterApi.as_view(),name="signup" ),
    path('signin/',views.TokenObtainPairView.as_view(),name="signin"),
    path('changePassword/',views.ChangePassword.as_view(),name="changePassword"),
    path('todolist/',views.TodoGetView.as_view(), name="ToDoList"),
    path('todos/',views.TodoCreateView.as_view(),name="CreateToDo"),
    path("todos/<id>", views.TodoUpdateView.as_view(),name="UpdateToDo"),
]

