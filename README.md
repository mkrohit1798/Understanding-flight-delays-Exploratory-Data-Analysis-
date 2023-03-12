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
![image](https://user-images.githubusercontent.com/125203016/224555546-f6d951e9-755e-4cf8-ba37-1470963d3ca2.png)

Weather delays as we can see are limited to certain routes with atypical or extreme weather conditions.
According to the Federal Aviation Administration, most of the delays in winter are due to surface winds, low
ceiling and low visibility, whereas during summer the majority of delays is attributable to convective weather,
low ceiling and associated low visibility (Federal Aviation Administration, 2017). In our analysis, we used
precipitation, wind speed, temperature and visibility as a proxy for these conditions.

**NAS Delays**
![image](https://user-images.githubusercontent.com/125203016/224555485-cf20c944-6649-463f-8072-3c81ee145748.png)
Delays and cancellations attributable to the national aviation system refer to a broad set of conditions(shown
above). Since the majority component(about 45%) of NAS delays attribute to non-extreme weather conditions,
resulting in similar delay routes and hotspots as compared to the weather delay graph.
