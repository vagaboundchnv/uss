from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    """
    It will redirect to index
    """
    return render(request, 'index.html')

@login_required
def partials(request, template_name):
    """
    It will redirect to index
    """
    return render(request, 'partials/' + template_name)
