from django.contrib import admin


from .models import HomeInfo, Person, GeeksModel

admin.site.register(HomeInfo)

admin.site.register(Person)
admin.site.register(GeeksModel)


