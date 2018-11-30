# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 23:23:14 2018

@author: Andrew
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

train = pd.read_csv("train.txt")
test = pd.read_csv("test.txt")

###########################################
#Lets do some preprocessing for our tables#
##########################################

#Accepts
#Here is a graph showing the volume of payments accepted
#print(accepts.info())
#T1PaymentPlot = accepts.Rpayment.value_counts().plot.bar()
#T1PaymentPlot.set_title('Volume of Payments Accepted')
#T1PaymentPlot.set_xlabel('Form of Payment')
#T1PaymentPlot.set_ylabel('Number of Restaurants using Payment')

#Here we are creating a new table with each restaurant having there own row
#This will tell us which restaurants accept different payments
Accepts_Transform = pd.get_dummies(accepts, columns=['Rpayment'])
Accepts_Transform = Accepts_Transform.groupby('placeID', as_index=False).sum()

#Cuisine
#A look at how many unique Restaurant Types we have
print("Number of unique Restaurant:", len(cuisine.placeID.unique()))
print("Number of unique Restaurant Types:", len(cuisine.Rcuisine.unique()))
print("A List of all Restaurant Types:")
print(cuisine.Rcuisine.unique())
#Bar Chart of top 20 Restaurant Types Volume
T2CuisinePlot = cuisine.Rcuisine.value_counts()[:20].plot.bar()
T2CuisinePlot.set_title('Volume of Top 20 Restaurant Types')
T2CuisinePlot.set_xlabel('Restaurant Type', size=15)
T2CuisinePlot.set_ylabel('Number of Restaurants')
#Dummy chart transformation
Cuisine_Transform = pd.get_dummies(cuisine, columns=['Rcuisine'])
Cuisine_Transform = Cuisine_Transform.groupby('placeID', as_index=False).sum()


