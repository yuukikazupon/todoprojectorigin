from django.urls import path
from .views import TodoList, TodoDetail, TodoCreate, TodoUpdate, TodoDelete,signupfunc
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path("",signupfunc, name="signup" ),
    path("login/",LoginView.as_view(template_name="login.html"),name="login"),
    path("logout/",LogoutView.as_view(template_name="logout.html"),name="logout"),
    path("list/" , TodoList.as_view(), name="list" ),
    path("<int:pk>/detail/", TodoDetail.as_view(), name="detail"),
    path("create/", TodoCreate.as_view(), name="create"),
    path("<int:pk>/update", TodoUpdate.as_view(), name="update"),
    path("<int:pk>/delete", TodoDelete.as_view(), name="delete"),
]
