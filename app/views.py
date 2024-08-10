from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def jogadoras(request):
    jogadoras = [
        {"nome": "Marta", "idade": 38, "posicao": "Atacante", "local_de_nascimento": "Dois Riachos - AL", "foto": "marta.png"},
        {"nome": "Gabi Portilho", "idade": 29, "posicao": "Atacante", "local_de_nascimento": "Brasília - Distrito Federal", "foto": "gportilho.png"},
        {"nome": "Ludmila", "idade": 29, "posicao": "Atacante", "local_de_nascimento": "Guarulhos - SP", "foto": "ludmila.jpg"},
        {"nome": "Ana Vitória", "idade": 24, "posicao": "Meio-Campista", "local_de_nascimento": "Rondonópolis - Mato Grosso", "foto": "anavitoria.webp"},
        {"nome": "Yayá", "idade": 22, "posicao": "Meio-Campista", "local_de_nascimento": "Suzano - São Paulo", "foto": "yaya.webp"},
        {"nome": "Lorena", "idade": 27, "posicao": "Goleira", "local_de_nascimento": "Ituverava - São Paulo", "foto": "lorena.jpg"},
        {"nome": "Tarciane", "idade": 21, "posicao": "Zagueira", "local_de_nascimento": "Belford Roxo - Rio de Janeiro", "foto": "tarciane.jpg"},
        {"nome": "Tamires", "idade": 36, "posicao": "Lateral", "local_de_nascimento": "Caeté - Minas Gerais", "foto": "tamires.jpg"},
        {"nome": "Kerolin", "idade": 24, "posicao": "Atacante", "local_de_nascimento": "Bauru - São Paulo", "foto": "kerolin.webp"},
        {"nome": "Adriana", "idade": 27, "posicao": "Atacante", "local_de_nascimento": "União - Piauí", "foto": "adriana.webp"},
        {"nome": "Yasmin", "idade": 27, "posicao": "Lateral", "local_de_nascimento": "Governador Valadares - Minas Gerais", "foto": "yasmin.jpg"},
    ]
    context = {
        "jogadoras": jogadoras,
    }
    return render(request, "jogadoras.html", context)

def sobre(request):
    return render(request, "sobre.html")