from sumandtotal import *

def find_average(data_sample, header=True):
	if header:
		data_sample = data_sample[1:]
	else:
		data_sample = data_sample 
	total = calculate_sum(data_sample)
	size = num_of_records(data_sample)
	return (total / size)

average_price = find_average(data_from_csv)
print("Average =", average_price)
print('Average = {:03.2f}'.format(average_price))

midpoint = round(number_of_ties / 2)
message = "Average of {} half = {:03.2f}"
print(message.format("1st", find_average(data_from_csv[:midpoint])))
print(message.format("2nd", find_average(data_from_csv[midpoint:], False)))
