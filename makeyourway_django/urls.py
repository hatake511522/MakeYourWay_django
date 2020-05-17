from django.contrib import admin
from gmap.models import Customer
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'address', 'lat', 'lng')


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gmap/', include('gmap.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('gmap/api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
