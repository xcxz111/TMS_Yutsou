from django import forms
from home.models import Feedback


class FeedbackForm(forms.Form):
    username = forms.CharField(
        label="full name",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "full name",
                "placeholder": "ФИО"
            }
        )
    )
    email = forms.EmailField(
        label="email address",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "email",
                "placeholder": "ваш email",
                "pattern": "[^ @]*@[^ @]*"
            }
        )
    )
    instagram = forms.CharField(
        label="instagram",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "instagram",
                "placeholder": "ваш instagram",
            }
        )
    )
    message = forms.CharField(
        label="your message",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "message",
                "placeholder": "напишите сообщение"
            }
        )
    )

    def clean(self):
        has_error = False
        if len(self.cleaned_data["message"]) < 10:
            self.add_error("message", "A lot of size")
            has_error = True
        if self.cleaned_data["instagram"].lower() == "google":
            self.add_error("instagram", "Realy?")
            has_error = True
        if has_error:
            raise forms.ValidationError("Invalid form")
        return self.cleaned_data

    def save(self):
        Feedback.objects.create(**self.cleaned_data)




