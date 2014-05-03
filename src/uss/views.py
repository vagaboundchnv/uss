from django.shortcuts import render

def index(request):
    """
    It will redirect to index
    """
    return render(request, 'index.html')

def partials(request, template_name):
    """
    It will redirect to index
    """
    return render(request, 'partials/' + template_name + '.html')
