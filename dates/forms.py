from django import forms


class DatesForm(forms.Form):
    description = forms.CharField()
    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "placeholder": "mm/dd/yyyy"
            }
        ))
    inflation = forms.FloatField()

    description.widget.attrs['placeholder'] = 'Year Description'
    inflation.widget.attrs['placeholder'] = 'Inflation Value'
