# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 19:47:24 2022

@author: ASUS
"""
#import library
import pandas as pd


#import/load the csv file
data = pd.read_csv( 'transaction.csv', sep=';')

#get info about the dataframe 
data.info()


#inserting new modified column
data['CostPerTransaction']= data['CostPerItem'] * data['NumberOfItemsPurchased']

data['SalePerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

data['ProfitPreTransaction'] = data['SalePerTransaction'] - data['CostPerTransaction']

data['Markup'] = round(((data['ProfitPreTransaction'])/ data['CostPerTransaction']),2)

#Convert data type
day=data['Day'].astype(str)
year= data['Year'].astype(str)

#concatenate string
my_date = day + '-' + data['Month'] + '-' + year
data['Date']= my_date

#Spliting string
split_column= data['ClientKeywords'].str.split( ',', expand=True)

data['ClientAge']= split_column[0]
data['ClientType']= split_column[1]
data['LengthOfContract']= split_column[2]

data['ClientAge']=data['ClientAge'].str.replace('[','')
data['LengthOfContract']=data['LengthOfContract'].str.replace(']','')

data["ItemDescription"] = data["ItemDescription"].str.lower()


season = pd.read_csv( 'value_inc_seasons.csv', sep=';')
#merge data
data= pd.merge(data,season, on ='Month')

#Drop column
data = data.drop('ClientKeywords', axis= 1)
data = data.drop(['Day','Year'], axis= 1)



#Export into csv

data.to_csv('valueInc_Cleaned.csv',index=False)
























