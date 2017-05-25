from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.files.images import get_image_dimensions
from acme.models import UserProfile


#class UserProfileForm(forms.ModelForm):
#    class Meta:
#        model = UserProfile

#    def clean_avatar(self):
#        avatar = self.cleaned_data['avatar']

#        try:
#            w, h = get_image_dimensions(avatar)

            #validate dimensions
#            max_width = max_height = 100
#            if w > max_width or h > max_height:
#                raise forms.ValidationError(
#                    u'Please use an image that is '
#                     '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
#            main, sub = avatar.content_type.split('/')
#            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
#                raise forms.ValidationError(u'Please use a JPEG, '
#                    'GIF or PNG image.')

            #validate file size
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

class VendFijoForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=200, required=True)
    # last_name = forms.CharField(max_length=200, required=True)
    # avatar = forms.ImageField(upload_to=upload_location,default=1,blank=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    init_time = forms.TimeField(required=True)
    end_time = forms.TimeField(required=True)

    class Meta:
        model = User
        fields = ('username','email','password1', 'password2', 'init_time', 'end_time')

    def save(self,commit=True):
        #client = ProfileUser(super(UserForm, self).save(commit = False),forms.ImageField(upload_to=upload_location,default=1,blank=True))
        client = super(VendFijoForm, self).save(commit = False)
        client.email = self.cleaned_data['email']
        client.username = self.cleaned_data['username']
        client.init_time = self.cleaned_data['init_time']
        client.end_time = self.cleaned_data['end_time']
        password = self.clean_password()
        client.set_password(password)
        #if client.avatar:
        #    client.set_avatar()
        if commit:
            client.save()
        return client

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("password must match")
        return password1


def upload_location(instance, filename):
    PostModel = instance.__class__
    new_id = PostModel.objects.order_by("id").last().id + 1
    return "%s/%s" %(new_id, filename)

class UserForm(UserCreationForm):
    #Nuevos campos escritos deben ser convertidos en form
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=200,required=True)
    #last_name = forms.CharField(max_length=200, required=True)
    #avatar = forms.ImageField(upload_to=upload_location,default=1,blank=True)
    password1 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email','password1', 'password2')
        #fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def save(self,commit=True):
        #client = ProfileUser(super(UserForm, self).save(commit = False),forms.ImageField(upload_to=upload_location,default=1,blank=True))
        client = super(UserForm, self).save(commit = False)
        client.email = self.cleaned_data['email']
        client.username = self.cleaned_data['username']
        password = self.clean_password()
        print password
        client.set_password(password)
        print client.password
        #if client.avatar:
        #    client.set_avatar()
        if commit:
            client.save()
        return client

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("password must match")
        return password1
