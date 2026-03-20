from django.contrib import admin
from django import forms
from .models import Slot

# 1. Creating a custom form to override the default time inputs
class SlotAdminForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = '__all__'
        widgets = {
            # Use modern HTML5 time pickers instead of Django's default text box
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }

# 2. Telling the Django Admin to use this new form
@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    form = SlotAdminForm
    list_display = ('date', 'start_time', 'end_time', 'is_booked', 'customer_name')
    list_filter = ('date', 'is_booked')