import csv
import numpy

# default delimeter is tab but can be changed by passing in an optional paramter for default
def open_csv(filename, default='\t'):
	data = []
	with open(filename, encoding='utf-8') as tsv:
		tie_reader = csv.reader(tsv, delimiter=default)
		for line in tie_reader:
			data.append(line)
	return data

data_from_csv = open_csv('data.csv')
#print(data_from_csv[0])
#print(data_from_csv)

FIELDNAMES = ['', 'id', 'priceLabel', 'name', 'brandId', 'brandName', 'imageLink', 'desc', 'vendor', 'pattern', 'material']

# 'b' boolean
# 'i' (signed) integer
# 'u' unsigned integer
# 'f' floating-point
# 'c' complex-floating point
# 'O' (Python) objects
# 'S', 'a'    (byte-)string
# 'U' Unicode
# 'V' raw data (void)

DATATYPES = [('myint', 'i'), ('myid', 'i'), ('price', 'f8'), ('name', 'a200'),
             ('brandId', '<i8'), ('brandName', 'a200'), ('imageUrl', '|S500'), 
             ('description', '|S900'),  ('vendor', '|S100'),  ('pattern', '|S50'),  ('material', '|S50'), ]



def load_data(filename, default='\t'):
	# Skip the header line of the file, which is line one
	my_csv = numpy.genfromtxt(filename, delimiter=default, skip_header=1, invalid_raise=False, names=FIELDNAMES, dtype=DATATYPES)
	return my_csv

my_csv = load_data('data.csv')
#print(my_csv)

