# Import Library
from pydub import AudioSegment
from pydub.playback import play

# Take in the audio file and outputing a different file
audio_in_file = "Cardinal Call 1_2.wav"
audio_out_file = "out_sine.wav"

# create 1 sec of silence audio segment
one_sec_segment = AudioSegment.silent(duration=1000)  #duration in milliseconds

#read wav file to an audio segment
song = AudioSegment.from_wav(audio_in_file)

#Add above two audio segments    
final_song = one_sec_segment + song

#Either save modified audio
final_song.export(audio_out_file, format="wav")

#Or Play modified audio
play(final_song)