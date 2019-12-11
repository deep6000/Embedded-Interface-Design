``  11111111111 #!/usr/bin/python3

import pyaudio
import wave
import boto3
from time import sleep
import requests

bucket_wave="buckwave"
region="us-east-1"
audioip= "test1.wav"

form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 44100 # 44.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
record_secs = 3 # seconds to record
dev_index = 2 # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'test1.wav' # name of .wav file

audio = pyaudio.PyAudio() # create pyaudio instantiation

# create pyaudio stream
stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                    input_device_index = dev_index,input = True, \
                    frames_per_buffer=chunk)
print("recording")
frames = []

# loop through stream and append audio chunks to frame array
for ii in range(0,int((samp_rate/chunk)*record_secs)):
    data = stream.read(chunk,exception_on_overflow = False)
    frames.append(data)

print("finished recording")

# stop the stream, close it, and terminate the pyaudio instantiation
stream.stop_stream()
stream.close()
audio.terminate()

# save the audio frames as .wav file
wavefile = wave.open(wav_output_filename,'wb')
wavefile.setnchannels(chans)
wavefile.setsampwidth(audio.get_sample_size(form_1))
wavefile.setframerate(samp_rate)
wavefile.writeframes(b''.join(frames))
wavefile.close()

print("Connecting to S3 bucket")
S3 = boto3.client('s3')
S3.upload_file(audioip,bucket,audioip) 

transcribe = boto3.client('transcribe',region)
job_name = "myjob"
job_uri = "s3://buckwave/test1.wav"
transcribe.delete_transcription_job(TranscriptionJobName=job_name)
transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    LanguageCode='en-US',
    MediaFormat= "wav",
    Media= {
        "MediaFileUri": job_uri
    }
) 
while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Not ready yet...")
    sleep(5)
    
myurl = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
#print(myurl) 
Text_Data = (requests.get(myurl).json())['results']['transcripts'][0]['transcript']
print(Text_Data)




'''
		#The following code comes from markjay4k as referenced below
		p=pyaudio.PyAudio()

		#input stream setup
		stream=p.open(format = pyaudio.paInt16,rate=RATE,channels=1, input_device_index = 2, input=True, frames_per_buffer=chunk)

		#the code below is from the pyAudio library documentation referenced below
		#output stream setup
		player=p.open(format = pyaudio.paInt16,rate=RATE,channels=1, output=True, frames_per_buffer=chunk)

		while True:            #Used to continuously stream audio
			 data=np.fromstring(stream.read(chunk,exception_on_overflow = False),dtype=np.int16)
			 player.write(data,chunk)
			
		#closes streams
		stream .stop_stream()
		stream.close()
		p.terminate
		'''
