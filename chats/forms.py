from django import forms


class Join_To_Group(forms.Form):
    uuid = forms.CharField(label='UUID')
