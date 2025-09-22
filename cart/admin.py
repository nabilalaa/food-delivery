from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    exclude = ["user"]   # هيخفي حقل user من الفورم

    def save_model(self, request, obj, form, change):
        if not obj.pk:   # لو Cart جديد
            obj.user = request.user
        obj.save()
        
    def get_changeform_initial_data(self, request):
        return {'user': request.user.pk}
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:  # السوبر يوزر يشوف كل حاجة
            return qs
        return qs.filter(user=request.user)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            if request.user.is_superuser:
                kwargs["queryset"] = Category.objects.all()
            else:
                kwargs["queryset"] = Category.objects.filter(user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Item,ItemAdmin)



class CategoryAdmin(admin.ModelAdmin):
    exclude = ["user"]   # هيخفي حقل user من الفورم

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:  # السوبر يوزر يشوف كل حاجة
            return qs
        return qs.filter(user=request.user)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:   # لو Cart جديد
            obj.user = request.user
        obj.save()
    def get_changeform_initial_data(self, request):
        return {'user': request.user.pk}
admin.site.register(Category,CategoryAdmin)



 
    
class CartItemInline(admin.TabularInline):  # أو StackedInline
    model = CartItem
    extra = 0

class CartAdmin(admin.ModelAdmin):
    list_display = ("user" ,"total_items","total_price")
    exclude = ["user"]    # هيخفي حقل user من الفورم

    def save_model(self, request, obj, form, change):
        if not obj.pk:   # لو Cart جديد
            obj.user = request.user
        obj.save()

    inlines = [CartItemInline]
    # علشان اليوزر يشوف بس الكاتيجوري بتاعته
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:  # السوبر يوزر يشوف كل حاجة
            return qs
        return qs.filter(user=request.user)

    def total_items(self, obj):
        return sum(item.quantity for item in CartItem.objects.filter(cart__user__username=obj.user.username))
    
    def total_price(self,obj):
        return sum(item.quantity * item.product.price for item in CartItem.objects.filter(cart__user__username=obj.user.username))


admin.site.register(Cart,CartAdmin)

admin.site.register(CartItem)
