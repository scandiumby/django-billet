from .base import CoreBasePagesView


class CoreHomeView(CoreBasePagesView):
    template_name = 'core/pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
