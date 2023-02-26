from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path

urlpatterns = [
    # path('',views.todofun,name='todofun'),
    path('', views.add_list,name='add_list'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbv/',views.classView.as_view(),name='cbv'),
    path('cbvdetail/<int:pk>/',views.detailedView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.viewupdate.as_view(), name='cbvupdatte'),
    path('cbvdelete/<int:pk>/', views.viewdelete.as_view(), name='cbvdelete')

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)