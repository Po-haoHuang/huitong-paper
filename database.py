# -*- coding: utf-8 -*-
"""
Created on Mon Jul 06 13:44:07 2015

@author: Po-hao Huang
"""

from sqlobject import *
import re
import os
import sys

__connection__ = 'sqlite:' + os.getcwdu()+os.sep+'papers.sqlite'

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


class Paper(SQLObject):
    """
        Recepie class/table.
        name_recepie: the recepie name
        ingredients_recepie : list of ingredients, is a foreign key (1-n)
        votes_recepies: this will help us see the nb of the reviews
        description_recepie: an abstract description of the recepie
        steps_recepies: the steps that we have to do for making that recepie
    """

#    ingredients_recepie = RelatedJoin('IngredientCouple')
    groupNumber = IntCol()
    paperWidth = IntCol()
    paperWeight = IntCol()
    paperWeightPerUnit = IntCol()
    paperRollNumber = IntCol()
    paperSpec = StringCol()
    paperLength = IntCol()
    paperStatus = IntCol()
    paperIndex = DatabaseIndex('groupNumber', 'paperWidth', 'paperWeightPerUnit',
                               'paperSpec', 'paperStatus', unique = True)
#    votes_recepie = IntCol()
#    site_recepie = StringCol(length=50)
#    description_recepie = StringCol(length=600)
#    steps_recepie = StringCol(length=1000)
#    name_recepie = StringCol(length=200)


#Create the 2 tables in our sqllite db.
#IngredientCouple.createTable()
#IngredientCouple._connection.debug = False
if Paper._connection.tableExists('paper'):
    Paper._connection.debug = False
else:    
    Paper.createTable()
    Paper._connection.debug = False
    
def InputPaper(groupNumber, paperWidth, paperRollNumber, paperSpec,
                     paperWeight, paperWeightPerUnit, paperLength,
                     paperStatus):
    m_paper = database.Paper(
    groupNumber = int(groupNumber), paperRollNumber = int(paperRollNumber),
    paperWidth = int(paperWidth), paperSpec = int(paperSpec),
    paperWeight = int(paperWeight), paperWeightPerUnit = int(paperWeightPerUnit),
    paperLength = int(paperLength), paperStatus = int(paperStatus))

#Recepie.sqlmeta.addJoin(MultipleJoin('IngredientCouple',
#                                     joinMethodName='ingredients_recepie'))


