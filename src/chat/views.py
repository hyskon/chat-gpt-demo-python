from django.shortcuts import render
from django.http import HttpResponse
import openai
from .models import Conversation, Message

# Create your views here.
def home(request):
    # Initialize chat input and chat response
    chat_input = ''
    chat_response = ''

    # Check if there is chat input
    if 'chat_input' in request.POST:
        # Get chat input from user
        chat_input = request.POST.get('chat_input')

        # Create new conversation
        conversation = Conversation.objects.create()

        # Use GPT-2 model to generate a response
        openai.api_key = "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"
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"User: {chat_input}\nBot: ",
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Get response text
        chat_response = response['choices'][0]['text']

        # Create new message
        Message.objects.create(
            conversation=conversation,
            question=chat_input,
            answer=chat_response,
        )

    # Render chat template with chat input and chat response
    return render(request, 'chat/index.html', {
        'chat_input': chat_input,
        'chat_response': chat_response,
    })