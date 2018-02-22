#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 09:23:59 2018

@author: geoff
"""

#%% specifying data location data from gitHub, preparing data

import os
import xlrd
#folderData="https://raw.githubusercontent.com/geeoffgoond/psrcdata/master/"
folderData="https://rawgit.com/geeoffgoond/psrcdata/master/"
fileXL=os.path.join(folderData,"2015-pr1-hhsurvey-household.xlsx")

# importing data into pandas
import pandas as pd

psrchh=pd.read_excel(fileXL)

#%% limiting columns and data to what we need

psrchh=psrchh[["hhid", "hhnumtrips", "hh_income_detailed", "h_zip", "h_city", "res_factors_hhchange", "res_factors_afford", "res_factors_school", "res_factors_walk", "res_factors_space", "res_factors_closefam", "res_factors_transit", "res_factors_hwy", "res_factors_30min", "prev_home_loc_zip", "prev_home_loc_city", "prev_home_loc_st"]]

WASzip=psrchh[psrchh.prev_home_loc_st=='WA']

WASzip.reset_index(inplace=True,drop=True) # resetting the index -- good practice

#As the cells have integers, I am confident to use comparisons:
WASzip=WASzip[(WASzip.prev_home_loc_zip <=99403) & (WASzip.prev_home_loc_zip>=98001)]

#dropping na
WASzip.dropna(axis=0,inplace=True)

#%% checking some things
WASzip.prev_home_loc_zip