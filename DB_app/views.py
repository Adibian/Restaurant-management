from django.db.models import Count, Max, Sum, F
from django.shortcuts import render
from DB_app.forms import UserForm, AddressForUserForm, CourierForm, AddressForm, MenuForm, Shop_FactorForm, \
    Shop_AccountForm, MenuForm, UserCommentForm, ManagerCommentForm, \
    IngredientForm, Customer_FactorForm, Factor_IngredientForm, Factor_MenuForm
from DB_app.models import User, Shop_Account, Address, Courier, Customer_Factor, Shop_Factor, Menu, Ingredient, \
    Factor_Menu, Factor_Ingredient, UserComment, ManagerComment


# Create your views here.


def home(request):
    return render(request, "home.html")


def inserts_list(request):
    return render(request, "inserts/inserts_list.html")


def insert_into_user(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        address_form = AddressForUserForm(data=request.POST)
        national_id = request.POST.get('national_id')
        if not national_id[0] == '0':
            # return render(request, "home.html", {'f': national_id})
            user_form.add_error('national_id', "enter correct national_id!")
        else:
            test = False
            for i in range(len(national_id)):
                if not national_id[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    test = True
            if test:
                user_form.add_error('national_id', "enter correct national_id!")


        phone_number = request.POST.get('phone_number')
        if not phone_number[0] == '0' or not phone_number[1] == '9':
            user_form.add_error('phone_number', "enter correct phone_number!")
        else:
            test = False
            for i in range(len(phone_number)):
                if not phone_number[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    test = True
            if test:
                user_form.add_error('phone_number', "enter correct phone_number!")


        fixed_phone_number = request.POST.get('fixed_phone_number')
        if not fixed_phone_number[0] == '0':
            address_form.add_error('fixed_phone_number', "enter correct fixed_phone_number!")
        else:
            test = False
            for i in range(len(fixed_phone_number)):
                if not fixed_phone_number[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    test = True
            if test:
                address_form.add_error('fixed_phone_number', "enter correct fixed_phone_number!")
        if user_form.is_valid() and address_form.is_valid():
            user = user_form.save()
            address = address_form.save(commit=False)
            address.user = user
            # return render(request, "home.html", {'f': address})
            address.save()
            return render(request, "home.html")
    else:
        user_form = UserForm()
        address_form = AddressForUserForm()
    return render(request, "inserts/insert_user.html",
                  {'user_form': user_form, 'address_form': address_form})


def insert_into_Courier(request):
    if request.method == 'POST':
        form = CourierForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home.html")
    else:
        form = CourierForm()
    return render(request, "inserts/insert.html",
                  {'form': form})


def insert_into_address(request):
    if request.method == 'POST':
        form = AddressForm(data=request.POST)
        fixed_phone_number = request.POST.get('fixed_phone_number')
        if not fixed_phone_number[0] == '0':
            form.add_error('fixed_phone_number', "enter correct fixed_phone_number!")
        else:
            test = False
            for i in range(len(fixed_phone_number)):
                if not fixed_phone_number[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    test = True
            if test:
                form.add_error('fixed_phone_number', "enter correct fixed_phone_number!")
        if form.is_valid():
            form.save()
            return render(request, "home.html")
    else:
        form = AddressForm()
    return render(request, "inserts/insert.html",
                  {'form': form})


def insert_into_menu(request):
    if request.method == 'POST':
        form = MenuForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home.html")
    else:
        form = MenuForm()
    return render(request, "inserts/insert.html",
                  {'form': form})


def insert_into_customer_factor(request):
    if request.method == 'POST':
        form = Customer_FactorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home.html")
    else:
        form = Customer_FactorForm()
    return render(request, "inserts/insert.html",
                  {'form': form})


def insert_into_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home.html")
    else:
        form = IngredientForm()
    return render(request, "inserts/insert.html",
                  {'form': form})


def insert_into_shop_account(request):
    if request.method == 'POST':
        form = Shop_AccountForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home.html")
    else:
        form = Shop_AccountForm()
    return render(request, "inserts/insert.html",
                  {'form': form})


def insert_into_shop_factor(request):
    if request.method == 'POST':
        form = Shop_FactorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home.html")
    else:
        form = Shop_FactorForm()
    return render(request, "inserts/insert.html",
                  {'form': form})


def insert_into_factor_menu(request):
    if request.method == 'POST':
        form = Factor_MenuForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home.html")
    else:
        form = Factor_MenuForm()
    return render(request, "inserts/insert.html",
                  {'form': form})


def insert_into_factor_ingredient(request):
    if request.method == 'POST':
        form = Factor_IngredientForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home.html")
    else:
        form = Factor_IngredientForm()
    return render(request, "inserts/insert.html",
                  {'form': form})


def insert_into_user_comment(request):
    if request.method == 'POST':
        form = UserCommentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home.html")
    else:
        form = UserCommentForm()
    return render(request, "inserts/insert.html",
                  {'form': form})


def insert_into_manager_comment(request):
    if request.method == 'POST':
        form = ManagerCommentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home.html")
    else:
        form = ManagerCommentForm()
    return render(request, "inserts/insert.html",
                  {'form': form})


"""
    Deleting
"""


def deletes_list(request):
    return render(request, "deletes/deletes_list.html")


def delete_user_list(request):
    all_user = User.objects.all()
    return render(request, "deletes/delete_user.html",
                  {'all_user': all_user, 'delete': True})


def delete_user(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return render(request, "home.html")


def delete_Courier_list(request):
    all_courier = Courier.objects.all()
    return render(request, "deletes/delete_Courier.html",
                  {'all_courier': all_courier, 'delete': True})


def delete_Courier(request, pk):
    courier = Courier.objects.get(pk=pk)
    courier.delete()
    return render(request, "home.html")


def delete_address_list(request):
    all_address = Address.objects.all()
    return render(request, "deletes/delete_address.html",
                  {'all_address': all_address, 'delete': True})


def delete_address(request, pk):
    address = Address.objects.get(pk=pk)
    address.delete()
    return render(request, "home.html")


def delete_menu_list(request):
    all_menu = Menu.objects.all()
    return render(request, "deletes/delete_menu.html",
                  {'all_menu': all_menu, 'delete': True})


def delete_menu(request, pk):
    menu = Menu.objects.get(pk=pk)
    menu.delete()
    return render(request, "home.html")


def delete_customer_factor_list(request):
    all_customer_factor = Customer_Factor.objects.all()
    return render(request, "deletes/delete_customer_factor.html",
                  {'all_customer_factor': all_customer_factor, 'delete': True})


def delete_customer_factor(request, pk):
    customer_factor = Customer_Factor.objects.get(pk=pk)
    customer_factor.delete()
    return render(request, "home.html")


def delete_ingredient_list(request):
    all_ingredient = Ingredient.objects.all()
    return render(request, "deletes/delete_ingredient.html",
                  {'all_ingredient': all_ingredient, 'delete': True})


def delete_ingredient(request, pk):
    ingredient = Ingredient.objects.get(pk=pk)
    ingredient.delete()
    return render(request, "home.html")


def delete_shop_factor_list(request):
    all_shop_factor = Shop_Factor.objects.all()
    return render(request, "deletes/delete_shop_factor.html",
                  {'all_shop_factor': all_shop_factor, 'delete': True})


def delete_shop_factor(request, pk):
    shop_factor = Shop_Factor.objects.get(pk=pk)
    shop_factor.delete()
    return render(request, "home.html")


def delete_shop_account_list(request):
    all_shop_account = Shop_Account.objects.all()
    return render(request, "deletes/delete_shop_account.html",
                  {'all_shop_account': all_shop_account, 'delete': True})


def delete_shop_account(request, pk):
    shop_account = Shop_Account.objects.get(pk=pk)
    shop_account.delete()
    return render(request, "home.html")


def delete_factor_menu_list(request):
    all_factor_menu = Factor_Menu.objects.all()
    return render(request, "deletes/delete_factor_menu.html",
                  {'all_factor_menu': all_factor_menu, 'delete': True})


def delete_factor_menu(request, pk):
    factor_menu = Factor_Menu.objects.get(pk=pk)
    factor_menu.delete()
    return render(request, "home.html")


def delete_factor_ingredient_list(request):
    all_factor_ingredient = Factor_Ingredient.objects.all()
    return render(request, "deletes/delete_factor_ingredient.html",
                  {'all_factor_ingredient': all_factor_ingredient, 'delete': True})


def delete_factor_ingredient(request, pk):
    factor_ingredient = Factor_Ingredient.objects.get(pk=pk)
    factor_ingredient.delete()
    return render(request, "home.html")


"""
    Updating
"""


def updates_list(request):
    return render(request, "updates/updates_list.html")


def update_user(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        user_id = request.POST.get("national_id")
        national_id = request.POST.get('national_id')
        if not national_id[0] == '0':
            # return render(request, "home.html", {'f': national_id})
            form.add_error('national_id', "enter correct national_id!")
        else:
            test = False
            for i in range(len(national_id)):
                if not national_id[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    test = True
            if test:
                form.add_error('national_id', "enter correct national_id!")

        phone_number = request.POST.get('phone_number')
        if not phone_number[0] == '0' or not phone_number[1] == '9':
            form.add_error('phone_number', "enter correct phone_number!")
        else:
            test = False
            for i in range(len(phone_number)):
                if not phone_number[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    test = True
            if test:
                form.add_error('phone_number', "enter correct phone_number!")

        if User.objects.filter(national_id=user_id).count() == 0:
            form.add_error('national_id', "There is't such user!")
        else:
            del form.errors['national_id']
        if form.is_valid():
            user = User.objects.get(national_id=user_id)
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            form.save()
            return render(request, "home.html")
    else:
        form = UserForm()
    return render(request, "updates/update.html",
                  {'form': form})


def update_Courier(request):
    if request.method == 'POST':
        form = CourierForm(data=request.POST)
        courier_id = request.POST.get("national_id")
        if Courier.objects.filter(national_id=courier_id).count() == 0:
            form.add_error('national_id', "There is't such courier!")
        else:
            del form.errors['national_id']
        if form.is_valid():
            form.save()
            return render(request, "home.html")
    else:
        form = CourierForm()
    return render(request, "updates/update.html",
                  {'form': form})


def update_address(request):
    if request.method == 'POST':
        form = AddressForm(data=request.POST)
        address_name = request.POST.get("address_name")
        user = request.POST.get("user")
        fixed_phone_number = request.POST.get('fixed_phone_number')
        if not fixed_phone_number[0] == '0':
            form.add_error('fixed_phone_number', "enter correct fixed_phone_number!")
        else:
            test = False
            for i in range(len(fixed_phone_number)):
                if not fixed_phone_number[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    test = True
            if test:
                form.add_error('fixed_phone_number', "enter correct fixed_phone_number!")

        if Address.objects.filter(address_name=address_name, user=user).count() == 0:
            form.add_error('address_name', "There is't such address name for this user!")
        elif '__all__' in form.errors.keys():
            del form.errors['__all__']
        if form.is_valid():
            address = Address.objects.get(address_name=address_name, user=user)
            address.address_path = form.cleaned_data.get("address_path")
            address.fixed_phone_number = form.cleaned_data.get("fixed_phone_number")
            address.save()
            return render(request, "home.html")
    else:
        form = AddressForm()
    return render(request, "updates/update.html",
                  {'form': form})


def update_menu(request):
    if request.method == 'POST':
        form = MenuForm(data=request.POST)
        food_name = request.POST.get("food_name")
        if Menu.objects.filter(food_name=food_name).count() > 0:
            del form.errors['food_name']
        else:
            form.add_error('food_name', "There is't such food!")
        if form.is_valid():
            form.save()
            return render(request, "home.html")
    else:
        form = MenuForm()
    return render(request, "inserts/insert.html",
                  {'form': form})


def update_customer_factor(request):
    if request.method == 'POST':
        form = Customer_FactorForm(data=request.POST)
        factor_number = request.POST.get("id")
        if form.is_valid():
            customer_factor = Customer_Factor.objects.get(factor_number=factor_number)
            customer_factor.address = form.cleaned_data.get("address")
            customer_factor.order_time = form.cleaned_data.get("order_time")
            customer_factor.user = form.cleaned_data.get("user")
            customer_factor.courier = form.cleaned_data.get("courier")
            customer_factor.save()
            return render(request, "home.html")
    else:
        form = Customer_FactorForm()
    factor_number = Customer_Factor.objects.only('factor_number')
    return render(request, "updates/update.html",
                  {'form': form, 'ids': factor_number})


def update_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(data=request.POST)
        item_name = request.POST.get("item_name")
        shop_name = request.POST.get("shop_name")
        if Ingredient.objects.filter(item_name=item_name, shop_name=shop_name).count() == 0:
            form.add_error('item_name', "There is't such item name for this shop!")
        elif '__all__' in form.errors.keys():
            del form.errors['__all__']
        if form.is_valid():
            ingredient = Ingredient.objects.get(item_name=item_name, shop_name=shop_name)
            ingredient.price = form.cleaned_data.get("price")
            ingredient.save()
            return render(request, "home.html")
    else:
        form = IngredientForm()
    return render(request, "updates/update.html",
                  {'form': form})


def update_shop_account(request):
    if request.method == 'POST':
        form = Shop_AccountForm(data=request.POST)
        shop_name = request.POST.get("shop_name")
        if Shop_Account.objects.filter(shop_name=shop_name).count() == 0:
            form.add_error('shop_name', "There is't such shop name!")
        else:
            del form.errors['shop_name']
        if form.is_valid():
            form.save()
            return render(request, "home.html")
    else:
        form = Shop_AccountForm()
    return render(request, "inserts/insert.html",
                  {'form': form})


def update_shop_factor(request):
    if request.method == 'POST':
        form = Shop_FactorForm(data=request.POST)
        factor_number = request.POST.get('id')
        if form.is_valid():
            shop_factor = Shop_Factor.objects.get(factor_number=factor_number)
            shop_factor.shop_name = form.cleaned_data.get("shop_name")
            shop_factor.order_time = form.cleaned_data.get("order_time")
            shop_factor.save()
            return render(request, "home.html")
    else:
        form = Shop_FactorForm()
    factor_number = Shop_Factor.objects.only('factor_number')
    return render(request, "updates/update.html",
                  {'form': form, 'ids': factor_number})


def update_factor_ingredient(request):
    if request.method == 'POST':
        form = Factor_IngredientForm(data=request.POST)
        ingredient = request.POST.get("ingredient")
        factor = request.POST.get("factor")
        if Factor_Ingredient.objects.filter(ingredient=ingredient, factor=factor).count() == 0:
            form.add_error('ingredient', "There is't such ingredient name for this factor!")
        elif '__all__' in form.errors.keys():
            del form.errors['__all__']
        if form.is_valid():
            factor_ingredient = Factor_Ingredient.objects.get(ingredient=ingredient, factor=factor)
            factor_ingredient.price = form.cleaned_data.get("price")
            factor_ingredient.number = form.cleaned_data.get("number")
            factor_ingredient.save()
            return render(request, "home.html")
    else:
        form = Factor_IngredientForm()
    return render(request, "updates/update.html",
                  {'form': form})


def update_factor_menu(request):
    if request.method == 'POST':
        form = Factor_MenuForm(data=request.POST)
        food_name = request.POST.get("food_name")
        factor = request.POST.get("factor")
        if Factor_Menu.objects.filter(food_name=food_name, factor=factor).count() == 0:
            form.add_error('food_name', "There is't such food_name name for this factor!")
        elif '__all__' in form.errors.keys():
            del form.errors['__all__']
        if form.is_valid():
            factor_menu = Factor_Menu.objects.get(food_name=food_name, factor=factor)
            factor_menu.price = form.cleaned_data.get("price")
            factor_menu.number = form.cleaned_data.get("number")
            factor_menu.save()
            return render(request, "home.html")
    else:
        form = Factor_MenuForm()
    return render(request, "updates/update.html",
                  {'form': form})


"""
    Some requirements 
"""


def requirements_list(request):
    return render(request, "requirements/requirements_list.html")


def order_food(request):
    if request.method == 'POST':
        form = Customer_FactorForm(data=request.POST)
        if form.is_valid():
            foods = request.POST.getlist('food')
            if foods:
                user = form.cleaned_data.get("user")
                address_path = form.cleaned_data.get("address")
                if user and not address_path:
                    user = User.objects.get(national_id=user)
                    address = Address.objects.get(user=user)
                    address_path = address.address_path
                factor = form.save(commit=False)
                factor.address = address_path
                factor.save()
                for food in foods:
                    menu_item = Menu.objects.get(food_name=food)
                    number = request.POST.get(food)
                    factor_menu = Factor_Menu(factor=factor, food=menu_item, food_name=menu_item.food_name,
                                              price=menu_item.price, number=number)
                    factor_menu.save()
                return render(request, "home.html")
    else:
        form = Customer_FactorForm()
    foods = Menu.objects.all()
    users = User.objects.all()
    return render(request, "requirements/order_food.html",
                  {'form': form, 'foods': foods, 'users': users})


def order_ingredient(request):
    if request.method == 'POST':
        form = Shop_FactorForm(data=request.POST)
        if form.is_valid():
            shop_name = form.cleaned_data.get("shop_name")
            shop_account = Shop_Account.objects.get(shop_name=shop_name)
            if not shop_account.active:
                form.add_error('shop_name', "This shop is not active!")
            ingredients = request.POST.getlist('ingredient')
            if ingredients and shop_account.active:
                factor = form.save(commit=False)
                test = True
                for ingredient in ingredients:
                    if Ingredient.objects.filter(item_name=ingredient, shop_name=factor.shop_name).count() == 0:
                        test = False
                if test:
                    factor.save()
                    for ingredient in ingredients:
                        ingredient_item = Ingredient.objects.get(item_name=ingredient, shop_name=factor.shop_name)
                        number = request.POST.get(ingredient)
                        factor_ingredient = Factor_Ingredient(factor=factor, ingredient=ingredient_item,
                                                              ingredient_name=ingredient,
                                                              price=ingredient_item.price, number=number)
                        factor_ingredient.save()
                    return render(request, "home.html")
    else:
        form = Shop_FactorForm()
    ingredients = Ingredient.objects.all()
    active_shops = Shop_Account.objects.filter(active=True).all()
    return render(request, "requirements/order_ingredient.html",
                  {'form': form, 'ingredients': ingredients, 'active_shops': active_shops})


def show_user_list(request):
    all_user = User.objects.all()
    return render(request, "deletes/delete_user.html",
                  {'all_user': all_user, 'show': True})


def show_user_orders(request, pk):
    user = User.objects.get(pk=pk)
    factor = Customer_Factor.objects.filter(user=user)
    factor_menu = Factor_Menu.objects.filter(factor__in=factor)
    factor_menu = factor_menu.annotate(all_price=F('number') * F('price'))[:]
    factor_menu = factor_menu.values('food_name').annotate(sum_number=Sum('number'),
                                                           sum_peice=Sum('all_price')).order_by('-sum_number')[:]
    return render(request, "requirements/show_user_orders.html", {'factor_menu': factor_menu})


def show_restaurant_orders(request):
    factor_ingredient = Factor_Ingredient.objects.all()
    factor_ingredient = factor_ingredient.annotate(all_price=F('number') * F('price'))[:]
    factor_ingredient = factor_ingredient.values('ingredient_name').annotate(sum_number=Sum('number'),
                                                                             sum_peice=Sum('all_price')).order_by(
        '-sum_number')[:]
    return render(request, "requirements/show_restaurant_orders.html", {'factor_ingredient': factor_ingredient})


def show_cost_benefit(request):
    factor_menu = Factor_Menu.objects.all()
    factor_menu = factor_menu.annotate(all_price=F('number') * F('price'))[:]
    sum_benefit = factor_menu.aggregate(Sum('all_price'))

    factor_ingredient = Factor_Ingredient.objects.all()
    factor_ingredient = factor_ingredient.annotate(all_price=F('number') * F('price'))[:]
    sum_cost = factor_ingredient.aggregate(Sum('all_price'))

    return render(request, "requirements/show_cost_benefit.html", {'sum_benefit': sum_benefit, 'sum_cost': sum_cost})


def show_user_comments(request):
    user_comment = UserComment.objects.all()
    return render(request, "requirements/show_user_comments.html", {'user_comment': user_comment})


def show_manager_comments(request):
    manager_comment = ManagerComment.objects.all()
    return render(request, "requirements/show_manager_comments.html", {'manager_comment': manager_comment})
