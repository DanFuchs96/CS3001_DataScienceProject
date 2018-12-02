# < INSERT HEADER BLOCK >
import pandas as pd
from data_cleaning import *

#####################
# RESTAURANT TABLES #
#####################

def synthesize_restaurant_profile():
    tables = [clean_loc_geo(), clean_loc_cuisine(), clean_loc_accepts(), clean_loc_parking(), clean_loc_hours()]
    restaurant_profile = clean_rating('placeID')
    for table in tables:
        print(table)
        print(restaurant_profile)
        restaurant_profile = pd.merge(restaurant_profile, table, on=['placeID'])
    return restaurant_profile
