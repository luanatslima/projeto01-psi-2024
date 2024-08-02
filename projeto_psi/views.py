from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def jogadoras(request):
    jogadoras = [
        {"nome": "Marta", "idade": "38", "posição": "Atacante", "local de nascimento": "Dois Riachos - AL", "foto": "marta.png"}
        {"nome": "Antônia", "idade": "", "posição": "", "local de nascimento": "", "foto": ""}
        {"nome": "Ludmila", "idade": "29", "posição": "Atacante", "local de nascimento": "Guarulhos - SP", "foto": "ludmila.jpg"}
        {"nome": "Cristiane", "idade": "39", "posição": "Atacante", "local de nascimento": "Osasco - SP", "foto": "cristiane.webp"}
    ]
    context = {
        "jogadoras" : jogadoras,
    }
    return render(request, "jogadoras.html", context)


def sobre(request):
    return render(request, "sobre.html")