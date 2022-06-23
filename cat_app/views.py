from django.shortcuts import render
from django.http import HttpResponse
import os
from dotenv import load_dotenv
import requests
# from requests_oauthlib import OAuth1
load_dotenv()


# Create your views here.
def index(request):
    
    key = os.environ['apikey']
    response = render(request, 'cat_app/index.html', { "hello": "cats"})
    return response

def get_some_cats(request):
    key = os.environ['apikey']
    header = {"api_key":key}
    response = requests.get(f"https://api.thecatapi.com/v1/images/search?limit=5&page=10&order=Desc", headers=header)
    responseJSON = response.json()
    cat_url = responseJSON[0]['url']

    return render(request, 'cat_app/getcats.html', {'preview_url' : cat_url})
    