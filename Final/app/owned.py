from django.views.generic import FormView, CreateView, DetailView, UpdateView, DeleteView, ListView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Owned Rows Mixins
class OwnerListView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        print('update get_queryset called')
        qs = super(OwnerListView, self).get_queryset()
        return qs.filter(user=self.request.user)

class OwnerDetailView(LoginRequiredMixin, DetailView):

    def get_queryset(self):
        print('update get_queryset called')
        qs = super(OwnerDetailView, self).get_queryset()
        return qs.filter(user=self.request.user)

class OwnerCreateView(LoginRequiredMixin, CreateView):
    def form_valid(self, form):
        print('form valid called')
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super(OwnerCreateView, self).form_valid(form)

class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    def get_queryset(self):
        print('update get_queryset called')
        qs = super(OwnerUpdateView, self).get_queryset()
        return qs.filter(user=self.request.user)

class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    def get_queryset(self):
        print('update get_queryset called')
        qs = super(OwnerDeleteView, self).get_queryset()
        return qs.filter(user=self.request.user)
