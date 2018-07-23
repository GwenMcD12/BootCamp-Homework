
# coding: utf-8

# ### Heroes Of Pymoli Data Analysis
# * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# 
# * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
# -----

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd
import numpy as np
import os
import csv

# Raw data file
file_to_load = "resources/purchase_data.csv"

# Read purchasing file and store into pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()


# ## Player Count

# * Display the total number of players
# 

# In[2]:


player_count = len(purchase_data['Purchase ID'].unique())
player_count


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[3]:


item_count = len(purchase_data['Item ID'].unique())
item_count

#item_count_formatted ='${:,.2f}'.format(item_count)

avg_purchase = round(purchase_data['Price'].mean(), 2)
avg_purchase

#avg_purhase_formatted = '${:,.2f}'.format(avg_purchase) 

total_revenue = round(purchase_data['Price'].sum(), 2)
total_revenue

#total_revenue_formatted ='${:,.2f}'.format(total_revenue)

rows = len(purchase_data.index)


purchasing_analysis_df = pd.DataFrame({"Total Revenue":[total_revenue],
                                       "Number of Purchases":[rows],
                                       "Average Price":[avg_purchase],
                                       "Number of Unique Items":[item_count]})



purchasing_analysis_df = purchasing_analysis_df[['Number of Unique Items', 
                                                 'Average Price', 
                                                 'Number of Purchases', 
                                                 'Total Revenue' ]]
purchasing_analysis_df


# ## Gender Demographics

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[4]:





# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, etc. by gender
# 
# 
# * For normalized purchasing, divide total purchase value by purchase count, by gender
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[5]:





# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[6]:


# Establish bins for ages
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]


# Bin the Age column

purchase_data["Age Group"] = pd.cut(purchase_data["Age"], age_bins, labels = age_labels)


grouped_age_df = purchase_data.groupby("Age Group")

age_nun = grouped_age_df["SN"].nunique()

age_bin_percentages = [((member/player_count)*100) for member in age_nun]
age_bin_percentages = ['%.2f' % member for member in age_bin_percentages ]

age_bin_counts = [age_nun[member] for member in age_labels]

age_demo_dict = {"Ages": age_labels,
                 "Percentage of Players": age_bin_percentages,
                 "Total Count": age_bin_counts
                }

age_demo_df = pd.DataFrame(age_demo_dict)


age_demo_df = age_demo_df.set_index("Ages")

age_demo_df = age_demo_df[["Percentage of Players","Total Count"]]

age_demo_df


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, etc. in the table below
# 
# 
# * Calculate Normalized Purchasing
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[7]:


age_purchases_counts = grouped_age_df["Age Group"].count()

average_age_purchase = grouped_age_df["Price"].mean()

total_age_purchases = grouped_age_df["Price"].sum()

normalized_age_purchases = [t/g for t,g in zip(total_age_purchases, age_bin_counts)]

average_age_purchase = ["$%.2f" % member for member in average_age_purchase]
total_age_purchases = ["$%.2f" % member for member in total_age_purchases]
normalized_age_purchases = ["$%.2f" % member for member in normalized_age_purchases]


age_purchases_dict = {"Ages": age_labels,
                         "Purchase Count": age_purchases_counts,
                         "Average Purchase Price": average_age_purchase,
                         "Total Purchase Value": total_age_purchases,
                         "Normalized Totals": normalized_age_purchases
                        }

age_purchases_df = pd.DataFrame(age_purchases_dict)


age_purchases_df = age_purchases_df[["Purchase Count",
                                     "Average Purchase Price",
                                     "Total Purchase Value",
                                     "Normalized Totals"]]

age_purchases_df


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[8]:


# Establish bins for ages
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]



##This is where Gwen stops :( I do not have any more time and wanted to try to concentrate on formulas working instead of just putting them in


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[9]:





# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[10]:




