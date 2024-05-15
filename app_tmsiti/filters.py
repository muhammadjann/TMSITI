from rest_framework.filters import BaseFilterBackend
from django.db.models import Q


class TMSITIDictionarySearchFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        search_param = request.query_params.get('search', None)
        if search_param:
            queryset = queryset.filter(
                Q(word_name_uz__icontains=search_param) |
                Q(word_name_ru__icontains=search_param) |
                Q(word_name_en__icontains=search_param) |
                Q(word_name_turk__icontains=search_param)
            )
        return queryset
