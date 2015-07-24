# -*- coding: utf-8 -*-
"""
Created on Mon Jul 06 13:44:07 2015

@author: Po-hao Huang
"""

import sqlite3 as lite
import os


DB = os.getcwdu()+os.sep+'papers.sqlite'
try:
	paper = lite.connect(DB)
except IOError:
	print "Error open db.\n"

paper.cursor().execute("CREATE TABLE IF NOT EXISTS paper ( \
  group_number INT NOT NULL, \
  paper_width INT NOT NULL, \
  paper_roll_number INT NOT NULL, \
  paper_spec TEXT NOT NULL, \
  paper_weight INT, \
  paper_weight_per_unit INT NOT NULL, \
  paper_status INT NOT NULL, \
  paper_length INT, \
  PRIMARY KEY ( group_number, paper_width, paper_spec, paper_weight_per_unit, paper_status ) \
  );" )
paper.commit()


def InputPaper(groupNumber, paperWidth, paperRollNumber, paperSpec,
                     paperWeight, paperWeightPerUnit, paperLength,
                     paperStatus):
		try:
			sql = "INSERT INTO paper (group_number, paper_width, paper_roll_number, paper_spec,\
					paper_weight, paper_weight_per_unit, paper_status,\
					paper_length) VALUES (?,?,?,?,?,?,?,?);"
			paper.cursor().execute(sql,(groupNumber, paperWidth, paperRollNumber, paperSpec,\
               paperWeight, paperWeightPerUnit, paperStatus, paperLength))
		except Exception,e:
			sql = "UPDATE paper SET paper_roll_number = paper_roll_number + " + paperRollNumber + \
					", paper_weight = paper_weight + " + paperWeight + \
					", paper_length = paper_length + " + paperLength + \
					" WHERE group_number = " + groupNumber + \
					" AND paper_width = " + paperWidth + \
					" AND paper_spec = " + paperSpec + \
					" AND paper_weight_per_unit = " + paperWeightPerUnit + \
					" AND paper_status = " + paperStatus +";"
			paper.cursor().execute(sql)
		paper.commit()


