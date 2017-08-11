import quandl

# Not necessary, I just do this so I do not show my API key.
api_key = open('quandlapikey.txt','r').read()
print(api_key)

df = quandl.get('FMAC/HPI_TX',authtoken=api_key)

df.to_csv('HPI_TX.csv')
print(df.head())


print("********************************")
import pandas as pd
fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
print(fiddy_states[0])
print("********************************")


for abbv in fiddy_states[0][0][1:]:
    # print(abbv)
    print("FMAC/HPI_%s" % str(abbv))