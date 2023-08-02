# Load lib
from MoeGoe import MoeTTS

# Load tts model
model = MoeTTS('model/1164_epochs.pth', 
                   'model/config.json')

# Generate wav file
text = '이것은 테스트 문장입니다.'
model.wav(text)


# You can change speaker and path
print(model.speakers) ## print list of speakers

model.wav(text=text, speaker_id=4, filepath='./demo.wav')


# You can receive the data as array format
data = model.main(text, 2) # Numpy array

## And you can play it directly
import simpleaudio as sa
sampling_rate =  model.hps_ms.data.sampling_rate

sa_obj = sa.play_buffer(data, 1, 4, sampling_rate)
sa_obj.wait_done()