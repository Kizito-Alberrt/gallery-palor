from django.conf.urls import url 
from . import views

urlpatterns=[
    url('^today/$',views.palor_of_day,name ='your palor'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_palor,name ='pastPalor')  
]