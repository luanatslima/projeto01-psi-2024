from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def jogadoras(request):
    jogadoras = [
        {"nome": "Marta", "idade": "40", "posição": "", "local de nascimento": "", "foto": ""}
        {"nome": "Antônia", "idade": "", "posição": "", "local de nascimento": "", "foto": ""}
        {"nome": "", "idade": "", "posição": "", "local de nascimento": "", "foto": ""}
        {"nome": "", "idade": "", "posição": "", "local de nascimento": "", "foto": ""}
    ]
    context = {
        "jogadoras" : jogadoras
    }
    return render(request, "jogadoras.html", context)


def sobre(request):
    return render(request, "sobre.html")