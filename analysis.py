import csv

# default delimeter is tab but can be changed by passing in an optional paramter for default
def open_csv(filename, default='\t'):
	data = []
	with open(filename, encoding='utf-8') as tsv:
		tie_reader = csv.reader(tsv, delimiter=default)
		for line in tie_reader:
			data.append(line)
	return data

data_from_csv = open_csv('data.csv')
print(data_from_csv[0])
