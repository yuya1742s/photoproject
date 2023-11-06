from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationFrom
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = CustomUserCreationFrom
    template_name = "signup.html"
    success_url = reverse_lazy('accounts:signup_success')

    def form_valid(self, form):
        user = form.save()
        self.object = user
        return super().form_valid(form)
    
class SignUpSuccessView(TemplateView):
    template_name = "signup_success.html"
        
