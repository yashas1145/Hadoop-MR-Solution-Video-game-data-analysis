#!/usr/bin/python

import matplotlib.pyplot as plt

cat, value = [], []

data = open('res', 'r')
for row in data:
	row = row.split("\t")
	cat.append(row[0])
	value.append(float(row[1][:-2]))
	
plt.bar(cat, value, color='b', label='Sales Vs Category')
plt.xlabel('Category', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.title('Sales vs Category', fontsize=12)
plt.legend()
plt.show()