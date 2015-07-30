# -*- coding: utf-8 -*-
"""
Created on Mon Jul 06 13:44:07 2015

@author: Po-hao Huang
"""

import sqlite3 as lite
import os
import sys


DB = os.getcwd()+os.sep+'papers.sqlite'
try:
    paper = lite.connect(DB)
except IOError:
    print ("Error open db.\n")

paper.cursor().execute("CREATE TABLE IF NOT EXISTS paper ( \
  group_number INT NOT NULL, \
  paper_width INT NOT NULL, \
  paper_weight_per_unit INT NOT NULL, \
  paper_spec TEXT NOT NULL, \
  paper_roll_number INT NOT NULL, \
  paper_customer TEXT NOT NULL, \
  paper_status INT NOT NULL, \
  paper_length INT, \
  paper_weight INT, \
  PRIMARY KEY ( group_number, paper_width, paper_spec, paper_weight_per_unit, paper_status, paper_customer ) \
  );" )
paper.commit()


def InputPaper(groupNumber, paperWidth, paperWeightPerUnit, paperSpec,
                     paperRollNumber, paperCustomer, paperStatus):                     
        try:
            sql = "INSERT INTO paper (group_number, paper_width, paper_weight_per_unit, paper_spec,\
                    paper_roll_number, paper_customer, paper_status,\
                    paper_length, paper_weight) VALUES (?,?,?,?,?,?,?,0,0);"
            paper.cursor().execute(sql,(groupNumber, paperWidth, paperWeightPerUnit, paperSpec,\
                 paperRollNumber, paperCustomer, paperStatus))
            paper.commit()
            return 0
           
        except:
            print(sys.exc_info())
            try:
                sql = "UPDATE paper SET paper_roll_number = paper_roll_number + " + paperRollNumber + \
                        ", paper_weight = paper_weight + " + '0' + \
                        ", paper_length = paper_length + " + '0' + \
                        " WHERE group_number = " + groupNumber + \
                        " AND paper_width = " + paperWidth + \
                        " AND paper_spec = " + paperSpec + \
                        " AND paper_weight_per_unit = " + paperWeightPerUnit + \
                        " AND paper_customer = "  + paperCustomer +\
                        " AND paper_status = " + paperStatus +" ;"
                paper.cursor().execute(sql)
                paper.commit()
                return 0
            except:
                try:
                    sql = "UPDATE paper SET paper_roll_number = paper_roll_number + " + paperRollNumber + \
                            ", paper_weight = paper_weight + " + '0' + \
                            ", paper_length = paper_length + " + '0' + \
                            " WHERE group_number = " + groupNumber + \
                            " AND paper_width = " + paperWidth + \
                            " AND paper_spec = " + paperSpec + \
                            " AND paper_weight_per_unit = " + paperWeightPerUnit + \
                            " AND ifnull(paper_customer, '') = ''"\
                            " AND paper_status = " + paperStatus +" ;"
                    paper.cursor().execute(sql)
                    paper.commit()
                    return 0
                except:
                    print(sys.exc_info())
                    return 1



