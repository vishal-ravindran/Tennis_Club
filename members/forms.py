from django import forms
from datetime import datetime
from members.models import Member

class SimpleForm(forms.Form):
    firstName = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastName = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField( widget=forms.DateInput(attrs={'class': 'form-control'}))
    # date_text = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'date_text'}))


    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone.isdigit()!= True:
            raise forms.ValidationError("Invalid phone number format")
        return phone
   
    def clean_date(self):
        date = self.cleaned_data['date']
        if not isinstance(date, str):  # Check if it's not already a string
            date = date.strftime('%Y-%m-%d')  # Convert datetime.date to string
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise forms.ValidationError("Invalid date format. Use YYYY-MM-DD.")
        return date


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstName', 'lastName', 'phone', 'join_date']  # Include the fields you want to edit
