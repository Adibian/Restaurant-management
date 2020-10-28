from django.utils import timezone

from DB_app.models import User, UserLog, UserComment, ManagerComment, Shop_Account, Factor_Ingredient, Factor_Menu, \
    Customer_Factor, Shop_Factor, Address, Ingredient, Menu, Courier, AddressLog, CourierLog, Customer_FactorLog, \
    Factor_IngredientLog, Factor_MenuLog, IngredientLog, ManagerCommentLog, MenuLog, Shop_AccountLog, Shop_FactorLog, \
    UserCommentLog
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from datetime import datetime, timedelta

from celery import shared_task

@shared_task
def delete_model(model_pk):
    try:
        UserLog.objects.get(pk=model_pk).delete()
    except User.DoesNotExist:
        pass


@receiver(pre_save, sender=User)
def user_trigger_insert_update(sender, instance, **kwargs):
    before_action = ''
    if User.objects.filter(pk=instance.pk).count() > 0:
        pre_instance = User.objects.get(pk=instance.pk)
        before_action = '{national_id:' + pre_instance.national_id + ', first_name:' + pre_instance.first_name + \
                    ', last_name:' + pre_instance.last_name + ', last_name:' + pre_instance.phone_number + \
                    ' ,date_of_birth:' + str(pre_instance.date_of_birth) + '}'

    after_action = '{national_id:' + instance.national_id + ', first_name:' + instance.first_name + ', last_name:' + \
                   instance.last_name + ', last_name:' + instance.phone_number + ' ,date_of_birth:' + \
                   str(instance.date_of_birth) + '}'
    user_log = UserLog(after_action=after_action, before_action=before_action, user=instance.national_id)
    user_log.save()
    last = UserLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(minutes=20):
        last.delete()

    # delete_model.apply_async(
    #     args=(user_log.pk,),
    #     eta=datetime.utcnow() + timedelta(hours=24)
    # )


@receiver(pre_delete, sender=User)
def user_trigger_delete(sender, instance, **kwargs):
    pre_instance = User.objects.get(pk=instance.pk)
    before_action = '{national_id:' + pre_instance.national_id + ', first_name:' + pre_instance.first_name + \
                    ', last_name:' + pre_instance.last_name + ', last_name:' + pre_instance.phone_number + \
                    ' ,date_of_birth:' + str(pre_instance.date_of_birth) + '}'

    after_action = ''
    user_log = UserLog(after_action=after_action, before_action=before_action, user=None)
    user_log.save()
    last = UserLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(seconds=20):
        last.delete()


@receiver(pre_save, sender=UserComment)
def user_comment_trigger_insert_update(sender, instance, **kwargs):
    before_action = ''
    if UserComment.objects.filter(pk=instance.pk).count() > 0:
        pre_instance = UserComment.objects.get(pk=instance.pk)
        before_action = '{user:' + str(pre_instance.user) + ', text:' + pre_instance.text + '}'

    after_action = '{user:' + str(instance.user) + ', text:' + instance.text + '}'
    try:
        key = str(UserComment.objects.last().pk + 1)
    except:
        key = 1
    user_log = UserCommentLog(after_action=after_action, before_action=before_action, key=key)
    user_log.save()
    last = UserCommentLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(seconds=20):
        last.delete()



@receiver(pre_delete, sender=UserComment)
def user_comment_trigger_delete(sender, instance, **kwargs):
    pre_instance = UserComment.objects.get(pk=instance.pk)
    before_action = '{user:' + pre_instance.user + ', text:' + pre_instance.text + '}'

    after_action = ''
    user_log = UserCommentLog(after_action=after_action, before_action=before_action, key=None)
    user_log.save()
    last = UserCommentLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(seconds=20):
        last.delete()

@receiver(pre_save, sender=ManagerComment)
def manager_comment_trigger_insert_update(sender, instance, **kwargs):
    before_action = ''
    if ManagerComment.objects.filter(pk=instance.pk).count() > 0:
        pre_instance = ManagerComment.objects.get(pk=instance.pk)
        before_action = '{text:' + pre_instance.text + '}'

    after_action = '{text:' + instance.text + '}'
    try:
        key = str(ManagerComment.objects.last().pk + 1)
    except:
        key = 1
    manager_comment_log = ManagerCommentLog(after_action=after_action, before_action=before_action, key=key)
    manager_comment_log.save()
    last = ManagerCommentLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(seconds=20):
        last.delete()


@receiver(pre_delete, sender=ManagerComment)
def manager_comment_trigger_delete(sender, instance, **kwargs):
    pre_instance = ManagerComment.objects.get(pk=instance.pk)
    before_action = '{text:' + pre_instance.text + '}'

    after_action = ''
    log = ManagerCommentLog(after_action=after_action, before_action=before_action, key=None)
    log.save()
    last = ManagerCommentLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(seconds=20):
        last.delete()


@receiver(pre_save, sender=Shop_Account)
def shop_account_trigger_insert_update(sender, instance, **kwargs):
    before_action = ''
    if Shop_Account.objects.filter(pk=instance.pk).count() > 0:
        pre_instance = Shop_Account.objects.get(pk=instance.pk)
        before_action = '{shop_name:' + str(pre_instance.shop_name) + ', active:' + str(
        pre_instance.active) + '}'

    after_action = '{shop_name:' + str(instance.shop_name) + ', active:' + str(
        instance.active) + '}'
    log = Shop_AccountLog(after_action=after_action, before_action=before_action, key=instance.shop_name)
    log.save()
    last = Shop_AccountLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(seconds=20):
        last.delete()


@receiver(pre_delete, sender=Shop_Account)
def shop_account_trigger_delete(sender, instance, **kwargs):
    pre_instance = Shop_Account.objects.get(pk=instance.pk)
    before_action = '{shop_name:' + str(pre_instance.shop_name) + ', active:' + str(
        pre_instance.active) + '}'

    after_action = ''
    log = Shop_AccountLog(after_action=after_action, before_action=before_action, key=None)
    log.save()
    last = Shop_AccountLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(seconds=20):
        last.delete()


@receiver(pre_save, sender=Factor_Ingredient)
def factor_ingredient_trigger_insert_update(sender, instance, **kwargs):
    before_action = ''
    if Factor_Ingredient.objects.filter(pk=instance.pk).count() > 0:
        pre_instance = Factor_Ingredient.objects.get(pk=instance.pk)
        before_action = '{ingredient:' + str(pre_instance.ingredient) + ', factor:' + str(
        pre_instance.factor) + ', ingredient_name:' + str(pre_instance.ingredient_name) + ', price:' + str(
        pre_instance.price) + '}'

    after_action = '{ingredient:' + str(instance.ingredient) + ', factor:' + str(
        instance.factor) + ', ingredient_name:' + str(instance.ingredient_name) + ', price:' + str(
        instance.price) + ', number:' + str(instance.number) + '}'
    try:
        key = str(Factor_Ingredient.objects.last().pk + 1)
    except:
        key = 1
    log = Factor_IngredientLog(after_action=after_action, before_action=before_action, key=key)
    log.save()
    last = Factor_IngredientLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(seconds=20):
        last.delete()


@receiver(pre_delete, sender=Factor_Ingredient)
def factor_ingredient_trigger_delete(sender, instance, **kwargs):
    pre_instance = Factor_Ingredient.objects.get(pk=instance.pk)
    before_action = '{ingredient:' + str(pre_instance.ingredient) + ', factor:' + str(
        pre_instance.factor) + ', ingredient_name:' + str(pre_instance.ingredient_name) + ', price:' + str(
        pre_instance.price) + '}'

    after_action = ''
    log = Factor_IngredientLog(after_action=after_action, before_action=before_action, key=None)
    log.save()
    last = Factor_IngredientLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(seconds=20):
        last.delete()


@receiver(pre_save, sender=Factor_Menu)
def Factor_Menu_trigger_insert_update(sender, instance, **kwargs):
    before_action = ''
    if Factor_Menu.objects.filter(pk=instance.pk).count() > 0:
        pre_instance = Factor_Menu.objects.get(pk=instance.pk)
        before_action = '{factor:' + str(pre_instance.factor) + ', food:' + str(
        pre_instance.food) + ', food_name:' + str(pre_instance.food_name) + ', price:' + str(
        pre_instance.price) + ', number:' + str(pre_instance.number) + '}'

    after_action = '{factor:' + str(instance.factor) + ', food:' + str(
        instance.food) + ', food_name:' + str(instance.food_name) + ', price:' + str(
        instance.price) + ', number:' + str(instance.number) + '}'
    try:
        key = str(Factor_Menu.objects.last().pk + 1)
    except:
        key = 1
    log = Factor_MenuLog(after_action=after_action, before_action=before_action, key=key)
    log.save()
    last = Factor_MenuLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(seconds=20):
        last.delete()


@receiver(pre_delete, sender=Factor_Menu)
def Factor_Menu_trigger_delete(sender, instance, **kwargs):
    pre_instance = Factor_Menu.objects.get(pk=instance.pk)
    before_action = '{factor:' + str(pre_instance.factor) + ', food:' + str(
        pre_instance.food) + ', food_name:' + str(pre_instance.food_name) + ', price:' + str(
        pre_instance.price) + ', number:' + str(pre_instance.number) + '}'

    after_action = ''
    log = Factor_MenuLog(after_action=after_action, before_action=before_action, key=None)
    log.save()
    last = Factor_MenuLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(seconds=20):
        last.delete()


@receiver(pre_save, sender=Customer_Factor)
def Customer_Factor_trigger_insert_update(sender, instance, **kwargs):
    before_action = ''
    if Customer_Factor.objects.filter(pk=instance.pk).count() > 0:
        pre_instance = Customer_Factor.objects.get(pk=instance.pk)
        before_action = '{factor_number:' + str(pre_instance.factor_number) + ', address:' + str(
        pre_instance.address) + ', order_time:' + str(pre_instance.order_time) + ', user:' + str(
        pre_instance.user) + ', courier:' + str(pre_instance.courier) + '}'

    after_action = '{factor_number:' + str(instance.factor_number) + ', address:' + str(
        instance.address) + ', order_time:' + str(instance.order_time) + ', user:' + str(
        instance.user) + ', courier:' + str(instance.courier) + '}'
    try:
        key = str(Customer_Factor.objects.last().pk + 1)
    except:
        key = 1
    log = Customer_FactorLog(after_action=after_action, before_action=before_action, key=key)
    log.save()
    last = Customer_FactorLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(seconds=20):
        last.delete()


@receiver(pre_delete, sender=Customer_Factor)
def Customer_Factor_trigger_delete(sender, instance, **kwargs):
    pre_instance = Customer_Factor.objects.get(pk=instance.pk)
    before_action = '{factor_number:' + str(pre_instance.factor_number) + ', address:' + str(
        pre_instance.address) + ', order_time:' + str(pre_instance.order_time) + ', user:' + str(
        pre_instance.user) + ', courier:' + str(pre_instance.courier) + '}'

    after_action = ''
    log = Customer_Factor(after_action=after_action, before_action=before_action, key=None)
    log.save()
    last = Customer_FactorLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(seconds=20):
        last.delete()


@receiver(pre_save, sender=Shop_Factor)
def Shop_Factor_trigger_insert_update(sender, instance, **kwargs):
    before_action = ''
    if Shop_Factor.objects.filter(pk=instance.pk).count() > 0:
        pre_instance = Shop_Factor.objects.get(pk=instance.pk)
        before_action = '{factor_number:' + str(pre_instance.factor_number) + ', shop_name:' + str(
            pre_instance.shop_name) + ', order_time:' + str(pre_instance.order_time) + '}'

    after_action = '{factor_number:' + str(instance.factor_number) + ', shop_name:' + str(
        instance.shop_name) + ', order_time:' + str(instance.order_time) + '}'
    try:
        key = str(Shop_Factor.objects.last().pk + 1)
    except:
        key = 1
    log = Shop_FactorLog(after_action=after_action, before_action=before_action, key=key)
    log.save()
    last = Shop_FactorLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(seconds=20):
        last.delete()


@receiver(pre_delete, sender=Shop_Factor)
def Shop_Factor_trigger_delete(sender, instance, **kwargs):
    pre_instance = Shop_Factor.objects.get(pk=instance.pk)
    before_action = '{factor_number:' + str(pre_instance.factor_number) + ', shop_name:' + str(
        pre_instance.shop_name) + ', order_time:' + str(pre_instance.order_time) + '}'

    after_action = ''
    log = Shop_Factor(after_action=after_action, before_action=before_action, key=None)
    log.save()
    last = Shop_FactorLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(seconds=20):
        last.delete()


@receiver(pre_save, sender=Address)
def Address_trigger_insert_update(sender, instance, **kwargs):
    before_action = ''
    if Address.objects.filter(pk=instance.pk).count() > 0:
        pre_instance = Address.objects.get(pk=instance.pk)
        before_action = '{address_name:' + pre_instance.address_name + ', address_path:' + str(
            pre_instance.address_path) + ', fixed_phone_number:' + str(
            pre_instance.fixed_phone_number) + ', user:' + str(
            pre_instance.user) + '}'

    after_action = '{address_name:' + instance.address_name + ', address_path:' + str(
        instance.address_path) + ', fixed_phone_number:' + str(instance.fixed_phone_number) + ', user:' + str(
        instance.user) + '}'
    try:
        key = str(Address.objects.last().pk + 1)
    except:
        key = 1
    log = AddressLog(after_action=after_action, before_action=before_action, key=key)
    log.save()
    last = AddressLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(seconds=20):
        last.delete()


@receiver(pre_delete, sender=Address)
def Address_trigger_delete(sender, instance, **kwargs):
    pre_instance = Address.objects.get(pk=instance.pk)
    before_action = '{address_name:' + pre_instance.address_name + ', address_path:' + str(
        pre_instance.address_path) + ', fixed_phone_number:' + str(pre_instance.fixed_phone_number) + ', user:' + str(
        pre_instance.user) + '}'

    after_action = ''
    log = AddressLog(after_action=after_action, before_action=before_action, key=None)
    log.save()
    last = AddressLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(seconds=20):
        last.delete()


@receiver(pre_save, sender=Ingredient)
def Ingredient_trigger_insert_update(sender, instance, **kwargs):
    before_action = ''
    if Ingredient.objects.filter(pk=instance.pk).count() > 0:
        pre_instance = Ingredient.objects.get(pk=instance.pk)
        before_action = '{item_name:' + pre_instance.item_name + ', shop_name:' + str(
            pre_instance.shop_name) + ', price:' + str(pre_instance.price) + '}'

    after_action = '{item_name:' + instance.item_name + ', shop_name:' + str(instance.shop_name) + ', price:' + str(
        instance.price) + '}'
    try:
        key = str(Ingredient.objects.last().pk + 1)
    except:
        key = 1
    log = IngredientLog(after_action=after_action, before_action=before_action, key=key)
    log.save()
    last = IngredientLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(seconds=20):
        last.delete()


@receiver(pre_delete, sender=Ingredient)
def Ingredient_trigger_delete(sender, instance, **kwargs):
    pre_instance = Ingredient.objects.get(pk=instance.pk)
    before_action = '{item_name:' + pre_instance.item_name + ', shop_name:' + str(
        pre_instance.shop_name) + ', price:' + str(pre_instance.price) + '}'

    after_action = ''
    log = IngredientLog(after_action=after_action, before_action=before_action, key=None)
    log.save()
    last = IngredientLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(seconds=20):
        last.delete()


@receiver(pre_save, sender=Menu)
def Menu_trigger_insert_update(sender, instance, **kwargs):
    before_action = ''
    if Menu.objects.filter(pk=instance.pk).count() > 0:
        pre_instance = Menu.objects.get(pk=instance.pk)
        before_action = '{food_name:' + pre_instance.food_name + ', price:' + pre_instance.price + '}'

    after_action = '{food_name:' + instance.food_name + ', price:' + str(instance.price) + '}'
    log = MenuLog(after_action=after_action, before_action=before_action, key=instance.food_name)
    log.save()
    last = MenuLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(seconds=20):
        last.delete()


@receiver(pre_delete, sender=Menu)
def Menu_trigger_delete(sender, instance, **kwargs):
    pre_instance = Menu.objects.get(pk=instance.pk)
    before_action = '{food_name:' + pre_instance.food_name + ', price:' + str(pre_instance.price) + '}'

    after_action = ''
    log = MenuLog(after_action=after_action, before_action=before_action, key=None)
    log.save()
    last = MenuLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(seconds=20):
        last.delete()


@receiver(pre_save, sender=Courier)
def Courier_trigger_insert_update(sender, instance, **kwargs):
    before_action = ''
    if Courier.objects.filter(pk=instance.pk).count() > 0:
        pre_instance = Courier.objects.get(pk=instance.pk)
        before_action = '{national_id:' + pre_instance.national_id + ', first_name:' + pre_instance.first_name + ', last_name:' + \
                        pre_instance.last_name + ', last_name:' + pre_instance.phone_number + '}'

    after_action = '{national_id:' + instance.national_id + ', first_name:' + instance.first_name + ', last_name:' + \
                   instance.last_name + ', last_name:' + instance.phone_number + '}'
    log = CourierLog(after_action=after_action, before_action=before_action, key=instance.national_id)
    log.save()
    last = CourierLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(minutes=20):
        last.delete()


@receiver(pre_delete, sender=Courier)
def Courier_trigger_delete(sender, instance, **kwargs):
    pre_instance = Courier.objects.get(pk=instance.pk)
    before_action = '{national_id:' + pre_instance.national_id + ', first_name:' + pre_instance.first_name + ', last_name:' + \
                    pre_instance.last_name + ', last_name:' + pre_instance.phone_number + '}'

    after_action = ''
    log = CourierLog(after_action=after_action, before_action=before_action, key=None)
    log.save()
    last = CourierLog.objects.order_by('time').first()
    if last.time < timezone.now() - timedelta(seconds=20):
        last.delete()