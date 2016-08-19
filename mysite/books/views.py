from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.template import Context

from books.forms import AddForm
from django.views.generic.edit import FormView

class AddBookView(FormView):
    template_name = 'add_form.html'
    success_url = '/books/'
    form_class = AddForm

    def form_valid(self, form):
        sg = form.save()
        print (sg.__dict__)

        messages.info( self.request, "successfully added" )
        return super(AddBookView, self).form_valid(form)
