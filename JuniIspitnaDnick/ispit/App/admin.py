from django.contrib import admin
from django.contrib.auth.models import User

from .models import Kategorija, Klient, Product, Prodazba

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    exclude = ("user",)

    def has_add_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        if request.user.is_superuser:
            return True
        return False

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user

        super().save_model(request, obj, form, change)

class KategorijaAdmin(admin.ModelAdmin):
    list_display = ("ime",)
    exclude = ("user",)

    def has_add_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

class KlientAdmin(admin.ModelAdmin):
    list_display = ("ime","prezime",)


admin.site.register(Klient, KlientAdmin)
admin.site.register(Kategorija, KategorijaAdmin)
admin.site.register(Product, ProductAdmin)
