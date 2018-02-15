from . import models
from . import serializers

from django.views.decorators.csrf import csrf_exempt

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics

class PollList(APIView):
    def get(self, request, format = None):
        polls = models.Poll.objects.all()
        serializer  = serializers.PollLookupSerializer(polls, many = True)
        return Response(serializer.data)

class Poll(APIView):
    def get_object(self, pk):
        try:
            return models.Poll.objects.get(id=pk)
        except models.Poll.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        poll = self.get_object(pk)
        serializer = serializers.PollSerializer(poll)
        return Response(serializer.data)

class Answer(APIView):
    def post(self, request, format=None):
        serializer = serializers.PollAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(request.data)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def ListPoll(request):
#     if request.method == 'GET':
#         queryset = models.Poll.objects.all()
#         serializer_class = serializers.PollSerializer(queryset, many = True)
#         return JsonResponse(serializer_class.data)

# def Poll(request, pk):
#     try:
#         poll = models.Poll.objects.get(pk=pk)
#     except models.Poll.DoesNotExist:
#         return JsonResponse(status=status.HTPP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer_class = serializers.PollFullSerializer(poll)
#         return JsonResponse(serializer_class.data)

# @api_view(['POST'])
# def Answer(request, pk):
#     if request.method == 'POST':
#         answer = serializers.PollAnswerSerializer(data = request.data)
#         if answer.is_valid():
#             answer.save()
#             return JsonResponse(answer.data, status = status.HTTP_201_CREATED)
#         return JsonResponse(answer.errors, status = status.HTTP_400_BAD_REQUEST)