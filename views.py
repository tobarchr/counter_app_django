from django.shortcuts import render, redirect

def index(request):
    if 'counter' not in request.session:        
        request.session['counter'] = 0
    else:
        request.session['counter'] +=1
    print("a GET request is being made to this route")
    print(request.session['counter'])
    return render (request,"index.html")

def destroy(request):
    del request.session['counter']
    return redirect('/')
    print(request.session['counter'])

def counter2(request):
    request.session['counter'] +=1
    return redirect('/')
    print(request.session['counter'])

