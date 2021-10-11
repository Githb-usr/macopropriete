from django.shortcuts import render

def show_index(request):
    """
    We display the homepage of the application
    :return: a template
    """
    return render(request, 'pages/index.html')