# Chat App
This is a chat app where you can have conversations with an AI.

## Features
- Create new conversations
- View all previous conversations
- Chat with the chatbot using natural language
- View a history of previous messages in the current conversation

## Prerequisites
- Python 3.6 or higher
- Django 2.2 or higher
- OpenAI API key

## Installation
1. Clone the repository
```
git clone https://github.com/user/repo.git
```
2. Navigate to the project directory
```
cd chat_app
```
3. Install the required packages
```
pip install -r requirements.txt
```
4. Set the OpenAI API key as an environment variable
```
export OPENAI_API_KEY=YOUR_API_KEY
```
5. Run the migration files to create the necessary database tables
```
python manage.py migrate
```
6. Run the development server
```
python manage.py runserver
```
7. Open the app in your browser at http://localhost:8000


## Usage
1. Click on the "New conversation" button to create a new conversation.
2. Type in a message in the text field and press enter or click the send button to send the message to the chatbot.
3. View the conversation history by clicking on a previous conversation in the "Conversations" list.


## Build with
Django - The web framework used
OpenAI - The AI platform used to generate responses

## Authors
Hylke Nicola - Initial work
