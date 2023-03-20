from django import forms

from .models import Player

position_choices = (
	("Forward", "Forward"),
	("Midfielder", "Midfielder"),
	("Defender", "Defender"),
	("Goalkeeper", "Goalkeeper")
	)

home_state_choices = (
	('AL', 'AL'), 
	('AK', 'AK'),
	('AZ', 'AZ'),
	('AR', 'AR'),
	('CA', 'CA'),
	('CO', 'CO'),
	('CT', 'CT'),
	('DE', 'DE'),
	('FL', 'FL'),
	('GA', 'GA'),
	('HI', 'HI'),
	('ID', 'ID'),
	('IL', 'IL'),
	('IN', 'IN'),
	('IA', 'IA'),
	('KS', 'KS'),
	('KY', 'KY'),
	('LA', 'LA'),
	('ME', 'ME'),
	('MD', 'MD'),
	('MA', 'MA'),
	('MI', 'MI'),
	('MN', 'MN'),
	('MS', 'MS'),
	('MO', 'MO'),
	('MT', 'MT'),
	('NE', 'NE'),
	('NV', 'NV'),
	('NH', 'NH'),
	('NJ', 'NJ'),
	('NM', 'NM'),
	('NY', 'NY'),
	('NC', 'NC'),
	('ND', 'ND'),
	('OH', 'OH'),
	('OK', 'OK'),
	('OR', 'OR'),
	('PA', 'PA'),
	('RI', 'RI'),
	('SC', 'SC'),
	('SD', 'SD'),
	('TN', 'TN'),
	('TX', 'TX'),
	('UT', 'UT'),
	('VT', 'VT'),
	('VA', 'VA'),
	('WA', 'WA'),
	('WV', 'WV'),
	('WI', 'WI'),
	('WY', 'WY'),
	("International", "International"),
	)

class PlayerForm(forms.ModelForm):
	name = forms.CharField()
	age = forms.IntegerField(max_value=99, min_value=16)
	club = forms.CharField(required=False)
	years_played = forms.IntegerField(max_value=99, min_value=0)
	home_location = forms.ChoiceField(choices=home_state_choices)
	position = forms.ChoiceField(choices= position_choices)


	class Meta:
		model = Player
		fields = [
			'name',
			'age',
			'club',
			'years_played',
			'home_location',
			'position']


# class RawPlayerForm(forms.Form):
# 	name = forms.CharField()
# 	age = forms.IntegerField(max_value=99, min_value=16)
# 	club = forms.CharField(required=False)
# 	years_played = forms.IntegerField(max_value=99, min_value=16)
# 	home_location = forms.ChoiceField(choices=home_state_choices)
# 	position = forms.ChoiceField(choices= position_choices)


