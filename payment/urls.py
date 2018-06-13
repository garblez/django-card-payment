from django.conf.urls import url

import views

urlpatterns = [
    url(r'^checkout/', views.ChargeCard.as_view(), name='/charge'),
    url(r'^save_card/', views.SaveCard.as_view(), name='save_card/'),
]