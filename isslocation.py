# Using Pandas and Plotly 
# Get current location as json
# then plot the location of the international space station

import pandas as pd
import plotly.express as px


# The data payload has a timestamp and an iss_position object with the latitude and longitude.
url = "http://api.open-notify.org/iss-now.json"

df = pd.read_json(url)

print(df)
#            iss_position  message           timestamp
# latitude        25.4802  success 2021-02-27 08:20:53
# longitude      -94.4389  success 2021-02-27 08:20:53

df['latitude'] = df.loc['latitude', 'iss_position']
df['longitude'] = df.loc['longitude', 'iss_position']
df.reset_index(inplace=True)

print(df)
#        index  iss_position  message           timestamp  latitude  longitude
# 0   latitude       25.4802  success 2021-02-27 08:20:53   25.4802   -94.4389
# 1  longitude      -94.4389  success 2021-02-27 08:20:53   25.4802   -94.4389

df = df.drop(['index', 'message'], axis=1)

print(df)
#    iss_position           timestamp  latitude  longitude
# 0       29.5969 2021-02-27 08:22:22   29.5969    -90.257
# 1      -90.2570 2021-02-27 08:22:22   29.5969    -90.257

fig = px.scatter_geo(df, lat='latitude', lon='longitude')

fig.show()
