from django.db import models
from django.contrib.auth import get_user_model

from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(
        verbose_name="カテゴリ名",
        max_length=255,
    )
    created = models.DateTimeField(
        auto_now_add = True,
        verbose_name="登録日",
    )
    modified = models.DateTimeField(
        auto_now = True,
        verbose_name="更新日",
    )
    
    def __str__(self):
        return self.name;


class Event(models.Model):
    name = models.CharField(
        verbose_name="イベント名",
        max_length=255,
    )
    max_participant = models.IntegerField(
        verbose_name="最大参加者数",
        default=0,
        validators=[
            MinValueValidator(1, "1以上にしてね"),
        ],
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name="カテゴリ",
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name="主催者",
    )
    created = models.DateTimeField(
        auto_now_add = True,
        verbose_name="登録日",
    )
    modified = models.DateTimeField(
        auto_now = True,
        verbose_name="更新日",
    )
    
    def __str__(self):
        return self.name;


class EventUser(models.Model):
    event = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE,
        verbose_name="イベント",
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name="参加者",
    )
    created = models.DateTimeField(
        auto_now_add = True,
        verbose_name="登録日",
    )
    modified = models.DateTimeField(
        auto_now = True,
        verbose_name="更新日",
    )


class Chat(models.Model):
    body = models.TextField(
        verbose_name="本文",
    )
    event = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE,
        verbose_name="イベント",
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name="投稿者",
    )
    created = models.DateTimeField(
        auto_now_add = True,
        verbose_name="登録日",
    )
    modified = models.DateTimeField(
        auto_now = True,
        verbose_name="更新日",
    )
    
    def clean(self):
        # 投稿ユーザがイベントに参加しているかの確認
        user_id = self.user_id
        event_id = self.event_id
        isAttend = EventUser.objects.filter(event_id=event_id, user_id=user_id).exists()
        if not isAttend:
            raise ValidationError({"body":"参加していません"})
