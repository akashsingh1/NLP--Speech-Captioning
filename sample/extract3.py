
import moviepy.editor

video = moviepy.editor.VideoFileClip("/Users/akash/Desktop/nlp/__1fS7Avmso.mov")

audio = video.audio

# Replace the parameter with the location along with filename
audio.write_audiofile("/Users/akash/Desktop/nlp/__1fS7Avmso.wav")