from django.forms import ModelForm
from accounts.models import MyUser
from after_login.models import UserEdit,Transactions


class UserEditForm(ModelForm):
    class Meta:
        model = UserEdit
        fields = ['country','city','adress','phone_number','model_pic']


class Transactions_Form(ModelForm):
    class Meta:
        model = Transactions
        fields = ['type','quantity']