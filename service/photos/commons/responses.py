from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

success_response = Response({'success':True}, status=HTTP_200_OK)