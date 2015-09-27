from groupingrows import *

def write_to_file(filename, data_sample):
	example = csv.writer(open(filename, 'w', encoding='utf-8'), dialect='excel')
	example.writerows(data_sample)

write_to_file("_data/solid_ties.csv", solid_ties)