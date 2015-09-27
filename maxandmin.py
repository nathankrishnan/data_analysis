from average import *

def find_max(data_sample, column):
	temp_list = []
	for row in data_sample:
		price = float(row[column])
		temp_list.append(price)
	return max(temp_list)

def find_min(data_sample, column):
	temp_list = []
	for row in data_sample:
		price = float(row[column])
		temp_list.append(price)
	return min(temp_list)


# def find_max_min(data_sample, column, minormax):
	

print(find_max(data_from_csv[1:], 2))
print(find_min(data_from_csv[1:], 2))

# Achieving this in numpy
price = my_csv['priceLabel']
prices_in_float = [float(x) for x in price]
numpy_max = numpy.amax(prices_in_float)
print(Numpy Max: numpy_max)