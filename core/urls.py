from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from finances.views import CashOutFlowListView, CashOutFlowCreateView, RevenueListView, RevenueCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cashoutflows/', CashOutFlowListView.as_view(), name='cashoutflow-list'),
    path('cashoutcreate/', CashOutFlowCreateView.as_view(), name='cashoutflow-create'),
    path('revenues/', RevenueListView.as_view(), name='revenues'),
    path('createrevenue/', RevenueCreateView.as_view(), name='createrevenue'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
