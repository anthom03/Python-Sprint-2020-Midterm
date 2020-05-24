from django.shortcuts import render

# Create your views here.


def index(request):
    """The home page for COVID Web."""
    return render(request, 'web_app/index.html')


def graph(request):
    """Show the COVID-19 graph."""
    return render(request, 'web_app/graph.html')


def graph_d_rates(request):
    """Show the COVID-19 death rates graph."""
    return render(request, 'web_app/graph_d_rates.html')
