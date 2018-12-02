#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Authors: Andrew Floyd, Daniel Fuchs
Course: CS3001 - Dr. Fu
Data Science Competition Project
"""
from numpy import cos

###########################
# FEATURE NAME MANAGEMENT #
###########################

def mass_feature_rename(table):
    translator = {'revID': 'revID',
                  'userID': 'userID',
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
        if column not in translator:
            continue
        translation = translator[column]
        if translation == column:
            continue
        else:
            table[translation] = table[column]
            table = table.drop([column], axis=1)
    return table

def extract_features(table):
    non_features = ['revID', 'userID', 'placeID', 'RATING_GENERAL', 'RATING_SERVICE', 'RATING_FOOD']
    features = []
    for column in table.columns:
        if column not in non_features:
            features.append(column)
    return table[features]

############################
# FEATURE: PAYMENT METHODS #
############################

def feature_payment_score(table, remove=True):
    r_fs = ['R_cash', 'R_visa', 'R_mc_ec', 'R_am_exp', 'R_debit']
    u_fs = ['U_cash', 'U_visa', 'U_mc_ec', 'U_am_exp', 'U_debit']
    n_fs = ['cash', 'visa', 'mc_ec', 'am_exp', 'debit']
    for i in range(min(len(r_fs), len(u_fs))):
        table.loc[(table[r_fs[i]] != table[u_fs[i]]), 'match_' + n_fs[i]] = -1
        table.loc[(table[r_fs[i]] == table[u_fs[i]]) | table[r_fs[i]], 'match_' + n_fs[i]] = 0
        table.loc[(table[r_fs[i]] == table[u_fs[i]]) & table[u_fs[i]], 'match_' + n_fs[i]] = 3
    table['payment_score'] = table.match_cash+table.match_visa+table.match_mc_ec+table.match_am_exp+table.match_debit
    if remove:
        for i in range(min(len(r_fs), len(u_fs))):
            table = table.drop(['match_' + n_fs[i]], axis=1)
            table = table.drop([r_fs[i]], axis=1)
            table = table.drop([u_fs[i]], axis=1)
    return table

###########################
# FEATURE: PAIR PROXIMITY #
###########################

def feature_pair_proximity(table, remove=True, keep_distance=True):
    table['D_lat'] = abs(table.R_latitude - table.U_latitude)
    table['D_long'] = abs(table.R_longitude - table.U_longitude)
    table['distance'] = (((table.D_lat * (111132.954 - 559.822 * cos(2.0 * table.R_latitude) +
                                          1.175 * cos(4.0 * table.R_latitude)))**2) +
                         ((table.D_long * ((3.14159265359/180) * 6367449 * cos(table.R_latitude)))**2)
                         ) ** 0.5

    # Creating banded feature "Proximity"
    table.loc[table.distance >= 5000, 'proximity'] = 0
    table.loc[table.distance < 5500, 'proximity'] = 1
    table.loc[table.distance < 4000, 'proximity'] = 2
    table.loc[table.distance < 2900, 'proximity'] = 3
    table.loc[table.distance < 2200, 'proximity'] = 4
    table.loc[table.distance < 1700, 'proximity'] = 5
    table.loc[table.distance < 1200, 'proximity'] = 6
    table.loc[table.distance < 800, 'proximity'] = 7
    table.loc[table.distance < 500, 'proximity'] = 8
    table.loc[table.distance < 300, 'proximity'] = 9
    table.loc[table.distance < 150, 'proximity'] = 10
    table.loc[table.distance < 100, 'proximity'] = 11
    table.loc[table.distance < 70, 'proximity'] = 12
    table.loc[table.distance < 40, 'proximity'] = 13
    table.loc[table.distance < 25, 'proximity'] = 14

    # Cleaning up table
    if remove:
        for column in ['D_lat', 'D_long', 'R_latitude', 'R_longitude', 'U_latitude', 'U_longitude']:
            table = table.drop([column], axis=1)
    if not keep_distance:
        table = table.drop(['distance'], axis=1)
    return table

#########################
# FEATURE: AVAILABILITY #
#########################

def feature_availability(table, remove=True):
    table['avg_hours'] = (table.R_weekday_hrs + table.R_sat_hrs + table.R_sun_hrs) / 3
    table['days_open'] = 0
    table.loc[table.R_weekday_hrs > 0, 'days_open'] += 5
    table.loc[table.R_sat_hrs > 0, 'days_open'] += 1
    table.loc[table.R_sun_hrs > 0, 'days_open'] += 1

    # Cleaning up table
    if remove:
        for column in ['R_weekday_hrs', 'R_sat_hrs', 'R_sun_hrs']:
            table = table.drop([column], axis=1)
    return table

#########
# notes #################
#########

# Some good features would likely include matching smoking and alcohol consumption. There's also quietness, and budget.
# Price, budget and whatnot would likely go with activity (jobs and etc). Formal dress is another simple matching.
# For dealing with cuisine, we can take the currently stored psuedo-lists and count cross-matches or something.
# Parking matters for rich people and those who have cars. Married people might care about non-quietness.
# Franchise might not matter. Dunno how to use personality / interest; probably useful for service rating though.
#
# A lot of these may not appear super helpful, but the model we use may pick up on something that we didn't expect.
# I pruned a lot of things during the initial feature cleaning, but there's always room to add some back if we need
# to. For the time being, we're a good bit along through the pre-processing stage.
