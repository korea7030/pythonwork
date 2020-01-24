from django.contrib import admin
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


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ RoomAdmin Definition"""
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

    # 조회필드 지정(default : icontains)
    search_fields = ('=city', '^host')  # city startswith

    filter_horizontal = ('amenities', 'facilities', 'house_rules')

    # custom function 지정
    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ PhotoAdmin Definition """

    pass
