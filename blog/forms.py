from django import forms
from .models import Post, Comment, User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # 标题和内容

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # 只让用户填内容

class SimpleRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # 手动设置密码
        if commit:
            user.save()
        return user