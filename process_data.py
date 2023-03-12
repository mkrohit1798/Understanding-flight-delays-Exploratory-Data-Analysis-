import pandas as pd
import os
import numpy as np
import matplotlib as plt

dirname = 'data_raw'

headers = []

def filter_data():
    li = []
    for filename in os.listdir('./data_raw'):
        if not filename.endswith("asc"):
            continue
        if '2018' in filename or '2019' in filename or '2020' in filename or '2021' in filename:
            df = pd.read_csv('./data_raw/' + filename, index_col=None, header=None, sep='|', usecols=[0, 6, 7, 8, 10, 12, 20], names=["Airline", "Source", "Dest", "Date", "Scheduled_Depart_time", "Depart_time", "Delay"])
        else:
            df = pd.read_csv('./data_raw/' + filename, index_col=None, header=None, sep='|', usecols=[0, 2, 3, 4, 6, 8, 16], names=["Airline", "Source", "Dest", "Date", "Scheduled_Depart_time", "Depart_time", "Delay"])
        li.append(df)

    flight_data = pd.concat(li, axis=0, ignore_index=True)
    flight_data.to_csv('export_dataframe.csv', index = False, header=True)

# print(len(flight_data))
# #flight_data.rename(columns={'Date (MM/DD/YYYY)': 'Date', 'oldName2': 'newName2'}, inplace=True)
# flight_data['Date'] = flight_data['Date'].astype('datetime64[ns]')
# flight_data['Month'] = flight_data['Date'].dt.month
# flight_data['Week'] = flight_data['Date'].dt.isocalendar().week
#
# plt.rcParams['figure.figsize'] = [15, 5]
#
# fig, (ax1, ax2) = plt.subplots(1, 2)
#
# yearly_groupby = flight_data.groupby('Month')
# average_delay_per_month = yearly_groupby.agg(mean_delay=('Departure delay (Minutes)', 'mean'))
#
#
# ax1.bar(range(len(yearly_groupby.groups.keys())), height=average_delay_per_month['mean_delay'], width=0.8)
# plt.xlabel("Month of year")
# plt.ylabel("Average delay in minutes")
#
# weekly_groupby = flight_data.groupby('Week')
# average_delay_per_week = weekly_groupby.agg(mean_delay=('Departure delay (Minutes)', 'mean'))
# ax2.bar(range(len(weekly_groupby.groups.keys())), height=average_delay_per_week['mean_delay'], width=0.8)
# plt.xlabel("Week of year")
# plt.ylabel("Average delay in minutes")
#
# pd.set_option('max_columns', None)
#
# print(flight_data.head())
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def filter_src_airports():
    airports = ['ATL', 'DFW', 'DEN', 'ORD', 'LAX', 'CLT', 'LAS', 'PHX', 'MCO', 'SEA', 'MIA', 'IAH', 'JFK', 'FLL', 'SFO', 'EWR', 'MSP', 'DTW', 'BOS', 'PHL', 'STL', 'BWI', 'TPA', 'SAN', 'SLC', 'IAD', 'BNA', 'LGA', 'DAL', 'DCA', 'PDX']
    df = pd.read_csv('export_dataframe.csv', index_col=None, header=0)
    filtered_data = df.loc[df['Source'].isin(airports)]
    filtered_data.to_csv('filtered_dataframe.csv', index = False, header=True)
    print(len(filtered_data))


def preprocess():
    df = pd.read_csv('filtered_dataframe.csv', index_col=None, header=0, nrows=10000000)
    df = df[df['Delay'].apply(lambda x: RepresentsInt(str(x)))]
    df['Delay'] = df['Delay'].astype(int)

    df['Delay'] = np.where((df.Delay < 0), 0, df.Delay)
    df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d', errors='coerce')
    df = df.dropna(subset=['Date'])
    df['Scheduled_Depart_time'] = pd.to_datetime(df['Scheduled_Depart_time'], format='%H%M', errors='coerce')

    df = df.dropna(subset=['Scheduled_Depart_time'])
    df['Depart_time'] = pd.to_datetime(df['Depart_time'], format='%H%M', errors='coerce')
    df = df.dropna(subset=['Depart_time'])
    #print(df['Scheduled_Depart_time'].dtypes)
    #df['min_of_day'] = df['Scheduled_Depart_time'].hour * 60 + df['Scheduled_Depart_time'].dt.minute
    df['Depart_time_slot'] = pd.cut(df['Depart_time'], bins=8, labels=[0, 1, 2, 3, 4, 5, 6, 7])

    print(len(df))
    return df