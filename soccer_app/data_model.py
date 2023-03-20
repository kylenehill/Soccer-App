import pandas as pd
import sys
#from data import can_provs, us_states
from soccer.data_scripts import data
#sys.path.insert(0, '/Users/kylene/cs469/django_app/soccer_app_stuff/soccer/data_scripts')

# create lists of dictionary values and keys representing US and CAN states
can_provs_list = list(can_provs.values())
us_states_list = list(us_states.values())
us_states_keys_list = list(us_states.keys())


# create df from mls_players.csv with column headers
df = pd.read_csv("mls_players.csv")
df.columns = ['name', 'age', 'club', 'position', 'home_location', 'years_played']


# create empty list to store clean home_state values; loop through current home_state values and append clean value to list
home_location_series_updated = []
home_location_series = df['home_location']

for state in home_location_series:
	if 'International' in state:
		state = 'International'
		home_location_series_updated.append(state)
		#print(state)
	else:
		states_list = state.split()
		for state_item in states_list:
			if state_item in can_provs_list:
				state = 'International'
				home_location_series_updated.append(state)
				continue
			if state_item in us_states_list:
				indx = us_states_list.index(state_item)
				state = us_states_keys_list[indx]
				home_location_series_updated.append(state)
				continue


# add list of cleaned home_state values to df as col
df['home_state_updated'] = home_location_series_updated

# copy df to df_cleaned without uncleaned home_state, age cols
df_cleaned = df[['age', 'position', 'home_state_updated', 'years_played']]

# apply get_dummies to quantify categorical values where 1 is true and 0 is false, add column to indicate pro status
df_cleaned_dummies = pd.get_dummies(data=df_cleaned, prefix='position', columns=['position'])
df_cleaned_dummies = pd.get_dummies(data=df_cleaned_dummies, prefix='home_state', columns=['home_state_updated'])

df_cleaned_dummies['is_pro'] = 1


#print(df_cleaned_dummies)






