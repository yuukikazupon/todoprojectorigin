from django.shortcuts import render,redirect
# from django.views import generic
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import TodoModel
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class TodoList(LoginRequiredMixin,ListView) :
    model = TodoModel
    template_name = "list.html"
    context_object_name = "todo_list"
    login_url = 'login'
    paginate_by = 3

class TodoDetail(LoginRequiredMixin,DetailView) :
    model = TodoModel
    template_name = "detail.html"
    context_object_name = "todo_detail"
    login_url = 'login'

class TodoCreate(LoginRequiredMixin,CreateView) :
    model = TodoModel
    template_name = "form.html"
    fields = "__all__"
    success_url = reverse_lazy("list")
    login_url = 'login'

    def form_valid(self,form) :
        messages.success(self.request,"保存しました")
        return super().form_valid(form)

    def form_invalid(self,form) :
        messages.error(self.request,"保存に失敗しました")
        return super().form_invalid(form)


class TodoUpdate(LoginRequiredMixin,UpdateView) :
    model = TodoModel
    template_name = "form.html"
    fields = "__all__"
    success_url = reverse_lazy("list")
    login_url = 'login'

class TodoDelete(LoginRequiredMixin,DeleteView) :
    model = TodoModel
    template_name = "delete.html"
    context_object_name = "todo_delete"
    success_url = reverse_lazy("list")
    login_url = 'login'

def signupfunc(request) :
    if request.method == "POST" :
        username1 = request.POST["username"]
        password1 = request.POST["password"]

        try :
            User.objects.get(username=username1)
            return render(request,"signup.html",{"message":"すでに登録してあります"})
        except :
            user = User.objects.create_user(username1,"",password1)
            return redirect("list")
    else :
        return render(request,"signup.html")
