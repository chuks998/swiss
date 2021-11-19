from django.shortcuts import render, redirect
from .models import AccountDetail, Verify
from django.db.models import F
from django.views.generic import ListView
from django.contrib.auth.models import User
from.forms import ProofOfAccount, ProofOfIdentity, ProofOfResidence



# Create your views here.
def landing_page(request):
    template = 'index.html'
    return render(request, template)



def logout_user(request):
    del request.session['user']
    return redirect('index')



class ProfileView(ListView):

    model = AccountDetail
    template_name = 'dashboard.html'
    context_object_name = 'dashboard'
    queryset = AccountDetail.objects.all()

    def get_context_data(self, **kwargs):

        context = super(ProfileView, self).get_context_data(**kwargs)
        context['account'] = AccountDetail.objects.all()
        context['verify'] = Verify.objects.all()
        
        return context

    def save(self):
        super().save()


    def transfer(request,):
        error_template = 'transfer_error.html'
        success_template = 'transfer_success.html'
        # success_template = 'transfer_success.html'

        
        if request.method == 'POST':
            try:
                username = request.POST['username']
                amount = request.POST['amount']
                senderUser = User.objects.get(username=username)
                recieverUser = request.POST['acct-num']
                sender = AccountDetail.objects.get(account_holder = senderUser)
                debit = False
                if int(amount) > sender.account_balance or int(amount) < 0:
                    msg = 'you can not transfer above your account balance'
                    debit = False
                    context = {'msg': msg}
                    return render(request, error_template, context)
                else:
                    sender.account_balance = F('account_balance')- int(amount)
                    sender.save()
                    debit = True
                    context={
                        'reciver': recieverUser,
                        'amount': amount,
                        'debit': debit,
                    }
                    return render(request, success_template,  context)
            except Exception as e:
                msg = 'you cannot perform this operation!'
                context = {'e': msg}
                return render(request, error_template, context)



    
    def proof_of_account(request):
        if request.method == 'POST':
            p_account= ProofOfAccount(request.POST, request.FILES, instance=request.user.verify)
            # p_identity= ProofOfAccount(request.POST, request.FILES, instance=request.user.verify)

            if p_account.is_valid():
                p_account.save()
                return redirect('dash')
        else:
            p_account = ProofOfAccount(instance=request.user.verify)

        context = {
            'p_account': p_account,
        }
        return render(request, 'poa.html', context)
                

    
    def proof_of_residence(request):
        if request.method == 'POST':
            p_residence= ProofOfResidence(request.POST, request.FILES, instance=request.user.verify)
            # p_identity= ProofOfAccount(request.POST, request.FILES, instance=request.user.verify)

            if p_residence.is_valid():
                p_residence.save()
                return redirect('dash')
        else:
            p_residence = ProofOfResidence(instance=request.user.verify)

        context = {
            'p_residence': p_residence,
        }
        return render(request, 'por.html', context)
                

    def proof_of_identity(request):
        if request.method == 'POST':
            p_identity= ProofOfIdentity(request.POST, request.FILES, instance=request.user.verify)

            if p_identity.is_valid():
                p_identity.save()
                return redirect('dash')
        else:
            p_identity = ProofOfIdentity(instance=request.user.verify)

        context = {
            'p_identity': p_identity,
        }
        return render(request, 'poi.html', context)
                
