from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('guests', views.GuestViewSet)
router.register('reservations', views.ReservationsViewSet)
router.register('movie', views.MovieViewSet)

urlpatterns = [
    path('', views.no_rest_no_model, name='products'),
    path('no_rest_from_model', views.no_rest_from_model,
     name='no_rest_from_model'),
    path('rest/fbvlist/', views.FBV_list, name='FBV_list'),
    path('rest/FBV_detail/<int:pk>', views.FBV_detail, name='FBV_detail'),
    path('rest/CBV_list/', views.CBV_list.as_view()),
    path('rest/CBV_detail/<int:pk>', views.CBV_detail.as_view()),
    path('rest/Guestlist/', views.GuestList.as_view() ),
    path('rest/Guestdetail/<int:pk>', views.GuestDetail.as_view() ),
    path('rest/Glist/', views.GtList.as_view()),
    path('rest/Gdetail/<int:pk>', views.GDetail.as_view()),
    path('rest/findmovie/', views.findmovie),
    path('rest/newreservation/', views.addreservation),
    path('rest/', include(router.urls)),

    # path('add', views.add_product, name='add'),
]
# # ila khdmti viewset  hadi dyal format_suffix_patterns makhaskxi  tdirha
# urlpatterns = format_suffix_patterns(urlpatterns)