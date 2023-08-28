from django.views.generic import TemplateView

class HomeView(TemplateView):
    http_method_names = ['get']
    template_name = "core/home.html"
