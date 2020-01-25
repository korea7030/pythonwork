import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms.models import Room, RoomType, Photo, Amenity, Facility, HouseRule
from users.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many users you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        all_users = User.objects.all()
        room_types = RoomType.objects.all()

        # 데이터 생성할 조건 생성(use lambda)
        seeder.add_entity(Room, number, {
            'name': lambda x: seeder.faker.address(),
            'host': lambda x: random.choice(all_users),
            'room_type': lambda x: random.choice(room_types),
            'guests': lambda x: random.randint(1, 20),
            'price': lambda x: random.randint(1, 300),
            'beds': lambda x: random.randint(1, 5),
            'bedrooms': lambda x: random.randint(1, 5),
            'baths': lambda x: random.randint(1, 5),
        })

        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        amenities = Amenity.objects.all()
        facilities = Facility.objects.all()
        rules = HouseRule.objects.all()

        for pk in created_clean:
            room = Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 30)):
                Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1, 31)}.webp",
                )

            # add manytomany field value 
            for a in amenities:
                number = random.randint(0, 15)
                if number % 2 == 0:
                    room.amenities.add(a)

            for f in facilities:
                number = random.randint(0, 15)
                if number % 2 == 0:
                    room.facilities.add(f)

            for r in rules:
                number = random.randint(0, 15)
                if number % 2 == 0:
                    room.house_rules.add(r)

        self.stdout.write(self.style.SUCCESS(f'{number} rooms created!'))
