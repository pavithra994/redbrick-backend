from rest_framework import viewsets, status

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Request, Job
from core.serializers import RequestSerializer
from redbrick.utils import StandardResultsSetPagination


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request):
        _status = request.GET.get("status")
        if _status:
            self.queryset = self.queryset.filter(status=_status)
        page = self.paginate_queryset(self.queryset)
        serializer = self.serializer_class(page,many=True)
        return self.get_paginated_response(serializer.data)
        # return Response(serializer.data,status=status.HTTP_200_OK)


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = RequestSerializer