from django.shortcuts import render
from .models import Animal, Equipement


def listes_list(request):
    animals = Animal.objects.all()
    equipements = Equipement.objects.all()
    return render(request, 'blog/listes_liste.html', {'animals': animals, 'equipements': equipements })


