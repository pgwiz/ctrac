from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Creates the initial user groups'

    def handle(self, *args, **options):
        Group.objects.get_or_create(name='Super Admin')
        Group.objects.get_or_create(name='Admin')
        Group.objects.get_or_create(name='Editor')
        Group.objects.get_or_create(name='Normal User')
        self.stdout.write(self.style.SUCCESS('Successfully created groups'))