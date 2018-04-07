from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Shop, Item, Review, Order, OrderItem
from urllib.parse import quote

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['icon_img', 'name', 'is_public']
    list_display_links = ['name']
    list_filter = ['is_public']
    search_fields = ['name']

    def icon_img(self, category):
        if category.icon:
            img_tag = '<img src="{}" style="max-width: 72px;" />'
            return mark_safe(img_tag.format(category.icon.url))
        return None


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'address_link']
    list_display_links = ['name']
    list_filter = ['category']

    def address_link(self, shop):
        if shop.address:
            url = 'https://map.naver.com/?query=' + quote(shop.address)
            return mark_safe('<a href="{}" target="_blank">{}</a>'.format(url, shop.address))
        return None

    address_link.short_description = '주소(네이버 맵으로 이동)'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['shop', 'name']
    list_display_links = ['name']
    list_filter = ['shop']
    search_fields = ['name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['imp_uid', 'user', 'name', 'amount_html', 'status_html', 'paid_at', 'receipt_link']
    actions = ['do_update', 'do_cancel']

    def do_update(self, request, queryset):
        total = queryset.count()
        if total > 0:
            for order in queryset:
                order.update()
            self.message_user(request, '주문 {} 건의 정보를 갱신했습니다.'.format(total))
        else:
            self.message_user(request, '갱신할 주문이 없습니다.')
    do_update.short_description = '선택된 주문들의 아임포트 정보 갱신하기'

    def do_cancel(self, request, queryset):
        queryset = queryset.filter(status='paid')
        total = queryset.count()

        if total > 0:
            for order in queryset:
                order.cancel()
            self.message_user(request, '주문 {} 건을 취소했습니다.'.format(total))


# admin.site.register([Shop, Item])
