from mp3_to_wav import wav_converter

# Provide paths for input MP3 and output WAV files
mp3_file_path = "../Audio/long_audio.mp3"
wav_file_path = "../Audio/output.wav"

wav_converter(mp3_file_path, wav_file_path, channels=1)