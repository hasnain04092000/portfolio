from django.contrib import admin
from .models import Services,ServicesTop, Project, Contact, Profile,Banner

# Register your models here.

admin.site.register(Services)
admin.site.register(Project)
admin.site.register(Contact)


class SingleObject(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True


admin.site.register(Profile, SingleObject)
admin.site.register(ServicesTop, SingleObject)
admin.site.register(Banner, SingleObject)
