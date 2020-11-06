import requests
import json

# yes i copied this function im too lazy to write it myself 
def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values


def translate_api(text, lang):
    text =[{
    'Text': text
    }]

    key = "82e622ccc27b4ad0af0918182329a742"
    region = 'westeurope'
    content = 'application/json'

    parameters = {
    'Ocp-Apim-Subscription-Key': key, 
    'Ocp-Apim-Subscription-Region': region,
    'Content-Type': content
    }

    url = "https://api.cognitive.microsofttranslator.com/translate"
    api = "?api-version=3.0"
    a_lang = "&to=" + lang
    complete_url =  url + api + a_lang

    request = requests.post(complete_url, headers = parameters, json = text)
    response = request.json()

    translated = json_extract(response, 'text')

    final = ''.join(translated) #list into str

    return final



print("Opening file... ")
file_out= open("translations.txt","a+") #we are going to write here and its appendable
file_in = open("input.txt", "r", encoding="utf-8") # initial text to translate


lang = input('Choose language: ') 

for line in file_in:
    print("Input text: ", line) 
    t = translate_api(line, lang)
    print("Translated text: ", t)
    file_out.write(t)






