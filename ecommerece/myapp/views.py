from django.shortcuts import render, redirect

@login_required
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    if request.method == 'POST':
        pass
