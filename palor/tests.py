from django.forms.fields import ImageField
from django.test import TestCase
from .models import Editor, Article,tags 

# Create your tests here.
class imageTestClass(TestCase):
    def setUp(self):
        self.gallery= ImageField(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
