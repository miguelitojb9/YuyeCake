from django.forms import *

from app.yuyakake.models import CakeBase, CakeSize, CakeMeringue, CakeLayer, Cake


class CreateBaseForm(ModelForm):
    class Meta:
        model = CakeBase
        fields = '__all__'

class CreateCakeSizeForm(ModelForm):
    class Meta:
        model = CakeSize
        fields = '__all__'


class CreateMerengueForm(ModelForm):
    class Meta:
        model = CakeMeringue
        fields = '__all__'


class CreatePisosForm(ModelForm):
    class Meta:
        model = CakeLayer
        fields = '__all__'


class CreateCakeForm(ModelForm):
    class Meta:
        model = Cake
        fields = '__all__'
