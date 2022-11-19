# Funzione che ritorna i bytes che costituiscono il file flac
def read_flac_song(song_path):
    song_file = open(song_path, 'rb')
    song_bytes = song_file.read()
    song_file.close()

    return song_bytes

# Funzione che converte un blocco di bytes in una stringa di bit
def bytes_to_bits(bytes_block):
    bits = ''
    for byte in bytes_block:
        bits += format(byte, '08b') # Ogni byte viene convertito il 8 bit
    return bits

# Funzione che estrapola il sample rate del file flac in Hz
def get_sample_rate(song_bytes):
    # sample rate è un blocco di 20 bit che inizia dopo 144 bit
    SAMPLE_RATE_START = 18 # 144 bit = 18 byte
    SAMPLE_RATE_END = 21 # 164 bit = 21 byte

    sample_rate_block = song_bytes[SAMPLE_RATE_START: SAMPLE_RATE_END] # Prendo i 3 bytes che contengono il sample rate
    bits = bytes_to_bits(sample_rate_block) # Li converto in 24 bit 
    return int(bits[:20], 2) # Rimuovo i 4 bit in più e converto il valore binario in decimale


song_bytes = read_flac_song('../tracks/10 - Fire In Cairo.flac')
sample_rate = get_sample_rate(song_bytes)
print(f'Sample rate: {sample_rate} Hz')