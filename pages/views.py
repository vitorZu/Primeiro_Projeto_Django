from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User



class IndexView(TemplateView):
    template_name = "index.html"

class RegisterView(TemplateView):
    template_name = "register.html"


def Store(request):
    data = {}
    if(request.POST['subButton'] == "register"):
        user = User.objects.create_user(request.POST['userField'], request.POST['emailField'], request.POST['passField'])
        user.first_name = request.POST['nameField']
        user.save()
        data['msg'] = 'Usuário cadastrado'
    else:
        data['msg'] = 'Deu ruim'

    return render(request, "register.html" ,data),
