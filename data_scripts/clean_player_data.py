# script to get list of MLS players from txt files and write to csv

import json, os, csv
import data

# players list
players_list = []

# csv field names
fields = ['player_name', 'age', 'club_name', 'player_position', 'player_hometown', 'years_played'] 

# location values from data.py file
can_keys = data.can_provs.keys()
can_values = data.can_provs.values()
us_states_keys = data.us_states.keys()
us_states_values = data.us_states.values()
us_states_cleaned_keys = data.states_cleaned.keys()
us_states_cleaned_values = data.states_cleaned.values()


player_positions = ['Forward', 'Midfielder', 'Defender', 'GK', 'Goalkeeper']

for current_file in data.filename_list:

	raw_player_file = open(current_file, 'r')

	file_lines = raw_player_file.readlines()
	count = 0



	for line in file_lines:

		count += 1


		# gets player club and player name from same line
		if [x for x in data.clubs if x in line] != []:
			player_club = [x for x in data.clubs if x in line][0]

			player_name = line.replace(player_club, '').strip()




		# get player age with value on next line
		if 'Age:' in line:
			next_line = file_lines[count]
			if len(next_line.strip()) == 2:
				player_age = int(next_line.strip())


				# calculates player_years_played by age - 16
				player_years_played = player_age - 16


		# get player position
		if [x for x in player_positions if x in line] != []:
			player_pos = [x for x in player_positions if x in line][0]



		# get player home location
		if ',' in line:
			if 'Age:' in line:
				player_home_location = line.replace('Age:', '').strip()
				player_home_loc_list = player_home_location.split(',')

				player_home_loc_list = [x.strip() for x in player_home_loc_list]



				if player_home_loc_list[1] in can_keys:
					player_home_loc_list[1] = data.can_provs[player_home_loc_list[1]]
				elif player_home_loc_list[1] in can_values:
					pass
				elif player_home_loc_list[1] in us_states_keys: 
					player_home_loc_list[1] = data.us_states[player_home_loc_list[1]]
				elif player_home_loc_list[1] in us_states_values:
					pass
				elif player_home_loc_list[1] in us_states_cleaned_keys:
					player_home_loc_list[1] = data.us_states[data.states_cleaned[player_home_loc_list[1]]]
				elif player_home_loc_list[1] in us_states_cleaned_values:
					pass
				else:
					player_home_loc_list.append('International')


			player_home_loc_str = ''
			for home_loc in player_home_loc_list:
				if home_loc == player_home_loc_list[-1]:
					player_home_loc_str += home_loc
				else:
					player_home_loc_str += home_loc + ', '




		if 'View More' in line:
			if player_home_loc_str == '':
				player_home_loc_str += 'International'
			player_info = [player_name, player_age, player_club, player_pos, player_home_loc_str, player_years_played]
			#print(player_info)
		
			players_list.append(player_info)

			# reset player record after each player added
			player_name = ''
			player_age = ''
			player_club = ''
			player_pos =''
			player_home_loc_str =''
			player_years_played = ''




# writes to csv
with open('mls_players.csv', 'w') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(fields)
    write.writerows(players_list)



print('csv complete, check directory..')






