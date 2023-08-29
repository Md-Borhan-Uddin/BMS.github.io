from django.contrib import admin

from accounts.models import Account, Transaction


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_id','get_username')

    def get_username(self,obj):
        return obj.user.username
    get_username.short_description = 'Username'



@admin.register(Transaction)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id','get_username','create')

    def get_username(self,obj):
        return obj.user.username
    get_username.short_description = 'Username'