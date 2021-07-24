from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
  list_display = ('name','email', 'phone', 'contact_date')
  list_display_links = ('name','phone', 'email')
  search_fields = ('name','email', 'phone')
  list_per_page = 25

class PickupAdmin(admin.ModelAdmin):
  list_display = ( 'uuid','sendername', 'recivername','senderemail','reciveremail','parcel','senderphone','reciverphone', 'request_date')
  list_display_links = ('uuid','sendername', 'recivername')
  search_fields = ('uuid','senderemail', 'reciveremail')
  list_per_page = 25

class RiderAssignmentAdmin(admin.ModelAdmin):
  list_display = ('rider_name','public_tracking_id','date_and_time_of_assignment')
  list_display_links = ('rider_name','public_tracking_id')
  search_fields = ('rider_name','public_tracking_id')
  list_per_page = 25

class RiderRecordAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image_of_rider.url))

    thumbnail.short_description = 'Rider Image'
    list_display = ('id','thumbnail','fullname', 'gender', 'residential_address')
    list_display_links = ('id', 'thumbnail', 'fullname')
    search_fields = ('id', 'fullname', 'gender')
    list_per_page = 25


admin.site.register(RiderAssignment, RiderAssignmentAdmin)
admin.site.register(RiderRecord, RiderRecordAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Pickup, PickupAdmin)