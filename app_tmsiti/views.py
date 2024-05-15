from rest_framework import mixins, status, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from app_tmsiti.serializers import NewsListSerializer, NewsListDetailSerializer, AnnouncementSerializer, \
    ManagementSerializer, \
    StructuralDivisionSerializer, StandardsSerializer, ContactSerializer, ElectStandardsSerializer, \
    BuildingReglementsSerializer, SubsystemSerializer, GroupSerializer, SHNKSerializer, DictionarySerializer
from .filters import TMSITIDictionarySearchFilter
from .models import TMSITINews, TMSITIAnnouncement, TMSITIManagement, TMSITIStructuralDivision, TMSITIStandard, \
    TMSITIContact, TMSITIElecStandards, TMSITIBuildingReglements, TMSITISubsystem, TMSITIGroup, TMSITISHNK, \
    TMSITIDictionary
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


class TMSITISubsystemViewSet(viewsets.ModelViewSet):
    queryset = TMSITISubsystem.objects.all().prefetch_related(
        'tmsitigroup_set__tmsitishnk_set'
    ).order_by('subsystem_number', 'tmsitigroup__group_number')
    serializer_class = SubsystemSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class TMSITIGroupViewSet(viewsets.ModelViewSet):
    queryset = TMSITIGroup.objects.all().select_related('group_subsystem').prefetch_related('tmsitishnk_set')
    serializer_class = GroupSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class TMSITISHNKViewSet(viewsets.ModelViewSet):
    queryset = TMSITISHNK.objects.all().select_related('SHNK_group')
    serializer_class = SHNKSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class TMSITIDictionaryViewSet(viewsets.ModelViewSet):
    queryset = TMSITIDictionary.objects.all()
    serializer_class = DictionarySerializer
    filter_backends = [TMSITIDictionarySearchFilter]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
