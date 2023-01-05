from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
import openai
from .models import Conversation, Message
from .forms import NewConversationForm

# Create your views here.
def home(request):    
    # Get all conversations
    conversations = Conversation.objects.all()
    # Create new conversation if the new chat button is clicked
    form = NewConversationForm()
    if request.method == 'POST':
    # Get form data
        form = NewConversationForm(request.POST)
        # Validate form data
        if form.is_valid():
            # Create new conversation
            conversation = form.save()
            # Redirect to new conversation
            return redirect('app', conversation_id=conversation.id)
        else:
            form = NewConversationForm()    
    # Render home template with conversations
    return render(request, 'chat/index.html', {
    'conversations': conversations,
    'form': form,
    })

def app(request, conversation_id):
    # Initialize chat input and chat response
    prompt = ''
    chat_response = ''
    
    # get conversation and messages 
    conversation = get_object_or_404(Conversation, pk=conversation_id)
    messages = Message.objects.filter(conversation=conversation)    
    
    # Check if there is the user submitted question
    if 'prompt' in request.POST:
        # Get chat input from user
        prompt = request.POST.get('prompt')
               
        # Use GPT-2 model to generate a response
        openai.api_key = "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"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{prompt}",
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )       

        # Get response text
        chat_response = response['choices'][0]['text'].strip()

        # Create new message
        Message.objects.create(
            conversation=conversation,
            question=prompt,
            answer=chat_response,
        )
        # return redirect('app', conversation_id=conversation.id)
    # Render chat template with chat input and chat response
    return render(request, 'chat/conversation.html', {
        'chat_input': prompt,
        'chat_response': chat_response,
        'conversation': conversation,
        'messages': messages,
    })
