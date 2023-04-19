import os
from pydub import AudioSegment
import wave

def correct_preprocess_audio(audio,speed=1.0):
    audio_with_altered_frame_rate = audio._spawn(audio.raw_data,overrides={"frame_rate": int(audio.frame_rate * speed)})
    print('nframe', audio_with_altered_frame_rate.frame_count())
    new_frame_audio = audio_with_altered_frame_rate.set_frame_rate(audio.frame_rate)
    print('nframe2', new_frame_audio.frame_count())
    return new_frame_audio


def get_audio(directory):
    for each_file in os.listdir(directory):
        if each_file.endswith(".wav"):
            audio = AudioSegment.from_wav(directory + each_file)
            print('Original:')
            print(audio.duration_seconds)
            print(audio.frame_rate)
            print(audio.frame_count())
            print()
            new_audio = correct_preprocess_audio(audio,audio.duration_seconds)
            print('New:')
            print(new_audio.duration_seconds)
            print(new_audio.frame_rate)
            print(new_audio.frame_count())
            print()
        
            new_audio.export(each_file,format="wav")
            #print('output',new_audio)
    return new_audio