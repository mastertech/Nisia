from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Registered


class HasWrittenStoryListFilter(admin.SimpleListFilter):
    title = _('Escreveu a história')

    parameter_name = 'story'

    def lookups(self, request, model_admin):
        return (
            ('True', _('Sim')),
            ('False', _('Não')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'True':
            return queryset.exclude(story__exact='')
        if self.value() == 'False':
            return queryset.filter(story__exact='')


class RegisteredAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role', 'has_written_story', 'registered_at')
    list_filter = ('role', HasWrittenStoryListFilter, 'registered_at')

admin.site.empty_value_display = 'desconhecido'
admin.site.register(Registered, RegisteredAdmin)
