from django import forms
from DB_app.models import User, Shop_Factor, Shop_Account, Menu, Ingredient, Customer_Factor, Courier, Address, \
    Factor_Ingredient, Factor_Menu, ManagerComment, UserComment


class UserForm(forms.ModelForm):
    # national_id = forms.CharField(max_length=10, min_length=10, required=True,
    #                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    # first_name = forms.CharField(max_length=20, required=True,
    #                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_name = forms.CharField(max_length=20, required=True,
    #                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    # phone_number = forms.CharField(max_length=11, min_length=11, required=True,
    #                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    # date_of_birth = forms.DateField(required=True)

    class Meta:
        model = User
        # fields = ('national_id', 'first_name', 'last_name', 'phone_number', 'date_of_birth', '')
        fields = '__all__'


class AddressForUserForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('address_path', 'fixed_phone_number', 'address_name')


class CourierForm(forms.ModelForm):
    # national_id = forms.CharField(max_length=10, min_length=10, required=True,
    #                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    # first_name = forms.CharField(max_length=20, required=True,
    #                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_name = forms.CharField(max_length=20, required=True,
    #                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    # phone_number = forms.CharField(max_length=11, min_length=11, required=True,
    #                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    # date_of_birth = forms.DateField(required=True,
    #                             widget=forms.DateField(attrs={'class': 'form-control'}))

    class Meta:
        model = Courier
        fields = '__all__'


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class Shop_FactorForm(forms.ModelForm):
    class Meta:
        model = Shop_Factor
        fields = '__all__'


class Shop_AccountForm(forms.ModelForm):
    class Meta:
        model = Shop_Account
        fields = '__all__'


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'


class Customer_FactorForm(forms.ModelForm):
    class Meta:
        model = Customer_Factor
        fields = '__all__'


class Factor_IngredientForm(forms.ModelForm):
    class Meta:
        model = Factor_Ingredient
        fields = '__all__'


class Factor_MenuForm(forms.ModelForm):
    class Meta:
        model = Factor_Menu
        fields = '__all__'


class UserCommentForm(forms.ModelForm):
    class Meta:
        model = UserComment
        fields = ('text',)


class ManagerCommentForm(forms.ModelForm):
    class Meta:
        model = ManagerComment
        fields = '__all__'
