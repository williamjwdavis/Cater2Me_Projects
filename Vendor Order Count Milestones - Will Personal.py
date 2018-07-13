import pandas as pd
from datetime import datetime

#Will Davis#

start=datetime.now()

#Make Edits Here 
milestone = [100, 250, 500, 750]
beginning_date = "05-31-2018"
ending_date = "06-30-2018"
#Make Edits Here ^

#Web data imports were deleted for confidentiality reasons

#Count Distributors
def findHistoricalOrderCount(orderIndex, vendorIndex, ordersData = [], vendorData = [], ):
    ordersDataLength = len(ordersData)
    for vendorIndex in range(len(vendorData)):
        while (ordersData[orderIndex] == vendorData[vendorIndex]):
            vendor_historical_order_count[vendorIndex] = vendor_historical_order_count[vendorIndex] + 1
            if orderIndex + 1 < ordersDataLength:
                orderIndex = orderIndex + 1
            else: return     
def findMonthOrderCount(orderIndex, vendorIndex, ordersData = [], vendorData = [], ):
    ordersDataLength = len(ordersData)
    for vendorIndex in range(len(vendorData)):
        while (ordersData[orderIndex] == vendorData[vendorIndex]):
            vendor_month_order_count[vendorIndex] = vendor_month_order_count[vendorIndex] + 1
            if orderIndex + 1 < ordersDataLength:
                orderIndex= orderIndex+1
            else: return

#Date Locations
def findBeginningDate(date, orders = []):
    for index in range(len(orders)):
        if date == orders[len(orders)-index - 1]:
            return len(orders) - index
def findEndingDate(date, orders = []):
    for index in range(len(orders)):
        if date == orders[len(orders)-index-1]:
            return len(orders)-index-1
    
OrderForDate = data.OrderForDate 
Market_Vendor = data.Market_Vendor
Market_Access_Order_ID = data.Market_Access_Order_ID
vendor = vendor_df.market_vendor

Market_Vendor = list(Market_Vendor)
vendor = list(vendor)

beginningLoc=0
endingLoc=0
milestone1_vendors = []
milestone2_vendors = []
milestone3_vendors = []
milestone4_vendors = []
vendor_historical_order_count = []
vendor_month_order_count = []

#Find beginningLoc and endingLoc
findBeginningDate(beginning_date, OrderForDate)
findEndingDate(ending_date, OrderForDate)

#particition Market_Vendor into before the month
#we care about, and strickly the month in question
historical_orders = Market_Vendor[0:beginningLoc]
last_month_orders = Market_Vendor[beginningLoc+1:endingLoc]

#sort the lists so that they're in a common alphabetical order
vendor.sort()
historical_orders.sort()
last_month_orders.sort()

#initializing vendor_order_count
for i in range(len(vendor)):
    vendor_historical_order_count.append(0)
    vendor_month_order_count.append(0)

#calculate the actual counts per vendor for historical and current month
findHistoricalOrderCount(0, 0, historical_orders, vendor)
findMonthOrderCount(0, 0, last_month_orders, vendor)

#outputing the resuts to a text file
for index in range(len(vendor)):
    if(vendor_historical_order_count[index]<milestone[0])&(vendor_historical_order_count[index]+ vendor_month_order_count[index]>milestone[0]):
        milestone1_vendors.append(vendor[index])
    elif(vendor_historical_order_count[index]<milestone[1])&(vendor_historical_order_count[index]+ vendor_month_order_count[index]>milestone[1]):
        milestone2_vendors.append(vendor[index])
    elif(vendor_historical_order_count[index]<milestone[2])&(vendor_historical_order_count[index]+ vendor_month_order_count[index]>milestone[2]):
        milestone3_vendors.append(vendor[index])
    elif(vendor_historical_order_count[index]<milestone[3])&(vendor_historical_order_count[index]+ vendor_month_order_count[index]>milestone[3]):
        milestone4_vendors.append(vendor[index])               
            
text_file = open("output.txt", "w")
text_file.write(
        "%s - %s \n %s:\n %s\n %s:\n %s\n %s:\n %s\n %s:\n %s" % (beginning_date, ending_date, milestone[0], milestone1_vendors, milestone[1], milestone2_vendors, milestone[2], milestone3_vendors, milestone[3], milestone4_vendors))
text_file.close()
print(datetime.now()-start)
"""
Created on Thu Jun 21 12:08:18 2018

@author: CATER2ME173
"""

