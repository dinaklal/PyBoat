import random
name = "PyBot"
weather = "Cloudy"
# Sentences we'll respond with if the user talks
responses = {
  "what's your name?": "my name is {0}".format(name),
  "what's today's weather?": "the weather is {0}".format(weather),
  "default": "default message"
}

def chats(sentence):
    if sentence.lower() in responses:
            return "PyBot : " + responses[ sentence ]
            