from django.shortcuts import render
from .models import *
# Create your views here.
def sortReport(report):
    return report.dateTime
def index(request):
    reportObjects = Report.objects.filter(subject=request.user)
    reports = []
    for report in reportObjects:
        reports.append(report)
    reports.sort(key=sortReport, reverse=True)
    report = reports[0]
    return render(request, "Dashboard/index.html", {
        "report": report
    })

def previous_reports(request):
    reportObjects = Report.objects.filter(subject=request.user)
    reports = []
    for report in reportObjects:
        reports.append(report)
    reports.sort(key=sortReport, reverse=True)
    previousReports = reports[1:]
    return render(request, "Dashboard/previous_reports.html", {
        "previousReports": previousReports
    })