from models import schedule_item
from django.contrib import admin


class admin_schedule_item(admin.ModelAdmin):
    fields = ("date", "time", "subject", "description", "participants")
    list_display = ("date", "time", "subject")

    def queryset(self, request):
        qs = super(schedule_item, self).queryset(request)
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(schedule_item)
# Register your models here.
