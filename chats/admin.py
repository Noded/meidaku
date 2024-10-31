from django.contrib import admin
from .models import Message, Group

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'content', 'timestamp', 'group')
    list_filter = ('author', 'group', 'timestamp')
    search_fields = ('content', 'author__username', 'group__uuid')

admin.site.register(Message, MessageAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'display_members')
    search_fields = ('uuid',)
    
    def display_members(self, obj):
        return ", ".join([member.username for member in obj.members.all()])
    
    display_members.short_description = 'Участники'


admin.site.register(Group, GroupAdmin)

