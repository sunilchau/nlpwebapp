import paralleldots

paralleldots.set_api_key('n4rRnNWFOQdGU5rRUQc28pa74L0HZ52SQSdxx4KPHlY')

def ner(text):
    nertext = paralleldots.ner(text)
    return nertext




