from django.shortcuts import render
from .models import CashOutFlow, Revenue
from django.views.generic import ListView, CreateView
from finances.forms import CashOutFlowForm, RevenueForm


class CashOutFlowListView(ListView):
    model = CashOutFlow
    template_name = 'cashout_list.html'
    context_object_name = 'cashoutflows'
    ordering = ['-date']



class CashOutFlowCreateView(CreateView):
    model = CashOutFlow
    form_class = CashOutFlowForm
    template_name = 'cashoutcreate.html'
    success_url = '/cashoutflows/'


class RevenueListView(ListView):
    model = Revenue
    context_object_name = 'revenues'
    template_name = 'revenues.html'
    ordering = ['-date']


class RevenueCreateView(CreateView):
    model = Revenue
    form_class = RevenueForm
    template_name = 'createrevenue.html'
    success_url = '/revenues/'