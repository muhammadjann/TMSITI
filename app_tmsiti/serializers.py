from rest_framework.serializers import ModelSerializer

from app_tmsiti.models import TMSITINews, TMSITIAnnouncement, TMSITIManagement, TMSITIStructuralDivision, \
    TMSITIStandard, TMSITIContact, TMSITIElecStandards, TMSITIBuildingReglements, TMSITISubsystem, TMSITIGroup, \
    TMSITISHNK, TMSITIDictionary


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


class SHNKSerializer(ModelSerializer):
    class Meta:
        model = TMSITISHNK
        fields = ['SHNK_code', 'SHNK_date', 'SHNK_title', 'SHNK_file_uz', 'SHNK_file_ru']


class GroupSerializer(ModelSerializer):
    shnk_set = SHNKSerializer(many=True, read_only=True)

    class Meta:
        model = TMSITIGroup
        fields = ['group_number', 'group_name', 'shnk_set']


class SubsystemSerializer(ModelSerializer):
    group_set = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = TMSITISubsystem
        fields = ['subsystem_number', 'subsystem_title', 'group_set']


class DictionarySerializer(ModelSerializer):
    class Meta:
        model = TMSITIDictionary
        fields = ['id', 'word_name_uz', 'word_name_ru', 'word_name_en', 'word_name_turk']
