from django.shortcuts import render
from django.http import HttpResponse    
from django.contrib.auth.decorators import login_required
from home.report import return_graph
import matplotlib.pyplot as plt
import io
import urllib, base64

# Create your views here.
def home(request):
    # return render(request, 'home/welcome.html', {})
    plt.switch_backend('Agg')
    plt.plot(range(10))
    fig = plt.gcf()
    #convert graph into dtring buffer and then we convert 64 bit code into image
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    return render(request,'home/welcome.html',{'data':uri})

@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})