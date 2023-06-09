from django import forms


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

