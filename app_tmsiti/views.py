from rest_framework import mixins, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from app_tmsiti.serializers import NewsListSerializer, NewsListDetailSerializer, AnnouncementSerializer, \
    ManagementSerializer, \
    StructuralDivisionSerializer, StandardsSerializer, ContactSerializer, ElectStandardsSerializer, \
    BuildingReglementsSerializer
from .models import TMSITINews, TMSITIAnnouncement, TMSITIManagement, TMSITIStructuralDivision, TMSITIStandard, \
    TMSITIContact, TMSITIElecStandards, TMSITIBuildingReglements
from .permissions import IsAdminOrPostOnly


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


class ContactApiView(APIView):
    permission_classes = (IsAdminOrPostOnly,)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        contacts = TMSITIContact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)


class ElectStandardsViewSet(ModelViewSet):
    queryset = TMSITIElecStandards.objects.all()
    serializer_class = ElectStandardsSerializer
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ('doc_number', 'doc_title', 'doc_type', 'doc_sign', 'doc_approved_year')
    ordering_fields = ('doc_number', 'doc_title', 'doc_type', 'doc_sign')


class BuildingReglementsViewSet(ModelViewSet):
    queryset = TMSITIBuildingReglements.objects.all()
    serializer_class = BuildingReglementsSerializer

