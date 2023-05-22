from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "restaurantly_Vanderstraeten_kevin/home.html")

def about(request):
    return render(request, "restaurantly_Vanderstraeten_kevin/about.html")

def menu(request):
    return render(request, "restaurantly_Vanderstraeten_kevin/menu.html")

def specials(request):
    return render(request, "restaurantly_Vanderstraeten_kevin/specials.html")

def events(request):
    return render(request, "restaurantly_Vanderstraeten_kevin/events.html")

def chefs(request):
    return render(request, "restaurantly_Vanderstraeten_kevin/chefs.html", {"tableauChefs" : tableauChefs})

def gallery(request):
    return render(request, "restaurantly_Vanderstraeten_kevin/gallery.html")

def contact(request):
    return render(request, "restaurantly_Vanderstraeten_kevin/contact.html")

def book(request):
    return render(request, "restaurantly_Vanderstraeten_kevin/book.html")

def why_us(request):
    return render(request, "restaurantly_Vanderstraeten_kevin/why.html")

def testimonials(request):
    return render(request, "restaurantly_Vanderstraeten_kevin/testimonials.html")

def chef_details(request,id):
    chef = tableauChefs[id]
    return render(request, "restaurantly_Vanderstraeten_kevin/chef_details.html", {"chef":chef})


tableauChefs = [
        {"nameChef": "Walter White", "functionChef": "Master Chef", "imgChef": "cafe/img/chefs/chefs-1.jpg", "id": 0},
        {"nameChef": "Sarah Jhonson", "functionChef": "Patissier", "imgChef": "cafe/img/chefs/chefs-2.jpg", "id": 1},
        {"nameChef": "William Anderson", "functionChef": "Cook", "imgChef": "cafe/img/chefs/chefs-3.jpg", "id": 2},
        ]


# tableauChefs2 = [
#     {"imgChef": "{% static 'cafe/img/chefs/chefs-1.jpg' %}", "id": 0},
#     {"imgChef": "{% static 'cafe/img/chefs/chefs-2.jpg' %}", "id": 1},
#     {"imgChef": "{% static 'cafe/img/chefs/chefs-3.jpg' %}", "id": 2},
# ]

