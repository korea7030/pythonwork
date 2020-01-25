from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Facility, models.HouseRule, models.Amenity)
class ItemAdmin(admin.ModelAdmin):
    """ ItemAdmin Definition"""

    list_display = (
        'name',
        'used_by',
    )

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ RoomAdmin Definition"""
    # admin form의 inline 표시(foreignkey 관계의 모델 표시 시에 좋음)
    inlines = (
        PhotoInline,
    )

    # Form의 경계 지정
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "city",
                    "address",
                    "price",
                    "room_type",
                )
            },
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {"fields": ("amenities", "facilities", "house_rules")},
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    # 리스트에 나타낼 필드 목록
    list_display = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    # 정렬 컬럼 지정
    ordering = (
        "name",
        "price",
    )

    # 리스트 필터 컬럼 지정
    list_filter = (
        'instant_book', 'host__gender',
        'city', 'country', 'room_type', 'amenities',
        'facilities', 'house_rules')

    # 리스트 길이가 많아질 때 사용(돋보기 클릭 시 팝업창으로 리스트 표시)
    raw_id_fields = (
        'host',
    )

    # 조회필드 지정(default : icontains)
    search_fields = ('=city', '^host__username')  # city startswith

    filter_horizontal = ('amenities', 'facilities', 'house_rules')

    # admin에서 저장할 때 호출되는 method(결국 model의 save() method를 호출하게 됨)
    def save_model(self, request, obj, form, change):
        print(obj, change, form)
        super().save_model(request, obj, form, change)

    # custom function 지정
    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = 'Photos Count'


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ PhotoAdmin Definition """

    list_display = ('__str__', 'get_thumbnail')

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')
    
    get_thumbnail.short_description = 'thumbnail'
