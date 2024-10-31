from django import forms

class Join_To_Group(forms.Form):
    uuid = forms.CharField(label='UUID', required=True)

class Create_Group(forms.Form):
    name = forms.CharField(label="Название группы", required=True)
