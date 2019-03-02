from django.shortcuts import render, redirect
from .mf import UserUF, UserRF, BuyF
from django.contrib import messages
from .models import Meds
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView


def delmed(mid):

    Meds.objects.filter(id=mid).delete()

def home(request):

    for x in Meds.objects.filter(qunt=0):
        delmed(x.id)
    meds = Meds.objects.all()
    return render(request,'mtfD/home.html',{'TIT':'Home|Page','meds':meds})

def buyer(request):

    if request.method == 'POST':
        form = UserRF(request.POST)
        if form.is_valid():
            un = form.cleaned_data['username']
            form.save()
            typ = User.objects.filter(username=un).first()
            typ.user_type.is_buyer=True
            typ.user_type.is_saler=False
            typ.user_type.is_agent=False
            typ.save()
            messages.success(request,f'sailer register successfully :) ')
            return redirect('blog-home')
    else:
        form = UserRF()
    return render(request,'mtfD/buyer.html',{'TIT':'Buyer|Page','form':form})

def saler(request):

    if request.method == 'POST':
        form = UserRF(request.POST)
        if form.is_valid():
            un = form.cleaned_data['username']
            form.save()
            typ = User.objects.filter(username=un).first()
            typ.user_type.is_buyer=False
            typ.user_type.is_saler=True
            typ.user_type.is_agent=False
            typ.save()
            messages.success(request,f'sailer register successfully :)')
            return redirect('blog-home')
    else:
        form = UserRF()
    return render(request,'mtfD/saler.html',{'TIT':'Saler|Page','form':form})

def agent(request):

    if request.method == 'POST':
        form = UserRF(request.POST)
        if form.is_valid():
            un = form.cleaned_data['username']
            form.save()
            typ = User.objects.filter(username=un).first()
            typ.user_type.is_buyer=False
            typ.user_type.is_saler=False
            typ.user_type.is_agent=True
            typ.save()
            messages.success(request,f'Agent register successfully :)')
            return redirect('blog-home')
    else:
        form = UserRF()
    return render(request,'mtfD/agent.html',{'TIT':'Agent|Page','form':form})

@login_required
def profile(request):

    if request.method == 'POST':
        form = UserUF(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile Update successfully')
            redirect('profile')
    else:
        form = UserUF(instance=request.user)
    context = {
        'TIT':'Profile|Page',
        'form':form
        }
    return render(request,'mtfD/profile.html',context)

med_pk = -1

class med_detailview(DetailView):
    

    model = Meds
    template_name = 'mtfD/detailview.html'

    def get_context_data(self, **kwargs):

        global med_pk
        context = super().get_context_data(**kwargs)
        context['TIT'] = 'Detail|Med'
        med_pk = self.kwargs['pk']
        return context

@login_required
def buy(request):

    global med_pk
    amount = 0
    qunt = 0
    if request.user.user_type.is_buyer:
        if request.method == 'POST':
            form = BuyF(request.POST)
            z = Meds.objects.filter(id=med_pk).first()
            if form.is_valid() and qunt <= z.qunt :
                qunt = form.cleaned_data['qunt']
                z = Meds.objects.filter(id=med_pk).first()
                amount = z.price * qunt
                z.qunt -= qunt
                z.save()
                messages.success(request,f'You have succesfully buyed Med {z.name}')
                return redirect('blog-home')
        else:
            form = BuyF()

        return render(request, 'mtfD/buy.html', {'TIT':'Buy|Page','amount':amount,'form':form,'med_pk':med_pk})        

class add_med(LoginRequiredMixin, CreateView):


    model = Meds
    fields = ['name','price','qunt']
    template_name = 'mtfD/add.html'
    def form_valid(self, form):

        form.instance.user = self.request.user
        if form.instance.user.user_type.is_saler :
            return super().form_valid(form)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['TIT'] = 'Add|Med'
        return context

class update_med(LoginRequiredMixin, UserPassesTestMixin, UpdateView):


    model = Meds
    fields = ['name','price','qunt']
    template_name = 'mtfD/add.html'

    def form_valid(self,form):

        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):

        med = self.get_object()
        if med.user == self.request.user:
            return True
        else:
            return False

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['TIT'] = 'Update|Med'
        return context

class del_meds(LoginRequiredMixin, UserPassesTestMixin, DeleteView):


    model = Meds
    template_name = 'mtfD/del.html'
    success_url = '/med/'

    def form_valid(form):

        self.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):

        med = self.get_object()
        if med.user == self.request.user:
            return True
        else:
            return False

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['TIT'] = 'Delete|Med'
        return context