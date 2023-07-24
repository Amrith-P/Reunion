from django.contrib import admin
from class_room.models import *
@admin.register(Bench11)
class Bench11ModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bench11._meta.fields]

@admin.register(Bench12)
class Bench12ModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bench12._meta.fields]    

@admin.register(Bench13)
class Bench13ModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bench13._meta.fields]

@admin.register(Bench14)
class Bench14ModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bench14._meta.fields]

@admin.register(Bench15)
class Bench15ModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bench15._meta.fields]

@admin.register(Bench21)
class Bench21ModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bench21._meta.fields]

@admin.register(Bench22)
class Bench22ModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bench22._meta.fields]

@admin.register(Bench23)
class Bench11ModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bench23._meta.fields]

@admin.register(Bench24)
class Bench24ModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bench24._meta.fields]

@admin.register(Bench25)
class Bench25ModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bench25._meta.fields]

@admin.register(Bench26)
class Bench26ModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bench26._meta.fields]    
