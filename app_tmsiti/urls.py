from django.urls import path
from rest_framework import routers

from app_tmsiti.views import NewsListViewSet, AnnouncementViewSet, ManagementViewSet, StructuralDivisionViewSet, \
    StandardsViewSet, ContactApiView, BuildingReglementsViewSet, ElectStandardsViewSet

router = routers.DefaultRouter()
router.register(r'news_list', NewsListViewSet)
router.register(r'announcement', AnnouncementViewSet)
router.register(r'managements', ManagementViewSet)
router.register(r'structural_division', StructuralDivisionViewSet)
router.register(r'standards', StandardsViewSet)
router.register(r'building-reg', BuildingReglementsViewSet)
router.register(r'elect-standards', ElectStandardsViewSet)
urlpatterns = [
                  path('contact/', ContactApiView.as_view()),
              ] + router.urls
