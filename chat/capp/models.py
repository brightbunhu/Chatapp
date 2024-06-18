from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='sent_messages')
    recipients = models.ManyToManyField(User, related_name='received_messages')

    def __str__(self):
        return f"Message from {self.sender.username} at {self.created_at}"

class MessageRecipient(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.message.content} - {self.recipient.username}"

class Call(models.Model):
    caller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='outgoing_calls')
    callee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incoming_calls')
    call_time = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=10, default='ringing')

    def __str__(self):
        return f"{self.caller.username} called {self.callee.username} at {self.call_time}"

    def mark_as_answered(self):
        self.status = 'answered'
        self.duration = (timezone.now() - self.call_time).seconds
        self.save()

class CallRecording(models.Model):
    call = models.ForeignKey(Call, on_delete=models.CASCADE, related_name='recordings')
    recording = models.FileField(upload_to='call_recordings/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recording of call from {self.call.caller.username} to {self.call.callee.username} at {self.created_at}"