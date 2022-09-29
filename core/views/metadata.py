from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.models import JobType
from core.serializers import JobTypeSerializer


@api_view(['GET'])
def job_types(request):
    job_types_qs = JobType.objects.all()
    serializer = JobTypeSerializer(job_types_qs,many=True)
    return Response(serializer.data,status=200)
