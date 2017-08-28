import quandl
import pandas as pd
import pickle

# Not necessary, I just do this so I do not show my API key.
api_key = open('quandlapikey.txt', 'r').read()


def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]


def grab_initial_state_data():
    states = state_list()

    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_" + str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df.rename(columns={'Value': str(abbv)}, inplace=True)
        print(query)
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    pickle_out = open('fiddy_states.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()


def grab_initial_state_data2():
    states = state_list()

    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_" + str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df.rename(columns={'Value': str(abbv)}, inplace=True)
        print(query)
        df = df.pct_change()
        print(df.head())
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    pickle_out = open('fiddy_states2.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()


def grab_initial_state_data3():
    states = state_list()

    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_" + str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df.rename(columns={'Value': str(abbv)}, inplace=True)
        df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100.0

        print(query)
        df = df.pct_change()
        print(df.head())
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    pickle_out = open('fiddy_states3.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()


# grab_initial_state_data()
# HPI_data = pd.read_pickle('fiddy_states.pickle')

# HPI_data['TX2'] = HPI_data['TX'] * 2
# print(HPI_data[['TX','TX2']].head())

import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')


#
# HPI_data.plot()
# plt.legend().remove()
# plt.show()


# grab_initial_state_data2()

# HPI_data2 = pd.read_pickle('fiddy_states2.pickle')
# HPI_data2.plot()
# plt.legend().remove()
# plt.show()

# grab_initial_state_data3()
# HPI_data3 = pd.read_pickle('fiddy_states3.pickle')
# HPI_data3.plot()
# plt.legend().remove()
# plt.show()

#
# def HPI_Benchmark():
#     df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
#     df.rename(columns={'Value': "United States"}, inplace=True)
#     df["United States"] = (df["United States"] - df["United States"][0]) / df["United States"][0] * 100.0
#     return df
#
#
# fig = plt.figure()
# ax1 = plt.subplot2grid((1, 1), (0, 0))
#
# HPI_data = pd.read_pickle('fiddy_states2.pickle')
# benchmark = HPI_Benchmark()
# HPI_data.plot(ax=ax1)
# benchmark.plot(color='k', ax=ax1, linewidth=10)
#
# plt.legend().remove()
# plt.show()

HPI_data = pd.read_pickle('fiddy_states3.pickle')
HPI_State_Correlation = HPI_data.corr()
print(HPI_State_Correlation)
print("-----")
print(HPI_State_Correlation.describe())

