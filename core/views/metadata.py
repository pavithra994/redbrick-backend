from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from core.models import JobType
from core.serializers import JobTypeSerializer


@api_view(['GET'])
@permission_classes((AllowAny,))
def job_types(request):
    job_types_qs = JobType.objects.all()
    serializer = JobTypeSerializer(job_types_qs,many=True)
    return Response(serializer.data,status=200)
