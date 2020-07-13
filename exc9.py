def speak(str):

    from win32com.client import Dispatch

    speak=Dispatch("SAPI.spVoice")

    speak.Speak(str)



if __name__== '__main__':

    import requests

    import json

    url = ('https://newsapi.org/v2/top-headlines?'

           'sources=bbc-sport&'

           'apiKey=807c6e7af3464b9088f13991539b47ad')



    response = requests.get(url)

    text = response.text

    my_json = json.loads(text)

    for i in range(0, 11):

        speak(my_json['articles'][i]['title'])