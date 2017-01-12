from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from nested_inline.admin import NestedTabularInline, NestedModelAdmin
from .models import *
from .emails import *

# Register your models here.
admin.site.register(HoldType)
admin.site.register(ShirtSizes)
admin.site.register(Event)
admin.site.register(Jersey)
admin.site.register(StaffJersey)
admin.site.register(TableSize)


def send_approval_email(modeladmin, request, queryset):
    sendApprovalEmail(queryset)
    queryset.update(emailed=True)
send_approval_email.short_description = "Send approval email and payment instructions"

class DealerResource(resources.ModelResource):
    class Meta:
        model = Dealer

class DealerAdmin(ImportExportModelAdmin):
    list_display = ('attendee', 'businessName', 'tableSize', 'chairs', 'tables', 'needWifi', 'approved', 'tableNumber', 'emailed', 'paidTotal')
    save_on_top = True
    resource_class = DealerResource
    actions = [send_approval_email]
    fieldsets = (
        (
	    None, 
            {'fields':(
                ('attendee', 'approved'), 
                'registrationToken', 'tableNumber',
                ('discount','discountReason'), 'notes'
            )}
        ),
        (
            'Business Info', 
            {'fields': (
                'businessName', 'license', 'website', 'description', 'partners'
            )}
        ),
        (
            'Table Request', 
            {'fields':(
                'tableSize', 
                ('willSwitch', 'needPower', 'needWifi', 'wallSpace', 'reception', 'breakfast'),
                ('nearTo', 'farFrom'),
                ('tables', 'chairs'), 'partners'
            )}
        ),
        (
            'Contributions', 
            {'fields':(
                'buttonOffer', 'charityRaffle'
            )}
        )
    )

admin.site.register(Dealer, DealerAdmin)

def send_staff_registration_email(modeladmin, request, queryset):
    for staff in queryset:
        sendStaffPromotionEmail(staff)
send_staff_registration_email.short_description = "Send registration instructions"

class StaffAdmin(admin.ModelAdmin):
    save_on_top = True
    actions = [send_staff_registration_email]
    list_display = ('attendee', 'title', 'department', 'shirtsize', 'staff_total')
    fieldsets = (
        (
	    None, 
            {'fields':(
                ('attendee', 'registrationToken'), 
                ('title', 'timesheetAccess'),
                ('department', 'supervisor'),
                ('twitter','telegram'),
                'shirtsize', 
            )}
        ),
        (
            'Emergency Contact', 
            {'fields': (
                'contactName', 'contactPhone', 'contactRelation'
            )}
        ),
        (
            'Misc', 
            {'fields': (
                'specialSkills', 'specialFood', 'specialMedical',
                'notes'
            )}
        ),
    )

    def staff_total(self, obj):
        return obj.attendee.paidTotal()

admin.site.register(Staff, StaffAdmin)


########################################################
#   Attendee Admin

def make_staff(modeladmin, request, queryset):
    for att in queryset:
        staff = Staff(attendee=att)
        staff.save()
make_staff.short_description = "Add to Staff"

def clear_abandons(modeladmin, request, queryset):
    for att in queryset:
        if att.abandoned() == True:
           jerseyTypes = PriceLevelOption.objects.filter(optionExtraType='Jersey')
           jerseyOptions = AttendeeOptions.objects.filter(option__in=jerseyTypes)
           for jerOpt in jerseyOptions:
             jersey = Jersey.objects.get(id=jerOpt.optionValue)
             jersey.delete()
           att.delete()
clear_abandons.short_description = "***Delete Abandoned Orders***"

class AttendeeOptionInline(NestedTabularInline):
    model=AttendeeOptions
    extra=1

class OrderItemInline(NestedTabularInline):
    model=OrderItem
    extra=0
    inlines = [AttendeeOptionInline]



class AttendeeAdmin(NestedModelAdmin):
    inlines = [OrderItemInline]
    save_on_top = True
    actions = [make_staff, clear_abandons]
    list_display = ('firstName', 'lastName', 'badgeName', 'email', 'paidTotal', 'effectiveLevel', 'abandoned', 'registeredDate')
    fieldsets = (
        (
	    None, 
            {'fields':(
                ('firstName', 'lastName'), 
                ('registrationToken', 'event'), 
                ('badgeName', 'badgeNumber'),
                ('address1', 'address2'),
                ('city', 'state', 'postalCode', 'country'),
                ('email','phone', 'emailsOk'),
                'birthdate', 
            )}
        ),
        (
            'Other Con Info', 
            {'fields': (
                'volunteerDepts', 'holdType', 'notes'
            )}
        ),
        (
            'Parent Info', 
            {'fields': (
                'parentFirstName', 'parentLastName', 
                'parentPhone', 'parentEmail',
            )}
        ),
    )


admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(AttendeeOptions)
admin.site.register(OrderItem)
admin.site.register(Order)

class PriceLevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'basePrice', 'startDate', 'endDate', 'public', 'group')

admin.site.register(PriceLevel, PriceLevelAdmin)

class PriceLevelOptionAdmin(admin.ModelAdmin):
    list_display = ('optionName', 'priceLevel', 'optionPrice', 'optionExtraType', 'required')

admin.site.register(PriceLevelOption, PriceLevelOptionAdmin)

class DiscountAdmin(admin.ModelAdmin):
    list_display = ('codeName', 'amountOff', 'percentOff', 'oneTime', 'used')
    save_on_top = True

admin.site.register(Discount, DiscountAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'volunteerListOk')

admin.site.register(Department, DepartmentAdmin)
