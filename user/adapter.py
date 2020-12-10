from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import perform_login
from allauth.utils import get_user_model

from .models import CustomUser

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        # ソーシャルログインの状態確認
        user = sociallogin.user
        if user.id:
            # すでに既存ユーザなのでそのまま進める
            return
        try:
            # 新規のユーザ
            User = get_user_model()
            # メールアドレスが登録済みかを確認
            existing_user = User.objects.get(email=user.email)
            # 存在するので連結
            sociallogin.connect(request, existing_user)
        except User.DoesNotExist:
            pass
