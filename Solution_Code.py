""" ADD PACKAGE """

# If there isn't this package in your computer, please install to using below instruction.
#!pip install --upgrade pip
#!pip install dc_stat_think
#import dc_stat_think as dcst
#import itertools as it


""" IMPORT """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


""" GET DATA and FIRST CHECKING for null or duplicate variables"""

data_path="/home/mahmut/Documents/DataScience/trivago_remote_task/marketing_campaigns.csv"
data_campaign = pd.read_csv(data_path)

print(data_campaign)
type(data_campaign)

data_campaign = data_campaign.drop_duplicates()


""" DATA STATISTICS AND EDA (Explore data analysis with graph) """
# Data Statistics ~ The meaning of the campaign data

data_campaign.head()
data_campaign.info()
data_campaign.describe()

week = data_campaign['Week'].drop_duplicates()

#CDF (Cumulative Distribution Function)
def cdf(cdf_data1, cdf_data2, label1, label2, label3):
    plt.figure(1)
    
    if len(cdf_data1) > 0:
        len_data1 = len(cdf_data1)
        data_array1 = np.arange(0,len_data1)
        probability1 = data_array1/len_data1
        plt.plot(np.sort(cdf_data1), probability1, marker='.', linestyle='none')
        
    if len(cdf_data2) > 0:
        len_data2 = len(cdf_data2)
        data_array2 = np.arange(0,len_data2)
        probability2 = data_array2/len_data2
        plt.plot(np.sort(cdf_data2), probability2, marker='.', linestyle='none')
        
    plt.legend([label2, label3], loc=4)
    plt.xlabel(label1)
    plt.ylabel('probability')
    plt.title('CDF (Cumulative Distribution Function)')
    plt.show()

#EDA
def DataAnalyze(campaign_name):
    if campaign_name == 'Entire Market':
        campaign = data_campaign
        revenue = campaign.groupby('Week')['Revenue'].mean()
        visits  = campaign.groupby('Week')['Visits'].mean()
        cost    = campaign.groupby('Week')['Cost'].mean()
        profit  = ((revenue-cost) / revenue)
        cdf(profit, '', 'Profit_Entire_Market', '', '')
    else:
        campaign = data_campaign[(data_campaign.Campaign == campaign_name)]
        revenue = campaign['Revenue']
        visits  = campaign['Visits']
        cost    = campaign['Cost']
        profit  = ((revenue-cost) / revenue)
        cdf(profit, '', 'Profit_' + campaign_name + '_Campaign', '', '')
        
    plt.figure(2)
    plt.plot(week, revenue, 'g^', week, cost, 'rv', week, visits, 'bs') 
    plt.legend(['Revenue', 'Cost', 'Visits'], loc=4)
    plt.xlabel('Week')
    plt.ylabel('Revenue & Cost & Visits')
    plt.title('Analyze ' + campaign_name)
    plt.show()
    
    plt.figure(3)
    plt.plot(visits, revenue, 'r*')
    plt.xlabel('Visits')
    plt.ylabel('Revenue')
    plt.title('Quality of Traffic for ' + campaign_name)
    plt.show()
    
    plt.figure(4)
    plt.plot(cost, revenue, 'g^', cost, visits, 'bs') 
    plt.legend(['Revenue', 'Visits'], loc=4)
    plt.xlabel('Cost')
    plt.ylabel('Revenue & Visits')
    plt.title('ROAD MAP ' + campaign_name)
    plt.show()
    


""" a) MARKET AND CAMPAIGN ANALYZE, b) QUALITY OF TRAFFIC IN TERMS OF REVENUE PER VISITOR,
    c) DRAW A ROAD MAP FOR RESPONSIBLE BUSINESS DEVELOPER"""
    
DataAnalyze('Entire Market')
DataAnalyze('Aldebaran')
DataAnalyze('Bartledan')
DataAnalyze('Cottington')







""" *****----***---*****----*----******-- """
""" TASK-2 """



""" GET DATA and FIRST CHECKING for null or duplicate variables"""

data_path="/home/mahmut/Documents/DataScience/trivago_remote_task/session_data.csv"
data_session = pd.read_csv(data_path)

print(data_session)
type(data_session)


""" DATA STATISTICS AND EDA (Explore data analysis with graph) """
# Data Statistics ~ The meaning of the campaign data

data_session.head()
data_session.info()
data_session.describe()

data_session['time_interval'] = (pd.to_datetime(data_session.session_end_text) - pd.to_datetime(data_session.session_start_text)).astype('timedelta64[m]')
data_session[data_session.time_interval < 0] = ((24*60) + data_session[(data_session['time_interval'] < 0)][['time_interval']])

time_interval = data_session['time_interval']
clickouts = data_session['clickouts']
booking = data_session['booking']

# you spend alot ot time on the web site but you can a little bit click
plt.figure(5)
plt.plot(time_interval, clickouts, 'g^')
plt.xlabel('time interval')
plt.ylabel('clickouts')
plt.title('relationship between time interval and clickouts')
plt.show()

plt.figure(6)
plt.plot(time_interval, booking, 'r*')
plt.xlabel('time_interval')
plt.ylabel('booking')
plt.title('relationship between time interval and booking')
plt.show()

# you can click much times but you can not booking
plt.figure(7)
plt.plot(booking, clickouts, 'g^')
plt.xlabel('booking')
plt.ylabel('clickouts')
plt.title('relationship between booking and clickouts')
plt.show()

plt.figure(8)
plt.plot(time_interval, booking, 'r*', time_interval, clickouts, 'g^')
plt.legend(['time_interval', 'clickouts'], loc=1)
plt.xlabel('time_interval')
plt.ylabel('booking & clickouts')
plt.title('relationship between booking, time interval and clickouts')
plt.show()


book_click_c = np.corrcoef(booking, clickouts)

book_interval_time_c = np.corrcoef(booking, data_session['time_interval'])