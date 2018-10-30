import random
name = "PyBot"
weather = "Cloudy"
# Sentences we'll respond with if the user talks
responses = {
  "what's your name?": ["my name is {0}".format(name),
    "they call me {0}".format(name),
      "I go by {0}".format(name)],
  "what's today's weather?": ["the weather is {0}".format(weather),"it's {0} today".format(weather)],
  "default": ["Sorry,Not Getting your language", "What are you talking",""]
}

def chats(sentence):
    if sentence.lower() in responses:
            return "PyBot : " + random.choice(responses[ sentence ])
    else:
         return "PyBot : " + random.choice(responses["default"])
            