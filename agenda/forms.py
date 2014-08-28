# -*- coding: utf8 -*-

from django import forms
from agenda.models import schedule_item


class form_schedule_item(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(format="%d/%m/%Y"),
        input_formats=(["%d/%m/%y", "%d/%m/%Y"])
    )

    class Meta:
        model = schedule_item
        fields = ("subject", "date", "time", "description", "participants")
