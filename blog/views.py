from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to the Katya blog<h2>")

def post(request):
    return HttpResponse(f"""<h1>Viewing Katya's posts from X</h1>
                        <body> VOTE TRUMP! VIVA UKRAINE </body>""")

def categories(request):
    return HttpResponse(
        "<h1>categories</h1>"
        """<body> 
        War <br>
        Katya on Monday <br>
        Katya on Tuesday <br>
        Katya on Wednesday <br>
        Katya on Thursday (Paid only) <br>
        Katya on Friday! <br>
        Katya on Saturday (Paid only) <br>
        Katya on Sunday (Classified) <br>
        Politics <br>
        Sports <br>
        Science <br>
        </body>"""
    )