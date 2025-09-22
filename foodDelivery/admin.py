from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):

    exclude = ["user"]   # هيخفي حقل user من الفورم

    def save_model(self, request, obj, form, change):
        if not obj.pk:   # لو Cart جديد
            obj.user = request.user
        obj.save()
    def get_changeform_initial_data(self, request):
        return {'user': request.user.pk}

    # علشان اليوزر يشوف بس الكاتيجوري بتاعته
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:  # السوبر يوزر يشوف كل حاجة
            return qs
        return qs.filter(user=request.user)
    

admin.site.register(Order,OrderAdmin)
