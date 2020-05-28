import apiai
import json

def send_message(message):
    request = apiai.ApiAI('47e54f47c4534c4cbc8041a3debfa028').text_request() #Token API to DialogFlow
    request.lang = 'en' #Language of request 'en', 'ru'
    request.session_id = 'session_1' #ID of the session of the dialog(we need it it to teach the bot)
    request.query = message #Send the request to Artifitial Intellengence with the user message
    response = json.loads(request.getresponse().read().decode('utf-8'))
    print(response['result']['fulfillment']['speech']) #Decomposing JSON and exctract the answer
    # If we have the answer from the bot - send it to the user, if don't - bot did not understand him
    return response['result']['action']

print('Input your message or go out type something like "Bye": ')
message = input()
action = None
while message != True:
    action = send_message(message)
    if action == 'smalltalk.greetings.bye':
        break
    message = input()

