from django import forms
from .models import Computer

class ComputerForm(forms.ModelForm):
    photo_upload = forms.ImageField(required=False)

    class Meta:
        model = Computer
        exclude = ["photo"]

    def save(self, commit=True):
        instance = super().save(commit=False)
        upload = self.cleaned_data.get("photo_upload")
        if upload:
            instance.photo = upload.file.read()
        if commit:
            instance.save()
        return instance
