from django.shortcuts import render
from django.contrib import messages
import requests
from django.http import HttpResponseRedirect

# Create your views here.
def display(request):
	query = request.GET.get("q")
	#print query
	url = 'https://mercury.postlight.com/parser?url='
	headers= {'Content-Type':'application/json','x-api-key':'PHPOY1bN6NVvFIw4jaQGJtCui4sX0H2J7gkUHAzn'}
	if(query):
		r= requests.get(url+query, headers=headers)
		json=r.json()
		#print json
		if 'error' in json:
			messages.success(request,"Please give a Valid Url")
			return HttpResponseRedirect('/')
		else:
			context_data = {'title':json['title'] , 'content':json['content']}
			return render(request,"display.html",context_data)
