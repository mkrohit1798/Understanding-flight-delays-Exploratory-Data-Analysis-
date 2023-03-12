import process_data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from scipy import stats
import statsmodels.api as sm


processed_data = process_data.preprocess()
one_hot = pd.get_dummies(processed_data.Depart_time_slot, prefix='Time_slot_')
processed_data = processed_data.join(one_hot)

one_hot_airline = pd.get_dummies(processed_data.Airline, prefix='Airline_')
processed_data = processed_data.join(one_hot_airline)
processed_data['Delay_bool'] = np.minimum(processed_data['Delay'], 1)

processed_data = processed_data[(np.abs(stats.zscore(processed_data['Delay'])) < 2.5)]

print(len(processed_data))
# slot_groupby = processed_data.groupby('Depart_time_slot')

# average_delay_per_time_slot = slot_groupby.mean()
# max_delay_per_time_slot = slot_groupby['Delay'].max()
#
# #delayed_flights = processed_data[processed_data[]]
# count_delay_per_time_slot = slot_groupby['Delay'].count()
# count_delay_rate = slot_groupby['Delay_bool'].mean()

# average_delay_per_time_slot = average_delay_per_time_slot.reset_index()
# count_delay_per_time_slot = count_delay_per_time_slot.reset_index()
# count_delay_rate = count_delay_rate.reset_index()


# fig, (ax1, ax2) = plt.subplots(1, 2)
#
# ax1.bar(range(len(count_delay_rate)), height=count_delay_rate['Delay_bool'], width=0.8, color='grey', tick_label=['00-03', '03-06', '06-09', '09-12', '12-15', '15-18', '18-21', '21-24'])
# ax1.set_title("Time slot (Hour of day)")
# ax1.set_ylabel("Fraction of flights delayed")
# # ax1.show()
#
# ax2.bar(range(len(average_delay_per_time_slot)), height=average_delay_per_time_slot['Delay'], width=0.8, color='black', tick_label=['00-03', '03-06', '06-09', '09-12', '12-15', '15-18', '18-21', '21-24'])
# ax2.set_title("Time slot (Hour of day)")
# ax2.set_ylabel("Average delay in minutes")
# plt.show()


# airline_groupby = processed_data.groupby('Airline')

# average_delay_per_time_slot = airline_groupby.mean()
# max_delay_per_time_slot = airline_groupby['Delay'].max()

# delayed_flights = processed_data[processed_data[]]
# count_delay_per_time_slot = airline_groupby['Delay_bool'].mean()
#
# average_delay_per_time_slot = average_delay_per_time_slot.reset_index()
# count_delay_per_time_slot = count_delay_per_time_slot.reset_index()
# print(average_delay_per_time_slot)

# fig, (ax1, ax2) = plt.subplots(1, 2)

# ax1.bar(range(len(count_delay_per_time_slot)), height=count_delay_per_time_slot['Delay_bool'], width=0.8)
# ax2.bar(range(len(average_delay_per_time_slot)), height=average_delay_per_time_slot['Delay'], width=0.8)
# plt.xlabel("Time slot")
# plt.ylabel("Average delay in minutes")
# plt.show()


processed_data['Week'] = processed_data['Date'].dt.week
week_groupby = processed_data.groupby('Week')
average_delay_per_week = week_groupby.mean()
average_delay_per_week = average_delay_per_week.reset_index()
average_delay_per_week['Week_delay_z'] = np.floor(stats.zscore(average_delay_per_week['Delay']))
processed_data = processed_data.join(average_delay_per_week[['Week', 'Week_delay_z']].set_index('Week'), on='Week')
one_hot_week = pd.get_dummies(processed_data.Week_delay_z, prefix='Week_delay_z_')
processed_data = processed_data.join(one_hot_week)



airport_groupby = processed_data.groupby('Source')
average_delay_per_airport = airport_groupby.mean()
average_delay_per_airport = average_delay_per_airport.reset_index()
average_delay_per_airport['Airport_delay'] = average_delay_per_airport['Delay']
#average_delay_per_airport['Week_delay_z'] = np.floor(stats.zscore(average_delay_per_week['Delay']))
processed_data = processed_data.join(average_delay_per_airport[['Source', 'Airport_delay']].set_index('Source'), on='Source')
#one_hot_week = pd.get_dummies(processed_data.Week_delay_z, prefix='Week_delay_z_')
#processed_data = processed_data.join(one_hot_week)

#processed_data['Week_z'] = np.abs(stats.zscore(processed_data['Delay']))


print(processed_data.head())
print(average_delay_per_week.head())
#processed_data['Week_cut'] = pd.cut(processed_data['Week'], bins=26, labels=list(range(0, 26)))
#one_hot_week = pd.get_dummies(processed_data.Week_cut, prefix='Week_')
#processed_data = processed_data.join(one_hot_week)



#
# week_groupby = processed_data.groupby('Week_cut')
# average_delay_per_week = week_groupby.mean()
# average_delay_per_week = average_delay_per_week.reset_index()
#
# plt.bar(range(len(average_delay_per_week)), height=average_delay_per_week['Delay'], width=0.8)
# plt.xlabel("Week No.")
# plt.ylabel("Average delay for week (minutes)")
# plt.show()


# airline_groupby = processed_data.groupby('Airline')
# average_delay_per_airline = airline_groupby.mean()
# average_delay_per_airline = average_delay_per_airline.reset_index()
# average_delay_per_airline = average_delay_per_airline.sort_values(by=['Delay'])
# fig, (ax1) = plt.subplots(1, 1)
#
# ax1.barh(average_delay_per_airline['Airline'], average_delay_per_airline['Delay'], align='center')
# ax1.set_yticks(average_delay_per_airline['Airline'])
# ax1.set_yticklabels(average_delay_per_airline['Airline'])
# ax1.invert_yaxis()  # labels read top-to-bottom
# ax1.set_xlabel('Average Delay')
# ax1.set_title('Average delays by airline')

# plt.show()



def linear_regression(processed_data):
    y = processed_data['Delay']
    x = processed_data.drop(columns=['Delay', 'Airline', 'Source', 'Dest', 'Date', 'Scheduled_Depart_time', 'Depart_time', 'Depart_time_slot', 'Week', 'Delay_bool', 'Week_delay_z'], axis=1)
    print(x.head())
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    LR = LinearRegression()

    normal_model = sm.GLM(x_train, y_train)

    # fitting the training data
    LR.fit(x_train, y_train)
    y_prediction = LR.predict(x_test)
    mse = mean_squared_error(y_test, y_prediction)
    y_pred_avg = np.full(len(y_prediction), 1, processed_data['Delay'].mean())
    mse_avg = mean_squared_error(y_test, y_pred_avg)
    plt.scatter(np.arange(100), y_prediction[0:100])
    plt.scatter(np.arange(100), y_test[0:100])
    plt.show()
    print(mse, mse_avg)

data_sample = processed_data.sample(frac=0.5, replace=False, random_state=1)

linear_regression(data_sample)