# -*- coding: utf-8 -*-
"""
Created on Mon Jul 06 13:44:07 2015

@author: Po-hao Huang
"""

import database
import sys
import sqlite3 as lite
import pandas.io.sql as psql, pandas
DB = 'papers.sqlite'
try:
	paper = lite.connect(DB)
except IOError:
	print "Error open db.\n"



def InputHarborPaper(groupNumber, paperWidth, paperRollNumber, paperSpec,
                     paperWeight, paperWeightPerUnit, paperLength,
                     paperStatus):
	pass

#    try:
#		m_paper = database.Paper(
#		groupNumber = int(groupNumber), paperRollNumber = int(paperRollNumber),
#		paperWidth = int(paperWidth), paperSpec = str(paperSpec),
#		paperWeight = int(paperWeight), paperWeightPerUnit = int(paperWeightPerUnit),
#		paperLength = int(paperLength), paperStatus = int(paperStatus))
#    except:
#		sql = "INSERT OR IGNORE INTO paper (group_number, paper_width, paper_roll_number, paper_spec,\
#                     paper_weight, paper_weight_per_unit, paper_length,\
#                     paper_status) VALUES (2,9,1,1,1,1,2,1);"
#		# sql_ing = "SELECT * FROM ingredient_couple"
#		# sql_join = "SELECT * FROM ingredient_couple_recepie"
#		try:
#			sql = "INSERT INTO paper (group_number, paper_width, paper_roll_number, paper_spec,\
#					paper_weight, paper_weight_per_unit, paper_status,\
#					paper_length) VALUES (" + groupNumber + "," + paperWidth + "," \
#					+ paperRollNumber + "," + paperSpec + ","+ paperWeight + "," + paperWeightPerUnit + ","\
#					+ paperStatus + "," + paperLength + ");"
#			paper.cursor().execute(sql)
#		except Exception, e:
#			#print e
#			sql = "UPDATE paper SET paper_roll_number = paper_roll_number + " + paperRollNumber + \
#					", paper_weight = paper_weight + " + paperWeight + \
#					", paper_length = paper_length + " + paperLength + \
#					" WHERE group_number = " + groupNumber + \
#					" AND paper_width = " + paperWidth + \
#					" AND paper_spec = " + paperSpec + \
#					" AND paper_weight_per_unit = " + paperWeightPerUnit + \
#					" AND paper_status = " + paperStatus +";"
#			paper.cursor().execute(sql)
#		paper.commit()
#		# panda_ing = psql.frame_query(sql_ing, recepie)
#		# panda_join = psql.frame_query(sql_join, recepie)
#		# panda_ingredient = psql.DataFrame().join\
#		# ([panda_ing, panda_join], how="outer")



if __name__ == "__main__":
    InputHarborPaper(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8])
    sys.exit()