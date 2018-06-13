from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Examples:
    # url(r'^$', 'payment_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'', include('payment.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
