#!/usr/bin/env python
# coding: utf-8

# In[54]:


#pip install groq
#pip install elevenlabs
#pip install python-dotenv


# In[55]:


from groq import Groq
import os
from dotenv import load_dotenv
from io import BytesIO
import requests
from elevenlabs.client import ElevenLabs
from elevenlabs import play
import speech_recognition as sr


# In[56]:


client = Groq( api_key="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",) # Get your own API key from: console.groq.com/home


# In[57]:


elevenlabs = ElevenLabs(api_key='sk_0d6dc1870a89c44687c0b4f7734bb11017508f03241e8f18',) # Get your own API key from: elevenlabs.io/app


# In[70]:


def getTextLLM(prompt):
    base_prompt="CONTEXT: You are a therapist who has 20+ years of experience in all kinds of therapy for example Cognitive behavioral therapy, Dialectical Behavior Therapy, Addiction therapy, grief counselling, child and youth therapy and family therapy. You are great at initiating conversations and making people feel comfortable. You are also great at storytelling, and use this in your therapy ONLY WHEN NECESSARY. You should also give them space to answer in between if they interrupt you. OUTPUT: The output will be fed to eleven labs for text to speech, avoid special characters BUT INCLUDE THEM IF THEY CHANGE THE MEANING OF THE SENTENCE. Make it sound like you are answering to your patient."
    full_prompt=base_prompt+" USER INPUT:"+prompt
    completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
      {
        "role": "user",
        "content":full_prompt
      }
    ],
    temperature=0.8,
    max_completion_tokens=1500,
    top_p=0.95,
    reasoning_effort="high",
    stream=True,
    stop=None
    )
    txtLLM = ""
    for chunk in completion:
        content = chunk.choices[0].delta.content or ""
        txtLLM += content
    return txtLLM


# In[59]:


def stt(local_audio_path):
    #local_audio_path = "yatharth.mp3"

    with open(local_audio_path, "rb") as f:
        audio_data = BytesIO(f.read())

    transcription = elevenlabs.speech_to_text.convert(
        file=audio_data,
        model_id="scribe_v1",
        tag_audio_events=True,
        language_code="eng",
        diarize=True,
    )
    return(transcription.text)


# In[62]:


def tts(txt):
    audio = elevenlabs.text_to_speech.convert(
    text=txt,
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
    )
    with open("output.mp3", "wb") as f:
        for chunk in audio:
            f.write(chunk)


# In[64]:


txt=stt("soumya_input.mp3")


# In[66]:


txt


# In[72]:


txtLLM=getTextLLM(txt)


# In[76]:


tts(txtLLM) #output will be saved in the local folder as output.mp3


# In[ ]:




