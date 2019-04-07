from django.shortcuts import render

# Create your views here.
def time_table(req):
    return render(req, 'class_info/time_table.html')