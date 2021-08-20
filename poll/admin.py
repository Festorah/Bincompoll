from django.contrib import admin
from .models import PollingUnit, AnnouncedLgaResults, Lga, AnnouncedPollingUnitResult, State, Party, AnnouncedStateResult, AnnouncedWardResult


admin.site.site_header = 'Bincom Poll'


class AnnouncedPollingUnitResultAdmin(admin.ModelAdmin):
	#Better dashboard view
	list_display = ('result_id', 'polling_unit_uniqueid', 'party_abbreviation', 'party_score')
	list_filter = ('polling_unit_uniqueid', 'party_abbreviation')


admin.site.register(AnnouncedPollingUnitResult, AnnouncedPollingUnitResultAdmin)


class PollingUnitAdmin(admin.ModelAdmin):
	list_display = ('unique_id', 'lga_id', 'unique_ward_id', 'polling_unit_name', 'polling_unit_description')
	list_filter =  ('unique_ward_id', 'polling_unit_name')


admin.site.register(PollingUnit, PollingUnitAdmin)

admin.site.register(AnnouncedLgaResults)
admin.site.register(Lga)
admin.site.register(State)
admin.site.register(Party)
admin.site.register(AnnouncedStateResult)
admin.site.register(AnnouncedWardResult)










