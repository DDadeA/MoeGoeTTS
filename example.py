# Load lib
import tts

# Load tts model
model = tts.MoeTTS('model/1164_epochs.pth', 
          'model/config.json')

# Generate wav file
model.wav('이것은 테스트 문장입니다.')

# You can change speaker and path
## list of speakers
print(model.speakers) 

model.wav(text='이것은 테스트 문장입니다.', speaker_id=4, filepath='./demo.wav')


# You can receive the data as array format
data = model.main('이것은 테스트 문장입니다.', 2) # Numpy array

## And you can play it directly
import simpleaudio as sa
sampling_rate =  model.hps_ms.data.sampling_rate

sa_obj = sa.play_buffer(data, 1, 4, sampling_rate)
sa_obj.wait_done()