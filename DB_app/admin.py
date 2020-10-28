from django.contrib import admin
from DB_app.models import User, Address, Courier, Customer_Factor, Ingredient, Menu, Shop_Account, Shop_Factor, \
    Factor_Menu, Factor_Ingredient, ManagerComment, UserComment, UserLog, CourierLog, ManagerCommentLog, MenuLog,\
    IngredientLog, AddressLog, Shop_FactorLog, Customer_FactorLog, Factor_MenuLog, Factor_IngredientLog,\
    Shop_AccountLog, UserCommentLog

# Register your models here.
admin.site.register(User)
admin.site.register(Address)
admin.site.register(Courier)
admin.site.register(Customer_Factor)
admin.site.register(Ingredient)
admin.site.register(Menu)
admin.site.register(Shop_Account)
admin.site.register(Shop_Factor)
admin.site.register(Factor_Menu)
admin.site.register(Factor_Ingredient)
admin.site.register(UserComment)
admin.site.register(ManagerComment)
admin.site.register(UserLog)
admin.site.register(Customer_FactorLog)
admin.site.register(AddressLog)
admin.site.register(CourierLog)
admin.site.register(Factor_MenuLog)
admin.site.register(Factor_IngredientLog)
