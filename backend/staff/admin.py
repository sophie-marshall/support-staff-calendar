from django.contrib import admin
from .models import StaffAvailability, StaffMember
from django import forms

class StaffAvailabilityForm(forms.ModelForm):
    class Meta:
        model = StaffAvailability
        fields = '__all__'
        
    sunday = forms.MultipleChoiceField(
        choices=StaffAvailability.SUNDAY_CLASSES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    monday = forms.MultipleChoiceField(
        choices=StaffAvailability.MONDAY_CLASSES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    tuesday = forms.MultipleChoiceField(
        choices=StaffAvailability.TUESDAY_CLASSES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    wednesday = forms.MultipleChoiceField(
        choices=StaffAvailability.WEDNESDAY_CLASSES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    thursday = forms.MultipleChoiceField(
        choices=StaffAvailability.THURSDAY_CLASSES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    friday = forms.MultipleChoiceField(
        choices=StaffAvailability.FRIDAY_CLASSES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    saturday = forms.MultipleChoiceField(
        choices=StaffAvailability.SATURDAY_CLASSES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

class StaffAvailabilityAdmin(admin.ModelAdmin):
    form = StaffAvailabilityForm

admin.site.register(StaffAvailability, StaffAvailabilityAdmin)
admin.site.register(StaffMember)