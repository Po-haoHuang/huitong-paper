# -*- coding: utf-8 -*-
"""
Created on Mon Jul 06 13:44:07 2015

@author: Po-hao Huang
"""

import database
import sys


def InputHarborPaper(groupNumber, paperWidth, paperRollNumber, paperSpec,
                     paperWeight, paperWeightPerUnit, paperLength,
                     paperStatus):
    m_paper = database.Paper(
    groupNumber = int(groupNumber), paperRollNumber = int(paperRollNumber),
    paperWidth = int(paperWidth), paperSpec = int(paperSpec),
    paperWeight = int(paperWeight), paperWeightPerUnit = int(paperWeightPerUnit),
    paperLength = int(paperLength), paperStatus = int(paperStatus))




if __name__ == "__main__":
    InputHarborPaper(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8])
    sys.exit()