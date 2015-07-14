# -*- coding: utf-8 -*-
"""
Created on Mon Jul 06 13:44:07 2015

@author: Po-hao Huang
"""

from sqlobject import *
import sqlite3 as lite
import pandas.io.sql as psql
import re
import os
import sys




DB = os.getcwdu()+os.sep+'papers.sqlite'
try:
	paper = lite.connect(DB)	
except IOError:
	print "Error open db.\n"

sql = "CREATE TABLE IF NOT EXISTS paper ( \
  group_number INT NOT NULL, \
  paper_width INT NOT NULL, \
  paper_roll_number INT NOT NULL, \
  paper_spec CHAR(10) NOT NULL, \
  paper_weight INT NOT NULL, \
  paper_weight_per_unit INT NOT NULL, \
  paper_status INT NOT NULL, \
  paper_length INT NOT NULL, \
  PRIMARY KEY ( group_number, paper_width,paper_spec, paper_weight_per_unit, paper_status ) \
  );" 
paper.cursor().execute(sql)
paper.commit()

#__connection__ = 'sqlite:' + os.getcwdu()+os.sep+'papers.sqlite'

#class IngredientCouple(SQLObject):
#    """
#        Ingredient and the amount of the ingredient.
#        ingredient: the name of the ingredient
#        amount: the amount of that ingredient
#        recepies: the recepies in with we can find this couple
#    """
#    ingredient = StringCol(length=200)
#    amount =  StringCol()
#    recepies = RelatedJoin('Recepie')


#class Paper(SQLObject):
#    """
#        Recepie class/table.
#        name_recepie: the recepie name
#        ingredients_recepie : list of ingredients, is a foreign key (1-n)
#        votes_recepies: this will help us see the nb of the reviews
#        description_recepie: an abstract description of the recepie
#        steps_recepies: the steps that we have to do for making that recepie
#    """
#
##    ingredients_recepie = RelatedJoin('IngredientCouple')
#    groupNumber = IntCol()
#    paperWidth = IntCol()
#    paperWeight = IntCol()
#    paperWeightPerUnit = IntCol()
#    paperRollNumber = IntCol()
#    paperSpec = StringCol()
#    paperLength = IntCol()
#    paperStatus = IntCol()
#    paperIndex = DatabaseIndex('groupNumber', 'paperWidth', 'paperWeightPerUnit',
#                               'paperSpec', 'paperStatus', unique = True)


#Create the 2 tables in our sqllite db.
#IngredientCouple.createTable()
#IngredientCouple._connection.debug = False
#if Paper._connection.tableExists('paper'):
#    Paper._connection.debug = False
#else:    
#    Paper.createTable()
#    Paper._connection.debug = False
    
def InputPaper(groupNumber, paperWidth, paperRollNumber, paperSpec,
                     paperWeight, paperWeightPerUnit, paperLength,
                     paperStatus):
    m_paper = database.Paper(
    groupNumber = int(groupNumber), paperRollNumber = int(paperRollNumber),
    paperWidth = int(paperWidth), paperSpec = int(paperSpec),
    paperWeight = int(paperWeight), paperWeightPerUnit = int(paperWeightPerUnit),
    paperLength = int(paperLength), paperStatus = int(paperStatus))


