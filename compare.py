#compare user input against mls_players



from data_model import get_df 
import get_user_player
import data_scripts


def get_result_likelihood():
	states_dict = data_scripts.data.us_states
	states_dict_keys = list(states_dict.keys())
	#print(type(states_dict_keys))

	states_dict_values = list(states_dict.values())
	#print(type(states_dict_values))

	df_cleaned = get_df()

	user_input = get_user_player.main()
	user_input_age = user_input[2]
	user_input_position = user_input[4]
	user_input_home_location = user_input[5]
	user_input_years_experience = user_input[6]


	if user_input_home_location in states_dict_values:
		indx = states_dict_values.index(user_input_home_location)
		user_input_home_location_long = states_dict_keys[indx]
		#print(user_input_home_location_abbrv)
	else:
		user_input_home_location_long = 'International'

	user_input_home_location_long = user_input_home_location_long.replace(' ', '_')
	#rint(df_cleaned.columns)
	#print(" ")
	#print(user_input_age, user_input_position, user_input_home_location, user_input_years_experience)

	pos_str = 'position_' + user_input_position
	home_loc_str = 'home_state_' + user_input_home_location_long


	control_total_players = len(df_cleaned)
	freq_age = len(df_cleaned[df_cleaned['age'] == user_input_age])
	freq_position = len(df_cleaned[df_cleaned[pos_str] == 1])
	freq_years_experience = len(df_cleaned[df_cleaned['years_played'] == user_input_years_experience])
	if home_loc_str in df_cleaned:
		freq_home_location = len(df_cleaned[df_cleaned[home_loc_str] == 1])
	else:
		freq_home_location = 0

	result_likelihood = ((freq_age / control_total_players) + (freq_position / control_total_players) + 
						(freq_home_location / control_total_players) + (freq_years_experience / control_total_players)) / 4

	result_likelihood = round((result_likelihood * 100), 1)
	result_likelihood = str(result_likelihood) + '% '

	#print(result_likelihood)
	return result_likelihood



