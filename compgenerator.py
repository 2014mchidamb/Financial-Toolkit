import csv
from yhoofuncs import keystatfunc
import numpy as np

comps = ["Company", "Market Cap", "EV", "Revenue (ttm)", "EBITDA (ttm)", "P/E (ttm)", "Price/Sales (ttm)", "Price/Book (mrq)", "EV/Revenue", "EV/EBITDA"]
compnums = [0, 1, 15, 19, 2, 5, 6, 7, 8] #corresponding indices for comps
comp_list = raw_input("Enter a space-separated list of companies: ").split(" ")
filename = comp_list[0]+"comps.csv"

ofile = open(filename, 'wb')
with open(filename, 'wb') as ofile:
	csvout = csv.writer(ofile, dialect='excel', quoting=csv.QUOTE_ALL)
	csvout.writerow(comps)
	statlists = []
	for i in compnums:
		statlists += [[]]
	for comp in comp_list[1:]:
		vals = [comp]
		stats = keystatfunc(comp)
		if stats != []:
			counter = 0
			for i in compnums:
				vals += [stats[i]]
				if counter > 3:
					statlists[counter] += [float(stats[i])]
				else:
					statlists[counter] += []
				counter += 1
			csvout.writerow(vals)
	csvout.writerow([])
	medians = ['Medians']
	means = ['Means']
	for stat in statlists:
		if stat != []:
			medians += [np.median(stat)]
			means += [np.mean(stat)]
		else:
			medians += [""]
			means += [""]
	csvout.writerow(medians)
	csvout.writerow(means)
	csvout.writerow([])
	vals = [comp_list[0]]
	stats = keystatfunc(comp_list[0])
	if stats != []:
		for i in compnums:
			vals += [stats[i]]
	csvout.writerow(vals)
