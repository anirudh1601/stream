from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .consumers import ChatConsumer
from channels.testing import ApplicationCommunicator
import pytest
import asyncio
from asgiref.sync import async_to_sync, sync_to_async
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# @pytest.mark.asyncio
# def home(request):
#   communicator = ApplicationCommunicator(ChatConsumer.as_asgi(), {"type": "http",})
#   event = await communicator.receive_output(timeout=1)
#   assert event["type"] == "http.response.start"
#   return HttpResponse('hello')


# @csrf_exempt
# @require_POST
# @pytest.mark.asyncio
# async def home(request):
#     if(request.body):
#         print('hello')
#         communicator = ApplicationCommunicator(ChatConsumer.as_asgi(), {"type": "http",})
#         response = await communicator.receive_output(timeout=1)
#         assert event["type"] == "http.response.start"

from django_eventstream import get_current_event_id
def home(request):
    return HttpResponse(get_current_event_id(['test']))