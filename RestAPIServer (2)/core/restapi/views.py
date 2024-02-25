from rest_framework import generics, status
from django.contrib.auth.models import User
from .models import *
from .handlers import *

from rest_framework.response import Response
from rest_framework.views import APIView

import base64
import asyncio

from .bot import bot

# Create your views here.
class SendMessage(APIView):
    
    def post(self, request):
        req = request_key(request, ['uuid', 'image'])
        if not req[0]:
            return req[1]
        base64_string = request.data['image']
        image_bytes = base64.b64decode(base64_string)
        async def send():
            await bot.send_photo(chat_id=request.data['uuid'], photo=image_bytes)
            return await bot.send_message(request.data['uuid'], text="Face")


        asyncio.run(send())
        print(request.data['uuid'])
        return Response(content_type=200, data=request.data['uuid'])


