from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "Dashboard/index.html")

def previous_reports(request):
    return render(request, "Dashboard/previous_reports.html")