from django.contrib import admin
from .models import Message, MessageRecipient, Call, CallRecording


admin.site.register(MessageRecipient),
admin.site.register(Message),
admin.site.register(Call),
admin.site.register(CallRecording)