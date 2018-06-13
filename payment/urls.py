from django.conf.urls import url

import views

urlpatterns = [
    url(r'^charge_card/', views.ChargeCard.as_view(), name='charge_card/'),
    url(r'^save_card/', views.SaveCard.as_view(), name='save_card/'),
]