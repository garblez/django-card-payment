from django.conf.urls import url

import views

urlpatterns = [
    url(r'^test/', views.test, name='test'),
    url(r'^charge/', views.charge_card, name='charge'),
    url(r'^save/', views.save_card, name='save'),
    url(r'^test_save/', views.test_save, name='test_save')
]