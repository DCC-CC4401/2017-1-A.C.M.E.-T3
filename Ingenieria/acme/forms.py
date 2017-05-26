from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.files.images import get_image_dimensions
from acme.models import ClientProfile, VendedorFijoProfile, VendedorAmbProfile


# class UserProfileForm(forms.ModelForm):
#    class Meta:
#        model = UserProfile

#    def clean_avatar(self):
#        avatar = self.cleaned_data['avatar']

#        try:
#            w, h = get_image_dimensions(avatar)

# validate dimensions
#            max_width = max_height = 100
#            if w > max_width or h > max_height:
#                raise forms.ValidationError(
#                    u'Please use an image that is '
#                     '%s x %s pixels or smaller.' % (max_width, max_height))

# validate content type
#            main, sub = avatar.content_type.split('/')
#            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
#                raise forms.ValidationError(u'Please use a JPEG, '
#                    'GIF or PNG image.')

# validate file size
#            if len(avatar) > (20 * 1024):
#                raise forms.ValidationError(
#                    u'Avatar file size may not exceed 20k.')

#        except AttributeError:
#            """
#            Handles case when we are updating the user profile
#            and do not supply a new avatar
#            """
#            pass

#        return avatar

class VendAmbForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=200, required=True)
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    # avatar = forms.ImageField(upload_to=upload_location,default=1,blank=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    cash = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    debit = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    credit = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    student = forms.BooleanField(widget=forms.CheckboxInput(), required=False)

    class Meta:
        model = User
        fields = (
            'username', 'email', 'password1', 'password2', 'last_name', 'first_name', 'cash', 'debit', 'credit', 'student')

    def save(self, commit=True):
        user = super(VendAmbForm, self).save(commit=True)
        password = self.clean_password()
        user.set_password(password)
        client = VendedorAmbProfile(user=user, cash=self.cleaned_data['cash'],
                                    debit=self.cleaned_data['debit'], credit=self.cleaned_data['credit'],
                                    student=self.cleaned_data['student'])
        # if client.avatar:
        #    client.set_avatar()
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
    # avatar = forms.ImageField(upload_to=upload_location,default=1,blank=True)
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
            'username', 'email', 'password1', 'password2', 'init_time', 'end_time', 'cash', 'debit', 'credit', 'student',
            'first_name', 'last_name')

    def save(self, commit=True):
        user = super(VendFijoForm, self).save(commit=True)
        password = self.clean_password()
        user.set_password(password)
        client = VendedorFijoProfile(user=user, init_time=self.cleaned_data['init_time'],
                                     end_time=self.cleaned_data['end_time'], cash=self.cleaned_data['cash'],
                                     debit=self.cleaned_data['debit'], credit=self.cleaned_data['credit'],
                                     student=self.cleaned_data['student'])
        # if client.avatar:
        #    client.set_avatar()
        if commit:
            client.save()
        return user

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("password must match")
        return password1


def upload_location(instance, filename):
    PostModel = instance.__class__
    new_id = PostModel.objects.order_by("id").last().id + 1
    return "%s/%s" % (new_id, filename)


class UserForm(UserCreationForm):
    # Nuevos campos escritos deben ser convertidos en form
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=200, required=True)
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    # avatar = forms.ImageField(upload_to=upload_location,default=1,blank=True)
    password1 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
        # fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def save(self, commit=True):
        # client = ProfileUser(super(UserForm, self).save(commit = False),forms.ImageField(upload_to=upload_location,default=1,blank=True))
        user = super(UserForm, self).save(commit=True)
        password = self.clean_password()
        user.set_password(password)
        client = ClientProfile(user=user)
        # if client.avatar:
        #    client.set_avatar()
        if commit:
            client.save()
        return user

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("password must match")
        return password1
