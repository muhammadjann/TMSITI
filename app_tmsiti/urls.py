from django.urls import path
from rest_framework import routers

from app_tmsiti.views import NewsListViewSet, AnnouncementViewSet, ManagementViewSet, StructuralDivisionViewSet, \
    StandardsViewSet

router = routers.DefaultRouter()
router.register(r'news_list', NewsListViewSet)
router.register(r'announcement', AnnouncementViewSet)
router.register(r'managements', ManagementViewSet)
router.register(r'structural_division', StructuralDivisionViewSet)
router.register(r'standards', StandardsViewSet)
urlpatterns = router.urls
