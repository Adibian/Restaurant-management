from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver


class User(models.Model):
    national_id = models.CharField(max_length=10, validators=[MinLengthValidator(10)], null=False, primary_key=True,
                                   unique=True)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    phone_number = models.CharField(max_length=11, validators=[MinLengthValidator(11)], null=False)
    date_of_birth = models.DateField(null=False)

    def __str__(self):
        # return self.first_name + " " + self.last_name
        return str(self.national_id)


class UserLog(models.Model):
    before_action = models.CharField(max_length=300, null=True, blank=True)
    after_action = models.CharField(max_length=300, null=True, blank=True)
    time = models.DateTimeField(default=timezone.now)
    user = models.CharField(max_length=300, null=True, blank=True)
    #
    # def __str__(self):
    #     return str(self.after_action)[:]


class Address(models.Model):
    address_name = models.CharField(max_length=20, null=False)
    address_path = models.CharField(max_length=200, null=False)
    fixed_phone_number = models.CharField(max_length=11, validators=[MinLengthValidator(11)], null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address')

    class Meta:
        unique_together = (('address_name', 'user'),)

    def __str__(self):
        return self.address_path


class AddressLog(models.Model):
    before_action = models.CharField(max_length=300, null=True, blank=True)
    after_action = models.CharField(max_length=300, null=True, blank=True)
    time = models.DateTimeField(default=timezone.now)
    key = models.CharField(max_length=300, null=True, blank=True)


class Menu(models.Model):
    food_name = models.CharField(max_length=20, null=False, primary_key=True, unique=True)
    price = models.IntegerField(validators=[MinValueValidator(0)], null=False)

    def __str__(self):
        return self.food_name


class MenuLog(models.Model):
    before_action = models.CharField(max_length=300, null=True, blank=True)
    after_action = models.CharField(max_length=300, null=True, blank=True)
    time = models.DateTimeField(default=timezone.now)
    key = models.CharField(max_length=300, null=True, blank=True)


class Courier(models.Model):
    national_id = models.CharField(max_length=10, validators=[MinLengthValidator(10)], null=False, primary_key=True,
                                   unique=True)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    phone_number = models.CharField(max_length=11, validators=[MinLengthValidator(11)], null=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class CourierLog(models.Model):
    before_action = models.CharField(max_length=300, null=True, blank=True)
    after_action = models.CharField(max_length=300, null=True, blank=True)
    time = models.DateTimeField(default=timezone.now)
    key = models.CharField(max_length=300, null=True, blank=True)


class Customer_Factor(models.Model):
    factor_number = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    order_time = models.DateTimeField(null=False, default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.factor_number)


class Customer_FactorLog(models.Model):
    before_action = models.CharField(max_length=300, null=True, blank=True)
    after_action = models.CharField(max_length=300, null=True, blank=True)
    time = models.DateTimeField(default=timezone.now)
    key = models.CharField(max_length=300, null=True, blank=True)


class Factor_Menu(models.Model):
    factor = models.ForeignKey(Customer_Factor, on_delete=models.CASCADE, null=False)
    food = models.ForeignKey(Menu, on_delete=models.CASCADE, null=False)
    food_name = models.CharField(max_length=20, null=False)
    price = models.IntegerField(validators=[MinValueValidator(0)], null=False)
    number = models.IntegerField(validators=[MinValueValidator(0)], null=False)

    class Meta:
        unique_together = (('factor', 'food_name'),)

    def __str__(self):
        return str(self.factor) + ' ' + str(self.food_name)


class Factor_MenuLog(models.Model):
    before_action = models.CharField(max_length=300, null=True, blank=True)
    after_action = models.CharField(max_length=300, null=True, blank=True)
    time = models.DateTimeField(default=timezone.now)
    key = models.CharField(max_length=300, null=True, blank=True)


class Shop_Account(models.Model):
    shop_name = models.CharField(max_length=20, null=False, primary_key=True)
    active = models.BooleanField(null=False, default=True)

    def __str__(self):
        return self.shop_name


class Shop_AccountLog(models.Model):
    before_action = models.CharField(max_length=300, null=True, blank=True)
    after_action = models.CharField(max_length=300, null=True, blank=True)
    time = models.DateTimeField(default=timezone.now)
    key = models.CharField(max_length=300, null=True, blank=True)


class Ingredient(models.Model):
    item_name = models.CharField(max_length=20, null=False)
    shop_name = models.ForeignKey(Shop_Account, on_delete=models.CASCADE, null=Factor_Menu)
    price = models.IntegerField(default=0, validators=[MinValueValidator(0)], null=False)

    class Meta:
        unique_together = (('shop_name', 'item_name'),)


class IngredientLog(models.Model):
    before_action = models.CharField(max_length=300, null=True, blank=True)
    after_action = models.CharField(max_length=300, null=True, blank=True)
    time = models.DateTimeField(default=timezone.now)
    key = models.CharField(max_length=300, null=True, blank=True)


class Shop_Factor(models.Model):
    factor_number = models.AutoField(primary_key=True)
    shop_name = models.ForeignKey(Shop_Account, on_delete=models.CASCADE, null=False)
    order_time = models.DateTimeField(null=False, default=timezone.now)

    class Meta:
        unique_together = (('shop_name', 'order_time'),)

    def __str__(self):
        return str(self.factor_number)


class Shop_FactorLog(models.Model):
    before_action = models.CharField(max_length=300, null=True, blank=True)
    after_action = models.CharField(max_length=300, null=True, blank=True)
    time = models.DateTimeField(default=timezone.now)
    key = models.CharField(max_length=300, null=True, blank=True)


class Factor_Ingredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=False)
    factor = models.ForeignKey(Shop_Factor, on_delete=models.CASCADE, null=False)
    ingredient_name = models.CharField(max_length=20, null=False)
    price = models.IntegerField(default=0,
                                validators=[MinValueValidator(0)], null=False)
    number = models.IntegerField(validators=[MinValueValidator(0)], null=False)

    class Meta:
        unique_together = (('ingredient', 'factor'),)

    def __str__(self):
        return str(self.factor) + ' ' + str(self.ingredient)


class Factor_IngredientLog(models.Model):
    before_action = models.CharField(max_length=300, null=True, blank=True)
    after_action = models.CharField(max_length=300, null=True, blank=True)
    time = models.DateTimeField(default=timezone.now)
    key = models.CharField(max_length=300, null=True, blank=True)


class UserComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    text = models.CharField(max_length=200, null=False)

    def __str__(self):
        return str(self.user) + ' ' + str(self.text)[:10]


class UserCommentLog(models.Model):
    before_action = models.CharField(max_length=300, null=True, blank=True)
    after_action = models.CharField(max_length=300, null=True, blank=True)
    time = models.DateTimeField(default=timezone.now)
    key = models.CharField(max_length=300, null=True, blank=True)


class ManagerComment(models.Model):
    text = models.CharField(max_length=200, null=False)

    def __str__(self):
        return str(self.text)[:10]


class ManagerCommentLog(models.Model):
    before_action = models.CharField(max_length=300, null=True, blank=True)
    after_action = models.CharField(max_length=300, null=True, blank=True)
    time = models.DateTimeField(default=timezone.now)
    key = models.CharField(max_length=300, null=True, blank=True)