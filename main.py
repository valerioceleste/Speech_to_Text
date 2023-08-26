#%%
from Tools.mp3_to_wav import wav_converter
from Tools.YouTube_to_mp3 import YouTubeURL_converter
#%%
URL = 'https://www.youtube.com/watch?v=ycOBZZeVeAc&list=PLPNW_gerXa4Pc8S2qoUQc5e8Ir97RLuVW&index=40'
filepath = '../../Audio'
#%%
#YouTubeURL_converter(URL,filepath)
mp3_file_path(URL,filepath)
#%%
# Provide paths for input MP3 and output WAV files
mp3_file_path = "../Audio/long_audio.mp3"
wav_file_path = "../Audio/output.wav"

wav_converter(mp3_file_path, wav_file_path, channels=1)