import base64

from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .forms import ComputerForm
from .models import Computer


@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    form = ComputerForm
    list_display = ("id", "title", "price", "cpu", "gpu", "ram", "created_at", "preview")
    
    def preview(self, obj):
        if obj.photo and isinstance(obj.photo, (bytes, memoryview)):
            b64 = base64.b64encode(obj.photo).decode("utf-8")
            return format_html(f'<img src="data:image/png;base64,{b64}" width="80" />')
        return "—"
    
    preview.short_description = _('превью')