#!/usr/bin/python 
#Input:			Name, Platform, Year, Genre, Publisher, Sales from regions: (North America, Europe, Japan, Others, Global), Critic score, Critic count, User score, User count, Developer, Rating
#Sample_Input:	Dungeon Explorer: Warriors of Ancient Arts, PSP, 2007, Role-Playing, Rising Star, Games, 0.01, 0, 0, 0, 0.01, 56, 13, 5.5, 4, Hudson Soft, T
#Output:		(Key : Value) :: (Genre : TotalSales(NA, EU, JP, Others, Global)) 

import sys
total = 0.0 
f = open("/home/yashas/hadoop/intRes", "w+") 

for i in sys.stdin: 
	row = i.strip().split("\t") 
	if len(row) == 16:
		name, pf, year, genre, pub, sNa, sEu, sJp, sOt, sGl, cScore, cCount, uScore, uCount, dev, rating = row 
	total = float(sNa) + float(sEu) + float(sJp) + float(sOt) + float(sGl) 
	print("{0}\t{1}".format(genre, total)) 
	f.write("{0}\t{1}\n".format(genre, total))

f.close()