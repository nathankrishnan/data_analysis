from processingcsv import *

def num_of_records(data_sample):
	return len(data_sample)

# minus one because we don't want to count the header line of the file
number_of_ties = num_of_records(data_from_csv) - 1

print(number_of_ties, " ties in our data sample")

def num_of_records2(data_sample):
	return data_sample.size

# print(num_of_records2(my_csv))