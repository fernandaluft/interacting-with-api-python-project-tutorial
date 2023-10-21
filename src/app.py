### Interacting with Spotify's API ###

# Imports
from dotenv import load_dotenv
load_dotenv()
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# Connection with Spotify
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# Getting the top 10 tracks from U2 with artist ID obtained in Spotify website
tracks = sp.artist_top_tracks(artist_id='51Blml2LZPmy7TTiAg47vQ')

# Converting data to dataframe
df = pd.DataFrame(columns=['Songs', 'Duration', 'Popularity'])
for i in range(len(tracks['tracks'])):
    df = df.append({'Songs':tracks['tracks'][i]['name'], 
                    'Duration':tracks['tracks'][i]['duration_ms'], 
                    'Popularity':tracks['tracks'][i]['popularity']}, ignore_index=True)

# Converting duration of songs to minutes
for item in df['Duration']:
    df['Duration'].replace(item, ((item/(1000*60))%60), inplace=True)

# Sorting values by popularity
df = df.sort_values(by='Popularity')
df.head(3)

# Scatter plot of the correlation between duration and popularity of songs
sns.scatterplot(df, x='Popularity', y='Duration')
plt.title('Correlation between Popularity and Duration of a Song')
plt.xlabel('Popularity')
plt.ylabel('Duration')
plt.tight_layout()
plt.show()

# As seen on the scatter plot pltted on explore.ipynb file, there is no correlation between duration and popularity of top ten
# U2 songs on Spotify.