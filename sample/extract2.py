#import moviepy.editor as mp
from pydub import AudioSegment

with open('__1fS7Avmso.en.vtt') as f:
    for _ in range(4):
        next(f)
    segment = 0
    for line in f:
        if(line.startswith('00:')):
            segment +=1
            #timestamps = [line.split()[0],line.split()[2]]
            print(line.split()[0],line.split()[2], segment)
        else:
            print(line)


audio = AudioSegment.from_wav("/Users/akash/Desktop/nlp/__1fS7Avmso.mp3")

start = ""
timestamps=[58]
for  idx,t in enumerate(timestamps):
    #break loop if at last element of list
    if idx == len(timestamps):
        break

    end = t * 1000 #pydub works in millisec
    print ("split at [ {}:{}] ms".format(start, end))
    audio_chunk=audio[start:end]
    audio_chunk.export( "audio_chunk_{}.wav".format(end), format="wav")

    start = end * 1000 


	


