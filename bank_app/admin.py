from django.contrib import admin
from .models import *

admin.site.register(Role)
admin.site.register(User)
admin.site.register(Account)
admin.site.register(Card)
admin.site.register(Credit)
admin.site.register(Logs)
admin.site.register(Transactions)
admin.site.register(UserHistory)