from django.urls import path
from api import views
urlpatterns = [
    path('entries/', views.EntryList.as_view(), name=views.EntryList.name),
    path('entry-detail/<int:pk>', views.EntryDetail.as_view(), name=views.EntryDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name)
]