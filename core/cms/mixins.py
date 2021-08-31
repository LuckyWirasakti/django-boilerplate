from extra_views.contrib.mixins import SearchableListMixin
from django_tables2.views import SingleTableView

class SingleSearchTableView(SearchableListMixin, SingleTableView):
    breadcrumb = {}

    def get_search_fields(self):
        return self.search_fields
    
    def get_breadcrumb(self):
        return self.breadcrumb

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_table_name].search_fields = self.get_search_fields()
        context[self.context_table_name].breadcrumb = self.extra_context
        print(context[self.context_table_name].breadcrumb)
        return context