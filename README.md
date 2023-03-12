# Understanding-flight-delays-Exploratory-Data-Analysis-
**Objective**
The objective of this project is two-fold. First, we aim to analyse the factors that lead to delay in passenger
aircraft. As a part of this analysis, we will also investigate the effect a flight delay at a particular date and time
has on subsequent delays, and under what conditions a flight delay can cause a chain reaction of delays that
follows.
As the second phase of the project, we will build a model that predicts the arrival delay for a given scheduled
flight. Through the analysis that we will perform in the first phase of the project, we aim to create a rich set of
features that will help us predict flight delays. We also hope to attain valuable insights from the analysis, which
will help us in picking the kind of prediction model that will be appropriate for our task.

**Datasets**
1. Detailed Statistics Departures dataset, https://www.transtats.bts.gov/ONTIME/Departures.aspx
2. OpenSky Aircraft Database, https://opensky-network.org/datasets/metadata/
3. Iowa Environmental Mesonet https://mesonet.agron.iastate.edu/

**Data Analysis**
Here we tried plotting routes on the US map for different delay causes. In comparison to the lighter coloured
routes, lines drawn with a stronger hue(shade) depict routes with larger percentages of delays.

**Weather Delays**
![image](https://user-images.githubusercontent.com/125203016/224555580-c65e4e4f-82b2-47bd-a03f-27f60e3ed791.png)

Weather delays as we can see are limited to certain routes with atypical or extreme weather conditions.
According to the Federal Aviation Administration, most of the delays in winter are due to surface winds, low
ceiling and low visibility, whereas during summer the majority of delays is attributable to convective weather,
low ceiling and associated low visibility (Federal Aviation Administration, 2017). In our analysis, we used
precipitation, wind speed, temperature and visibility as a proxy for these conditions.

**NAS Delays**
![image](https://user-images.githubusercontent.com/125203016/224555599-a49d1544-f36f-44b4-a98b-3f0280b44c0c.png)

Delays and cancellations attributable to the national aviation system refer to a broad set of conditions(shown
above). Since the majority component(about 45%) of NAS delays attribute to non-extreme weather conditions,
resulting in similar delay routes and hotspots as compared to the weather delay graph.

**Airline and Aircraft Delays**

![image](https://user-images.githubusercontent.com/125203016/224555633-1c73935c-f65c-480b-8aa1-35999513f735.png)

Airline delay is more distributed across the country and is not dependent on geographical location. Upon
analysis we found aircraft age and model to be important features that could affect the performance of a certain
aircraft belonging to an airline.

**Additional Delay Causes**
![image](https://user-images.githubusercontent.com/125203016/224555667-6a204dcb-0e42-4a7b-ab06-2e6e6a9c1640.png)
![image](https://user-images.githubusercontent.com/125203016/224555675-92c4c6e1-91fc-41f8-bf09-6c59de1f99b4.png)

We discovered that time-based features can also be crucial elements in forecasting flight delays after further
investigation. On weekends and holidays, people prefer to travel more, causing traffic congestion and airport
operations challenges, resulting in delays. We also discovered that the busiest airports had a greater likelihood
of flight delays. Most of the airports that cause delays include JFK, Chicago, ATL, Miami, DNV, Austin, LA, and
SF.

**Implementation and Validation**

**Feature Selection**

Data collection and cleaning took the majority of our time as Weather and
Aircraft metadata was not readily available to use on the internet.

![image](https://user-images.githubusercontent.com/125203016/224555979-a25914c0-67d5-4f77-9ac3-a48468e81700.png)

Based on the features selected we used sklearn to get the importance of the overall classification. As
expected, weather-based features play an important role while determining the delays across the flights. This
is also supported by the analysis done by BTS which shows that almost 30% of the flights are delayed due to
weather-based reasons.

**Regression**

We used the dataset described above to train regression models that predict the arrival delay of flights. This
regression was done on a small subset of flight data, using 500000 rows for training and validation. We got a
score that was greatly lower than what we expected, with our best performing model being Random Forest
with an R2 Score of 0.0761.

We attribute this to the fact that our dataset was small and restricted to only one year of flight delay data(flight
delays in 2015). By training our model on multiple years of flight delay data, we hope that it will be better able
to understand and predict flight delays.

