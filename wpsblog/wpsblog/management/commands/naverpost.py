from django.core.management.base import BaseCommand, CommandError
from wpsblog.models import Naverpost as naver


class Command(BaseCommand):
    help = "testing command"

    def add_arguments(self, parser):
        parser.add_argument('naver_title', type=str)

    def handle(self, *args, **options):
        for naver_title in options['naver_title']:
            try:
                naver = naver.objects.get(title=naver_title)
            except:
                raise CommandError('Naver post "%s" does not exist' % naver_title)
            
            naver.opend = False
            naver.save()
           
            self.stdout.write(self.style.SUCCESS('Successfully closed naver "%s"' % naver_title))
