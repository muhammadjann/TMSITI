from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import TMSITINews, TMSITIAnnouncement, TMSITIManagement, TMSITIStructuralDivision, TMSITIStandard
from rest_framework.decorators import api_view
from app_tmsiti.serializers import NewsListSerializer, NewsListDetailSerializer, AnnouncementSerializer, ManagementSerializer, \
    StructuralDivisionSerializer, StandardsSerializer


class NewsListViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    queryset = TMSITINews.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return NewsListDetailSerializer
        return NewsListSerializer


class AnnouncementViewSet(ModelViewSet):
    queryset = TMSITIAnnouncement.objects.all()
    serializer_class = AnnouncementSerializer


class ManagementViewSet(ModelViewSet):
    queryset = TMSITIManagement.objects.all()
    serializer_class = ManagementSerializer


class StructuralDivisionViewSet(ModelViewSet):
    queryset = TMSITIStructuralDivision.objects.all()
    serializer_class = StructuralDivisionSerializer


class StandardsViewSet(ModelViewSet):
    queryset = TMSITIStandard.objects.all()
    serializer_class = StandardsSerializer
