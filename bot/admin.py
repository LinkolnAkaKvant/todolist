from django.contrib import admin

from bot.models import TgUser


class TgUserAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'db_user')
    readonly_fields = ('verification_code',)

    def db_user(self, obj: TgUser) -> str:
        if obj.user:
            return obj.user.username
        else:
            return None


admin.site.register(TgUser, TgUserAdmin)
