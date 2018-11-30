# -*- coding: utf-8 -*-
"""
Author: Andrew Floyd
Course: CS3001 - Dr. Fu
Data Science Competition Project
"""

import pandas as pd
import matplotlib.pyplot as plt

accepts = pd.read_csv("chefmozaccepts.csv")
cuisine = pd.read_csv("chefmozcuisine.csv")
hours4 = pd.read_csv("chefmozhours4.csv")
parking = pd.read_csv("chefmozparking.csv")
usercuisine = pd.read_csv("usercuisine.csv")
payment = pd.read_csv("userpayment.csv")
userprofile = pd.read_csv("userprofile.csv")
geoplaces2 = pd.read_csv("geoplaces2.csv")

R = pd.read_csv("rating_final.csv")

#train = pd.read_csv("train.txt")
#test = pd.read_csv("test.txt")

###########################################
#Lets do some preprocessing for our tables#
##########################################

#Accepts
#Here is a graph showing the volume of payments accepted
#print(accepts.info())
T1PaymentPlot = accepts.Rpayment.value_counts().plot.bar()
T1PaymentPlot.set_title('Volume of Payments Accepted')
T1PaymentPlot.set_xlabel('Form of Payment')
T1PaymentPlot.set_ylabel('Number of Restaurants using Payment')

#Here we are creating a new table with each restaurant having there own row
#This will tell us which restaurants accept different payments
Accepts_Transform = pd.get_dummies(accepts, columns=['Rpayment'])
#This command combines rows with the same placeID into one row per ID
Accepts_Transform = Accepts_Transform.groupby('placeID', as_index=False).sum()

#Cuisine
#A look at how many unique Restaurant Types we have (Stats)
print("Number of unique Restaurant:", len(cuisine.placeID.unique()))
print("Number of unique Restaurant Types:", len(cuisine.Rcuisine.unique()))
print("A List of all Restaurant Types:")
print(cuisine.Rcuisine.unique())
print()
print()
#Bar Chart of top 20 Restaurant Types Volume
T2CuisinePlot = cuisine.Rcuisine.value_counts()[:20].plot.bar()
T2CuisinePlot.set_title('Volume of Top 20 Restaurant Types')
T2CuisinePlot.set_xlabel('Restaurant Type', size=15)
T2CuisinePlot.set_ylabel('Number of Restaurants')
#Dummy chart transformation
Cuisine_Transform = pd.get_dummies(cuisine, columns=['Rcuisine'])
Cuisine_Transform = Cuisine_Transform.groupby('placeID', as_index=False).sum()

#Hours4
#Stats
print("Number of unique Restaurants in Hours Table:", len(hours4.placeID.unique()))
print("Number of unique times:", len(hours4.hours.unique()))
print("List of Unique days:")
print(hours4.days.unique())
print()
print()
#Not sure if this data will be of much use

#Parking
#Stats
print("Number of unique Restaurants in Parking Table:", len(parking.placeID.unique()))
print()
T4ParkingPlot = parking.parking_lot.value_counts().plot.bar()
T4ParkingPlot.set_title('Volume of Parking Types', size=14)
T4ParkingPlot.set_xlabel('Parking Type', size=12)
T4ParkingPlot.set_ylabel('Count', size=12)
#Dummy Transformation
Parking_Transform = pd.get_dummies(parking, columns=['parking_lot'])
Parking_Transform = Parking_Transform.groupby('placeID', as_index=False).sum()

#UserCuisine
#Stats
print("Number of unique users in usercuisine table:", len(usercuisine.userID.unique()))
print("Number of unique user restuarant categories:", len(usercuisine.Rcuisine.unique()))
print("List of unique user restuarant categories:")
print(usercuisine.Rcuisine.unique())
print()
print()
#Bar Chart of top 20 most popular types
T5UserCuisinePlot = usercuisine.Rcuisine.value_counts()[:20].plot.bar()
T5UserCuisinePlot.set_title('Volume of Top 20 User Favorite Restaurant Types', size=14)
T5UserCuisinePlot.set_xlabel('Restaurant Type', size=12)
T5UserCuisinePlot.set_ylabel('Count', size=12)
#Dummy Transformation
UserCuisine_Transform = pd.get_dummies(usercuisine, columns=['Rcuisine'])
UserCuisine_Transform = UserCuisine_Transform.groupby('userID', as_index=False).sum()

#User Payments
#Stats
print("Number of unique users in payment table:", len(payment.userID.unique()))
print("Number of unique user payment categories:", len(payment.Upayment.unique()))
print("List of unique user payment categories:")
print(payment.Upayment.unique())
print()
print()
#Bar Chart
T6UserPaymentPlot = payment.Upayment.value_counts().plot.bar()
T6UserPaymentPlot.set_title('Volume of User Payments per Type', size=14)
T6UserPaymentPlot.set_xlabel('User Payment Types', size=12)
T6UserPaymentPlot.set_ylabel('Count', size=12)
#Dummy Transformation
Payment_Transformation = pd.get_dummies(payment, columns=['Upayment'])
Payment_Transformation = Payment_Transformation.groupby('userID', as_index=False).sum()
