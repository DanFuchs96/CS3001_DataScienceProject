#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Authors: Andrew Floyd, Daniel Fuchs
Course: CS3001 - Dr. Fu
Data Science Competition Project
"""

###########################
# FEATURE NAME MANAGEMENT #
###########################

def mass_feature_rename(table):
    translator = {'userID': 'userID',
                  'placeID': 'placeID',
                  'rating': 'RATING_GENERAL',
                  'food_rating': 'RATING_FOOD',
                  'service_rating': 'RATING_SERVICE',
                  'alcohol': 'R_alcohol',
                  'smoking_area': 'R_smoking',
                  'accessibility': 'R_accessibility',
                  'price': 'R_price',
                  'franchise': 'R_franchise',
                  'other_services': 'R_services',
                  'Rformal_dress': 'R_formal_dress',
                  'Rquiet': 'R_quiet',
                  'open_area': 'R_open_area',
                  'Rlatitude': 'R_latitude',
                  'Rlongitude': 'R_longitude',
                  'Rcuisine': 'R_cuisine',
                  'accepts_cash': 'R_cash',
                  'accepts_visa': 'R_visa',
                  'accepts_mc_ec': 'R_mc_ec',
                  'accepts_am_exp': 'R_am_exp',
                  'accepts_debit': 'R_debit',
                  'accepts_check': 'R_check',
                  'free_parking': 'R_park_free',
                  'paid_parking': 'R_park_paid',
                  'no_parking': 'R_park_none',
                  'weekdays': 'R_weekday_hrs',
                  'sat_hours': 'R_sat_hrs',
                  'sun_hours': 'R_sun_hrs',
                  'latitude': 'U_latitude',
                  'longitude': 'U_longitude',
                  'smoker': 'U_smoking',
                  'drink_level': 'U_alcohol',
                  'transport': 'U_transport',
                  'interest': 'U_interest',
                  'personality': 'U_personality',
                  'activity': 'U_activity',
                  'weight': 'U_weight',
                  'budget': 'U_budget',
                  'formal_dress': 'U_formal_dress',
                  'quiet': 'U_quiet',
                  'married': 'U_married',
                  'age': 'U_age',
                  'cuisine': 'U_cuisine',
                  'uses_cash': 'U_cash',
                  'uses_visa': 'U_visa',
                  'uses_mc_ec': 'U_mc_ec',
                  'uses_am_exp': 'U_am_exp',
                  'uses_debit': 'U_debit'}
    for column in table.columns:
        translation = translator[column]
        if translation is None or translation == column:
            continue
        else:
            table[translation] = table[column]
            table = table.drop([column], axis=1)
    return table

#############################
# FEATURE: PAYMENT MATCHING #
#############################

###########################
# FEATURE: PAIR PROXIMITY #
###########################