
# coding: utf-8

# In[25]:


import speech_recognition as sr
import numpy as np
import os
import os
import speech_recognition as sr
from tqdm import tqdm


# In[31]:


# Load all audio files (divided in previous step)
files = sorted(os.listdir('C:\\Users\\MWars\\Desktop\\Untitled Folder\\parts\\'))

with open("C:\\Users\\MWars\\Desktop\\Untitled Folder\\api.json") as f:
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()


# In[39]:


all_text = []
i = 0

for f in tqdm(files):
    # Load audio files part by part
    name = 'C:\\Users\\MWars\\Desktop\\Untitled Folder\\parts\\' + f 
    
    with sr.AudioFile(name) as source:
        audio = r.record(source)
    
    # Transcribe audio file (I used Polish language)
    text = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS, language='pl-PL')
    # Add text to a list
    all_text.append(text)
    
    # This is important, because I save results every 5 steps in order API will cut me
    # (Google Speech API has requests limitation)
    i = i + 1
    if i%5 == 0: 
        print(name,"- current saved")
        with open("C:\\Users\\MWars\\Desktop\\Untitled Folder\\txt.txt", "w") as f:
                f.write(str(all_text))
                

