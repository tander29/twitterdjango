from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='../login')
def notification(request):
    html = 'notification.html'
    return render(request, html)
