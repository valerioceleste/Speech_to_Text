from pydub import AudioSegment


def wav_converter(mp3_path, wav_path, channels=1):

    try:
        sound = AudioSegment.from_file(mp3_path, format="mp3")
    except:
        sound = AudioSegment.from_file(mp3_path, format="mp4")
    finally:
        sound = sound.set_channels(channels)
        sound.export(wav_path, format="wav")
        print('...converting mp3 to wav.')
