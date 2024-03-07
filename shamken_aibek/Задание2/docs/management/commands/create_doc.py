from django.core.management import BaseCommand
from docs.models import DocumentModel

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Creating docs")

        doc_names = [
            "Doc1",
            "Doc2",
            "Doc3",

        ]
        docx = DocumentModel.objects.create(name='doc1', file='doc1.docx',)


        self.stdout.write(self.style.SUCCESS("Doc created successfully!"))

