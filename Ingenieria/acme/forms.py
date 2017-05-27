from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.files.images import get_image_dimensions
from acme.models import ClientProfile, VendedorFijoProfile, VendedorAmbProfile

CHOICES = [('../static/img/AvatarVendedor3.png', ), ('../static/img/AvatarVendedor2.png', 'test2'),
           ('../static/img/AvatarVendedor3.png', 'test3'), ('../static/img/AvatarVendedor4.png', 'test4')]


class VendAmbForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=200, required=True)
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    cash = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    debit = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    credit = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    student = forms.BooleanField(widget=forms.CheckboxInput(), required=False)

    class Meta:
        model = User
        fields = (
            'username', 'email', 'password1', 'password2', 'last_name', 'first_name', 'cash', 'debit', 'credit',
            'student')

    def save(self, commit=True):
        user = super(VendAmbForm, self).save(commit=True)
        password = self.clean_password()
        user.set_password(password)
        client = VendedorAmbProfile(user=user, cash=self.cleaned_data['cash'],
                                    debit=self.cleaned_data['debit'], credit=self.cleaned_data['credit'],
                                    student=self.cleaned_data['student'])
        if commit:
            client.save()
        return user

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("password must match")
        return password1


class VendFijoForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=200, required=True)
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    init_time = forms.TimeField(required=True)
    end_time = forms.TimeField(required=True)
    cash = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    debit = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    credit = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    student = forms.BooleanField(widget=forms.CheckboxInput(), required=False)

    class Meta:
        model = User
        fields = (
            'username', 'email', 'password1', 'password2', 'init_time', 'end_time', 'cash', 'debit', 'credit',
            'student',
            'first_name', 'last_name')

    def save(self, commit=True):
        user = super(VendFijoForm, self).save(commit=True)
        password = self.clean_password()
        user.set_password(password)
        client = VendedorFijoProfile(user=user, init_time=self.cleaned_data['init_time'],
                                     end_time=self.cleaned_data['end_time'], cash=self.cleaned_data['cash'],
                                     debit=self.cleaned_data['debit'], credit=self.cleaned_data['credit'],
                                     student=self.cleaned_data['student'])
        if commit:
            client.save()
        return user

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("password must match")
        return password1


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=200, required=True)
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=True)
        password = self.clean_password()
        user.set_password(password)
        client = ClientProfile(user=user)
        if commit:
            client.save()
        return user

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("password must match")
        return password1
