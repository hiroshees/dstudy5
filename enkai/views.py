from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import resolve_url

from django.http import HttpResponse
from django.http import HttpRequest
from django.http import Http404
from django.http import HttpResponseBadRequest

from django.urls import reverse_lazy
from django.urls import reverse

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.conf import settings

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.sites.shortcuts import get_current_site

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.core.mail import BadHeaderError, send_mail

from .models import Category, Event, EventUser, Chat
from .forms import ChatCreateForm


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "enkai/category/list.html"
    

class CategoryCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Category
    fields = ["name"]
    template_name = "enkai/category/create.html"
    success_url = reverse_lazy("enkai:category_list")
    success_message = "新規作成しました"


class CategoryEditView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Category
    fields = ["name"]
    template_name = "enkai/category/edit.html"
    success_url = reverse_lazy("enkai:category_list")
    success_message = "更新しました"


class EventUserMixin(UserPassesTestMixin):
    raise_exception = False
    
    def test_func(self):
        user = self.request.user
        pk = self.kwargs['pk']
        event = Event.objects.get(pk=pk)
        return user.pk == event.user.pk or user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "主催者のみがアクセス可能です")
        return redirect('enkai:event_list')


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "enkai/event/list.html"
    

class EventCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Event
    fields = ["name","max_participant","category","user"]
    template_name = "enkai/event/create.html"
    success_url = reverse_lazy("enkai:event_list")
    success_message = "新規作成しました"
    
    def get_initial(self):
        initial = super().get_initial()
        initial["user"] = self.request.user
        return initial


class EventEditView(SuccessMessageMixin, LoginRequiredMixin, EventUserMixin, UpdateView):
    model = Event
    fields = ["name","max_participant","category","user"]
    template_name = "enkai/event/edit.html"
    success_url = reverse_lazy("enkai:event_list")
    success_message = "更新しました"


class MyOwnerEventView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "enkai/event/mylist.html"
    
    def get_queryset(self):
        user_id = self.request.user.id
        event = Event.objects.filter(user_id=user_id)
        return event


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = "enkai/event/detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_id = self.kwargs.get("pk")
        user_id = self.request.user.id
        is_attend = EventUser.objects.filter(user_id=user_id, event_id=event_id).exists()
        context['is_attend'] = is_attend
        return context


class EventUserCreateView(LoginRequiredMixin, TemplateView):
    def get_success_url(self):
        return reverse_lazy('enkai:event_detail', kwargs={"pk" : self.kwargs.get("event_id")})

    def get(self, *args, **kwargs):
        event_id = self.kwargs.get("event_id")
        user_id = self.request.user.id
        
        currnet_participants = EventUser.objects.filter(event_id=event_id).count()
        event = Event.objects.get(pk=event_id)
        if(currnet_participants >= event.max_participant):
            messages.error(self.request, "満員です")
            return redirect(self.get_success_url())
        event_user = EventUser()
        event_user.event_id = event_id
        event_user.user_id = user_id
        event_user.save()
        messages.success(self.request, "イベントに参加しました")
        return redirect(self.get_success_url())


class EventUserDeleteView(LoginRequiredMixin, TemplateView):
    def get_success_url(self):
        return reverse_lazy('enkai:event_detail', kwargs={"pk" : self.event_user.event_id})

    def get(self, *args, **kwargs):
        event_id = self.kwargs.get("event_id")
        user_id = self.request.user.id
        event_user = EventUser.objects.filter(event_id=event_id, user_id=user_id).first()
        event_user.delete()
        self.event_user = event_user
        messages.success(self.request, "イベントから辞退しました")
        return redirect(self.get_success_url())


class ChatCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Chat
    #fields = ["body"]
    form_class = ChatCreateForm
    template_name = "enkai/chat/create.html"
    success_message = "投稿しました"
    
    def get_success_url(self):
        return reverse_lazy('enkai:chat', kwargs={"event_id" : self.kwargs["event_id"]})

    def get_form(self):
        # フォームのもつインスタンスに直接値を代入しておく
        form =  super().get_form()
        form.instance.event_id = self.kwargs.get("event_id")
        form.instance.user_id = self.request.user.id
        return form
    
    def get(self, request, **kwargs):
        event_id = kwargs.get("event_id")
        user_id = request.user.id
        isAttend = EventUser.objects.filter(event_id=event_id, user_id=user_id).exists()
        if not isAttend:
            messages.error(request, "イベントに参加してません")
            return redirect("enkai:event_detail", event_id)
        return super().get(request, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_id = self.kwargs["event_id"]
        event = Event.objects.filter(pk=event_id).first()
        chats = Chat.objects.filter(event_id=event_id)
        
        data = dict(
            event_id=event_id,
            event=event,
            chats=chats
        )
        context.update(data)
        return context

