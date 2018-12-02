# < INSERT HEADER BLOCK >
import pandas as pd
from data_cleaning import *

######################
# ID LIST GENERATION #
######################

def generate_user_list():
    t = pd.read_csv("train.csv")['userID']
    t = pd.DataFrame(t.unique())
    t.columns = ['userID']
    return t

def generate_restaurant_list():
    t = pd.read_csv("train.csv")['placeID']
    t = pd.DataFrame(t.unique())
    t.columns = ['placeID']
    return t

#####################
# RESTAURANT TABLES #
#####################

def synthesize_restaurant_profile():
    tables = [clean_loc_geo(), clean_loc_cuisine(), clean_loc_accepts(), clean_loc_parking(), clean_loc_hours()]
    restaurant_profile = pd.DataFrame(generate_restaurant_list())
    for table in tables:
        restaurant_profile = pd.merge(restaurant_profile, table, how='left', on=['placeID'])
    return standardize_restaurant_profile(restaurant_profile)

def standardize_restaurant_profile(table):
    for column in table.columns:
        table[column].fillna(table[column].mode()[0], inplace=True)
    return table

###############
# USER TABLES #
###############

def synthesize_user_profile():
    tables = [clean_user_profile(), clean_user_cuisine(), clean_user_payment()]
    user_profile = pd.DataFrame(generate_user_list())
    for table in tables:
        user_profile = pd.merge(user_profile, table, how='left', on=['userID'])
    return standardize_user_profile(user_profile)

def standardize_user_profile(table):
    for column in table.columns:
        table[column].fillna(table[column].mode()[0], inplace=True)
    return table

############################
# PRIMARY TABLE GENERATION #
############################

# [ W I P ]
