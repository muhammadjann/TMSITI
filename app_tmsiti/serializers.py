from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app_tmsiti.models import TMSITINews, TMSITIAnnouncement, TMSITIManagement, TMSITIStructuralDivision, \
    TMSITIStandard, TMSITIContact, TMSITIElecStandards, TMSITIBuildingReglements


class NewsListSerializer(ModelSerializer):
    class Meta:
        model = TMSITINews
        fields = ('id', 'title', 'content', 'date_published', 'image')


class NewsListDetailSerializer(ModelSerializer):
    class Meta:
        model = TMSITINews
        fields = "__all__"


class AnnouncementSerializer(ModelSerializer):
    class Meta:
        model = TMSITIAnnouncement
        fields = '__all__'


class ManagementSerializer(ModelSerializer):
    class Meta:
        model = TMSITIManagement
        fields = '__all__'


class StructuralDivisionSerializer(ModelSerializer):
    class Meta:
        model = TMSITIStructuralDivision
        fields = '__all__'


class StandardsSerializer(ModelSerializer):
    class Meta:
        model = TMSITIStandard
        fields = '__all__'


class ContactSerializer(ModelSerializer):
    class Meta:
        model = TMSITIContact
        fields = '__all__'


class ElectStandardsSerializer(ModelSerializer):
    class Meta:
        model = TMSITIElecStandards
        fields = '__all__'


class BuildingReglementsSerializer(ModelSerializer):
    class Meta:
        model = TMSITIBuildingReglements
        fields = '__all__'