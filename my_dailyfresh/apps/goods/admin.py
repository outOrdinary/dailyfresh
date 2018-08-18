from django.contrib import admin
from apps.goods.models import Goods,GoodsType

# Register your models here.

admin.site.register(Goods)
admin.site.register(GoodsType)
