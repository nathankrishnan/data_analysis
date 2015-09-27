from filteringrows import *

gucci_ties = filter_col_by_string(data_from_csv, "brandName", "Gucci")
jcrew_ties = filter_col_by_string(data_from_csv, "brandName", "J.Crew")

max_gucci = find_max(gucci_ties[1:], 2)
max_jcrew = find_max(jcrew_ties[1:], 2)

message = "Maximum {} tie price is = ${:03.2f}"
print(message.format("Gucci", max_gucci))
print(message.format("J.Crew", max_jcrew))

message = "Average price of {} ties are = ${:03.2f}"
avg_gucci = find_average(gucci_ties)
avg_jcrew = find_average(jcrew_ties)
print(message.format("Gucci", avg_gucci))
print(message.format("J.Crew", avg_jcrew))

striped_ties = filter_col_by_string(data_from_csv, "print", "_striped")
paisley_ties = filter_col_by_string(data_from_csv, "print", "_paisley")
solid_ties = filter_col_by_string(data_from_csv, "print", "_solid")





