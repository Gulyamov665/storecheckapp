from django.contrib import admin

# Register your models here.
from store.models import Details, Trade, Sku, United, Visit, Territory


class VisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'trade', 'visit_date', 'user', )


admin.site.register(Visit, VisitAdmin)
admin.site.register(Trade)
admin.site.register(Sku)
admin.site.register(Territory)
admin.site.register(Details)
admin.site.register(United)
