from pytubefix import Search 
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
#start=time.time()
#In order for this to work you need to have your own spotify app , you can read more about this here https://spotipy.readthedocs.io/en/2.25.2/
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_CLIENT_ID_HERE",
                                               client_secret="YOUR SECRET ID HERE",
                                               redirect_uri="http://127.0.0.1:8000/callback",#OR SOME PORT LIKE 8000  
                                               scope="user-library-read"))


artistlist=[]
lista_me_url=[]
telikh_lista=[]
username = "YOUR USERNAME"

playlist="4d83xfvE0h7WgeidICZouH"
sp_playlist = sp.user_playlist_tracks(username, playlist_id=playlist)
tracks = sp_playlist['items']


def urlreturner(titlos):
    counter_entos=0
    result = Search(titlos)
    for video in result.videos:
        print("mpika",titlos)
        counter_entos=+1
        url=video.watch_url
        return str(url)
    print(f'esoterikos{counter_ektos},ejoterikos{counter_entos}')



def list_to_file_writer(filename,list_grapsimatos):
    with open(filename, 'w+') as f:
    
    # write elements of list
     for items in list_grapsimatos:
            f.write('%s\n' %items)
    
    print("File written successfully")
    f.close()   

def get_playlist_tracks_more_than_100_songs(username, playlist_id):
    print("i entered")
    results = sp.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:  #επομενα τραγουδια
        results = sp.next(results)
        tracks.extend(results['items'])
    results = tracks    

    playlist_tracks_id = []
    playlist_tracks_titles = []
    playlist_tracks_artists = []
    playlist_tracks_first_artists = []
    playlist_tracks_first_release_date = []
    playlist_tracks_popularity = []
    kostolista_tragoudia =[]
    kostolista_kalitexnes =[]
    lista_kallitexnes_tragoudia =[]

    for i in range(len(results)):
     #   print(i) # Counter
        
        playlist_tracks_id = results[i]['track']['id']
        playlist_tracks_titles = results[i]['track']['name']
        playlist_tracks_first_release_date = results[i]['track']['album']['release_date']
        playlist_tracks_popularity = results[i]['track']['popularity']

        artist_list = []
        try:    #travaei tragoudia profanws
            kostolista_tragoudia.append(playlist_tracks_titles)
        except:
            continue
        for artist in results[i]['track']['artists']: #τραβάει ονόματα καλλιτεχνών για λόγους ευκολίας τραβάει μόνο τον πρώτο , απλα βγάλε το break αμα τους θες ολους
            artist_list= artist['name']
            break
        playlist_tracks_artists = artist_list
        print(playlist_tracks_artists)
        try:
            kostolista_kalitexnes.append(playlist_tracks_artists)
        except:
            continue
        # features = sp.audio_features(playlist_tracks_id)
        # features_df = pd.DataFrame(data=features, columns=features[0].keys())
        # features_df['title'] = playlist_tracks_titles
        # features_df['all_artists'] = playlist_tracks_artists
        # features_df['popularity'] = playlist_tracks_popularity
        # features_df['release_date'] = playlist_tracks_first_release_date
        # features_df = features_df[['id', 'title', 'all_artists', 'popularity', 'release_date',
        #                           'danceability', 'energy', 'key', 'loudness',
            #                          'mode', 'acousticness', 'instrumentalness',
            #                         'liveness', 'valence', 'tempo',
            #                        'duration_ms', 'time_signature']]
        
    

    for i in range(len(kostolista_kalitexnes)):#μονο ο εγω ειμαι ικανος να κανω το ιδιο ηλιθιο λαθος δυο φορες
        telikh_lista.append(str(kostolista_kalitexnes[i])+"-"+str(kostolista_tragoudia[i]))
    
    for antikeimeno in telikh_lista:
        try:
            lista_me_url.append(urlreturner(antikeimeno))
            temp=str(lista_me_url[counter_ektos])
            #f.write(temp,"\n")
            counter_ektos=+1
        except:
            continue
    list_to_file_writer("lista_me_urlfinale.txt",lista_me_url)
    list_to_file_writer("teliko_arheiofinale.txt",telikh_lista)
    list_to_file_writer("kallitexnesfinale.txt",kostolista_kalitexnes)    
    list_to_file_writer("tragoudiafinale.txt",kostolista_tragoudia)    
    
        


    return 1

noumero=get_playlist_tracks_more_than_100_songs(username,playlist)
#end = time.time()
#print(f"Total runtime of the program is {end - start} seconds")
                                              
