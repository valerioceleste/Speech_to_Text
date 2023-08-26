# %%
from pydub import AudioSegment

# %%
def mp3_to_wav(mp3_path, wav_path):
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav")

# Provide paths for input MP3 and output WAV files
mp3_file_path = "input.mp3"
wav_file_path = "output.wav"

mp3_to_wav(mp3_file_path, wav_file_path)