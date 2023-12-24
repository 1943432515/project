from django.contrib import admin
from DS.models import *


# Register your models here.
def change_status_ON(modeladmin, request, queryset):
    queryset.update(status='ON')


def chang_status_OFF(modeladmin, request, queryset):
    queryset.update(status='OFF')


class customerinfoAdmin(admin.ModelAdmin):
    search_fields = ('user_name',)
    list_per_page = 10
    list_display = ('user_name', 'user_email')
    fields = ('user_name', 'user_email', 'user_password', 'gender', 'tel_number', 'address', 'true_name', 'money')


class goodinfoInline(admin.TabularInline):
    model = goodinfo


class goodinfoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_filter = ('status',)
    list_editable = ('status',)
    list_display = ('name', 'price', 'number', 'label', 'seller', 'status')
    fields = ('name', 'image', 'price', 'introduction', 'number', 'label', 'seller', 'status')
    actions = [change_status_ON, chang_status_OFF]


class sellerinfoAdmin(admin.ModelAdmin):
    inlines = [goodinfoInline]
    search_fields = ('user_name',)
    list_filter = ('user_name',)
    list_per_page = 10
    list_display = ('user_name', 'user_email')
    fields = ('user_name', 'user_email', 'user_password', 'id_number', 'gender', 'tel_number', 'address', 'true_name')


admin.site.register(customerinfo, customerinfoAdmin)
admin.site.register(sellerinfo, sellerinfoAdmin)
admin.site.register(goodinfo, goodinfoAdmin)
