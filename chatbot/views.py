from django.shortcuts import render 
from django.http import JsonResponse 
import json
  
from .chat import get_response

def chatbot_view(request):
    print("Chatbot view called")
    if request.method == 'POST':
        #print("Post called")
        data = json.loads(request.body)
        user_message = data.get('message')
        #print(f"User message: {user_message}")  # Debug line
        #print(request.POST)
        #user_message = request.POST.get('message')
        if user_message is not None:
            #print("User defined")
            bot_response = get_response(user_message)
            #print(f"Bot response: {bot_response}")
        else:
            bot_response = "Sorry, I didn't understand that."
        return JsonResponse({'response': bot_response})
    else:
        return render(request, 'index-2.html')
    
    
#def query_view(request): 
 ##      prompt = request.POST.get('prompt') 
   #     try:
    ###      response = "get_completion(prompt) failed" 
       # return JsonResponse({'response': response}) 
    
    #return render(request, 'index-2.html') 
