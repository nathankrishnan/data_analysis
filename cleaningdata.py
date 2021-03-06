from maxandmin import *

def create_boolean_field_from_search_term(data_sample, search_term):
	new_array = []
	new_array.append(data_sample[0].append(search_term))

	# Start from 2nd row
	for row in data_sample[1:]:
		new_bool_field = False
		if search_term in row[7]:
			new_bool_field = True
		row.append(new_bool_field)
		new_array.append(row)
	return new_array

def filter_col_by_bool(data_sample, column):
	matches_search_term = []

	for item in data_sample[1:]:
		if item[column]:
			matches_search_term.append(item)
	return matches_search_term

my_new_csv = create_boolean_field_from_search_term(data_from_csv, "cashmere")

number_of_cashmere_ties = num_of_records(filter_col_by_bool(my_new_csv, 11))

print("Length: ", num_of_records(my_new_csv))
print("Cashmere Ties: ", number_of_cashmere_ties)

