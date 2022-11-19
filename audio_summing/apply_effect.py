import soundfile as sf
import numpy as np

# Funzione che replica i dati audio del filtro finchè non raggiunge una durata tale da ricoprire tutta la canzone.
def extends_filter(filter, max_shape):
    extended_filter = filter
    while(extended_filter.shape[0] < max_shape[0]):
        extended_filter = np.concatenate((extended_filter, filter))
    
    return extended_filter


song_path = "../tracks/10 - Fire In Cairo.flac"
filter_path = "../tracks/rain.flac"

song_data, song_sample_rate = sf.read(song_path)
filter_data, filter_sample_rate = sf.read(filter_path)

if song_data.shape[0] > filter_data.shape[0]:
    # Allineo la durata del filtro con quella della canzone
    filter_data = extends_filter(filter_data, song_data.shape)

# Sommo i dati audio delle due tracce
new_song = song_data + filter_data[:len(song_data)]

# Creo il file flac della canzone con l'effetto
sf.write("Fire In Cairo - with effect.flac", data=(new_song), samplerate=song_sample_rate, format='flac')

