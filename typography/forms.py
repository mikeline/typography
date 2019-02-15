from django import forms


type_choice = [('book', 'Книга'), ('magazine', 'Журнал'), ('document', 'Документ'), ('banner', 'Баннер'), ('poster', 'Плакат')]


class Prod(forms.Form):
    name = forms.CharField(label="Название", max_length=200, widget=forms.TextInput(attrs={"class": "myfield"}))
    type = forms.MultipleChoiceField(choices=type_choice, label="Тип", widget=forms.CheckboxSelectMultiple)
    desc = forms.CharField(label="Описание:", max_length=400, widget=forms.TextInput(attrs={"class": "descfield"}))
    price = forms.FloatField(label="Цена заказа", max_value=10000000, widget=forms.NumberInput(attrs={"class": "myfield"}))
    start = forms.CharField(label="Дата начала исполнения", widget=forms.DateInput(attrs={"class": "myfield"}))
    finish = forms.CharField(label="Дата завершения исполнения", widget=forms.DateInput(attrs={"class": "myfield"}))
    last_name = forms.CharField(label="Фамилия заказчика", max_length=100, widget=forms.TextInput(attrs={"class": "myfield"}))
    first_name = forms.CharField(label="Имя заказчика", max_length=100, widget=forms.TextInput(attrs={"class": "myfield"}))
    mid_name = forms.CharField(label="Отчество заказчика", max_length=100, widget=forms.TextInput(attrs={"class": "myfield"}))
    birth_date = forms.CharField(label="Дата рождения заказчика", widget=forms.DateInput(attrs={"class": "myfield"}))


class Typo(forms.Form):
    name = forms.CharField(label="Название типографии", max_length=200, widget=forms.TextInput(attrs={"class": "myfield"}))
    found_date = forms.CharField(label="Дата основания", widget=forms.DateInput(attrs={"class": "myfield"}))
    region = forms.CharField(label="Страна", max_length=200, widget=forms.TextInput(attrs={"class": "myfield"}))
    city = forms.CharField(label="Город", max_length=200, widget=forms.TextInput(attrs={"class": "myfield"}))
    address = forms.CharField(label="Адрес", max_length=200, widget=forms.TextInput(attrs={"class": "myfield"}))
    desc = forms.CharField(label="Описание типографии", max_length=500, widget=forms.Textarea(attrs={"class": "descfield"}))
    first_name = forms.CharField(label="Имя директора", max_length=200, widget=forms.TextInput(attrs={"class": "myfield"}))
    mid_name = forms.CharField(label="Отчество директора", max_length=200, widget=forms.TextInput(attrs={"class": "myfield"}))
    last_name = forms.CharField(label="Фамилия директора", max_length=200, widget=forms.TextInput(attrs={"class": "myfield"}))
    birth_date = forms.CharField(label="Дата рождения директора", widget=forms.DateInput(attrs={"class": "myfield"}))


