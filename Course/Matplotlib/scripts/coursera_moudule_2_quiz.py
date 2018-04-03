# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to Preview the Grading for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# An NOAA dataset has been stored in the file data/C2A2_data/BinnedCsvs_d400/b091d88a3b4e7d3c9707df0e1cd8e7d5be82221e8f40485f1464c1ae.csv. The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) Daily Global Historical Climatology Network (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
# Each row in the assignment datafile corresponds to a single observation.
# The following variables are provided to you:
# id : station identification code
# date : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# element : indicator of element type
# TMAX : Maximum temperature (tenths of degrees C)
# TMIN : Minimum temperature (tenths of degrees C)
# value : data value for element (tenths of degrees C)
# For this assignment, you must:
# Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
# Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
# Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
# Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
# The data you have been given is near Tampa, Florida, United States, and the stations the data comes from are shown on the map below.

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]


    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()
    print(station_locations_by_hash['LONGITUDE'])

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(400,'b091d88a3b4e7d3c9707df0e1cd8e7d5be82221e8f40485f1464c1ae')

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd
import numpy as np
%matplotlib notebook

def line_polt_temp(binsize, hashid):
    df = pd.read_csv('data/C2A2_data/BinnedCsvs_d{}/{}.csv'.format(binsize,hashid))
    df_0514, df_2015 = clean_data(df)

    df_0514 = (df_0514.groupby(df_0514['Month_Day'])
               .agg({'TMAX':'max','TMIN':'min'})
               .rename(columns={'TMAX': 'Max', 'TMIN': 'Min'}))
    df_2015 = (df_2015.groupby(df_2015['Month_Day'])
               .agg({'TMAX':'max','TMIN':'min'})
               .rename(columns={'TMAX': 'Max', 'TMIN': 'Min'}))
    df_2015['Break_Max'] = df_2015[df_2015['Max'] > df_0514['Max']]['Max']
    df_2015['Break_Min'] = df_2015[df_2015['Min'] < df_0514['Min']]['Min']

    df_0514.plot(kind ='line',linewidth=0.25, alpha = 0.5)

    plt.gca().fill_between(range(len(df_0514.index)),
                       df_0514['Max'].tolist(), df_0514['Min'].tolist(),
                       facecolor='grey',
                       alpha=0.1)
    x = plt.gca().xaxis
    plt.gca().set_title('Temperature(°C) Record Breaks In 2015 Compared To 2005-2014 Records', y=1.05)
    plt.gca().set_ylabel('Temperature'),
    for item in x.get_ticklabels():
        item.set_rotation(45)
    plt.tick_params(top='off', bottom='off',
                left='off', right='off', labelbottom='on')
    plt.subplots_adjust(bottom=0.25)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)


def clean_data(df):
    df['Month_Day'] = df['Date'].map(lambda x: x.split('-')[1] + '-' + x.split('-')[2])
    df = df[~(df['Month_Day'] == '02-29')]
    df['Data_Value'] = df['Data_Value'].map(lambda x: x / 10)
    df = df.merge(df.pivot(columns = 'Element', values = 'Data_Value'), right_index = True,left_index = True)
    df_10 = df[df['Date'] < '2015-01-01']
    df_1 = df[df['Date'] >= '2015-01-01']

    return df_10, df_1


line_polt_temp(400,'b091d88a3b4e7d3c9707df0e1cd8e7d5be82221e8f40485f1464c1ae')
