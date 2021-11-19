from django.db import models
import string, random
from django.contrib.auth.models import User

# account number genarator
def account_genarator(length=11, var=string.digits):
        return ''.join(random.choice(var) for _ in range(length))


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.account_holder.username, filename)



class AccountDetail(models.Model):
    account_holder = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(default=account_genarator, max_length=11, unique=True, blank=True, null=True)
    account_balance = models.FloatField(default=0.00)
    
    class META:
        verbose_name_plural = 'AccountDetail'

    def __str__(self):
        return f'{self.account_holder} account({self.account_number})'

    def save(self):
            super().save()

class Verify(models.Model):
    account_holder = models.OneToOneField(User, on_delete=models.CASCADE)
    proof_of_identity = models.ImageField(verbose_name='proof of identity', upload_to=user_directory_path)
    proof_of_residence = models.ImageField(verbose_name='proof of residence', upload_to=user_directory_path)
    proof_of_account = models.ImageField(verbose_name='proof of account', upload_to=user_directory_path)

    class META:
        verbose_name_plural = 'Verification'
    
    def save(self):
            super().save()
    
    def __str__(self):
        return f'{self.account_holder} photo of verification'