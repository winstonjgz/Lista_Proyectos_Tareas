from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label='Titulo', max_length=50, widget=forms.TextInput(attrs={'class': 'input'}) )
    description = forms.CharField(label='Descripcion de la tarea', widget=forms.Textarea(attrs={'class': 'input'}))


class CreateNewProject(forms.Form):
    name = forms.CharField(label='Titulo Proyecto', max_length=50, widget=forms.TextInput(attrs={'class': 'input'}) )
    