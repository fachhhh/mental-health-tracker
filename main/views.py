from django.shortcuts import render

def show_main(request):
    context = {
        "npm" : "2306245030",
        "name" : "Hadyan Fachri",
        "class" : "PBP A"
    }

    return render(request,"main.html",context)