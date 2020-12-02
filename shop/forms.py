# -*- coding: utf-8 -*-
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from shop.validator import Validator


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].label = 'Логин'
		self.fields['password'].label = 'Пароль'

	def clean(self):
		username = self.cleaned_data['username']
		password = self.cleaned_data['password']

		if not User.objects.filter(username=username).exists():
			raise forms.ValidationError('Пользователь с данным логином не зарегистрирован в системе!',
										code='username_not_in_system')

		user = User.objects.get(username=username)

		if user and not user.check_password(password) :
			raise forms.ValidationError('Неверный пароль!', code='false_password')


class RegistrationForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	password_check = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = [
			'username',
			'password',
			'password_check',
			'first_name',
			'last_name',
			'email'
		]

	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		self.fields['username'].label = 'Логин'
		self.fields['username'].help_text = 'Обязательное поле. 3-150 символов. Только буквы, цифры и символы @/./+/-/_.'
		self.fields['password'].label = 'Пароль'
		self.fields['password'].help_text = 'Придумайте пароль 3-150 символов.'
		self.fields['password_check'].label = 'Повторите пароль'
		self.fields['first_name'].label = 'Имя'
		self.fields['last_name'].label = 'Фамилия'
		self.fields['email'].label = 'Ваша почта'
		self.fields['email'].help_text = 'Пожалуйста, указывайте реальный адрес.'

	def clean(self):
		username = self.cleaned_data['username']
		password = self.cleaned_data['password']
		password_check = self.cleaned_data['password_check']
		# email = self.cleaned_data['email']

		if not Validator.check_length(username, 3, 150):
			raise forms.ValidationError('Неверная длина логина!')
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError('Пользователь с данным логином уже зарегистрирован в системе!')
		if not Validator.check_length(password, 3, 150):
			raise forms.ValidationError('Неверная длина пароля!')
		if password != password_check:
			raise forms.ValidationError('Ваши пароли не совпадают! Попробуйте снова.')
		# if not Validator.check_email(email):
		# 	raise forms.ValidationError('Неверная почта!')
		# if User.objects.filter(email=email).exists():
		# 	raise forms.ValidationError('Пользователь с данным почтовым адресом уже зарегистрирован в системе!')




class OrdForm(forms.Form):

	name = forms.CharField()
	last_name = forms.CharField(required=False)
	phone = forms.CharField()
	buying_type = forms.ChoiceField(widget=forms.Select(), choices=([("self", "Самовывоз"), ("delivery", "Доставка")]))
	date = forms.DateField(widget=forms.SelectDateWidget(), initial=timezone.now())
	address = forms.CharField(required=False)
	comments = forms.CharField(widget=forms.Textarea, required=False)

	def __init__(self, *args, **kwargs):
		super(OrdForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = 'Имя'
		self.fields['last_name'].label = 'Фамилия'
		self.fields['phone'].label = 'Контактный телефон'
		self.fields['phone'].help_text = 'Пожалуйста, указывайте реальный номер телефона, по которому с Вами можно связаться'
		self.fields['buying_type'].label = 'Способ получения'
		self.fields['buying_type'].help_text = 'Доставка производится на следующий день после оформелния заказа. Менеджер с Вами предварительно свяжется'
		self.fields['address'].label = 'Адрес доставки'
		self.fields['address'].help_text = 'Обязательно указывайте город!'
		self.fields['comments'].label = 'Комментарии к заказу'
		self.fields['date'].label = 'Дата доставки'
		self.fields['date'].help_text = 'Доставка производится на следующий день после оформелния заказа. Менеджер с Вами предварительно свяжется'