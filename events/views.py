from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.views import View

# Create your views here.
def show_number(request, number):
    answer = f"""
    <html>
    <body>
    <p>The answer is {number}!</p>
    </body>
    </html>
    """
    return HttpResponse(answer)
