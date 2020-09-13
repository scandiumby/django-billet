from django.urls import reverse
from django.views.generic import TemplateView


class CoreBasePagesView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['core_home_url'] = reverse('home')
        return context
