#!/usr/bin/python
#Stats: 8147/16719 (Approximately 48.729% of the total data is selected and converted to K:V Pairs)

import sys

total = 0
prevKey = None

for i in sys.stdin:
	row = i.strip().split("\t")
	if len(row) != 2:
		continue

	curKey, curSale = row

	if prevKey and prevKey != curKey:
		print (prevKey, "\t", total)
		prevKey = curKey
		total = 0

	prevKey = curKey
	total += float(curSale)

if prevKey != None:
	print(prevKey, "\t", total)