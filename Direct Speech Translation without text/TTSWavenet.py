#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 14:29:56 2021

@author: limbu
"""

#Using Google Cloud Console (Wavenet) Convert text to Speech using Synthetic voice

#Install Google Cloud Language API using below code
#!pip install --user  --upgrade google-cloud-language
#!pip install --upgrade google-cloud-texttospeech



Proj = "catdogcnn-313bcb1bdec2.json"             #Download the API key in json format for the project from Google Cloud Console

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = Proj

import os
from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Build the voice request, select the language code ("en-US") 
# ****** the NAME
# and the ssml voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
language_code = 'en-US',
name = 'en-US-Wavenet-C',
ssml_gender = texttospeech.SsmlVoiceGender.MALE)

# Select the type of audio file you want returned (Mp3 Here)
# speaking_rate is the speed of the voice
audio_config = texttospeech.AudioConfig(
audio_encoding=texttospeech.AudioEncoding.MP3,
speaking_rate = 1)

counter = 1                             #Looping counter

EngSrc = "En"                           #Source path for english text with a single line
EngTar = "En"                           #Target path for english text with a single line
Lines = 1000                            #Total number of lines/text files required

while( counter <= Lines ):
    # Set the text input to be synthesized
    file1 = open(EngSrc+str(counter)+".txt",encoding="utf8")
    blabla = file1.read()
    synthesis_input = texttospeech.SynthesisInput(text=blabla)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(input = synthesis_input, voice = voice, audio_config = audio_config)

    # The response's audio_content is binary.
    with open(EngTar+str(counter)+".mp3", 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        
    counter = counter+1

#Wavenet Swedish Audio Generate
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3,
    speaking_rate = 1)

voiceS = texttospeech.VoiceSelectionParams(
    language_code="sv-SE",
    name="sv-SE-Wavenet-A",
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)

SweSrc = "Sv"                           #Source path for Swedish text with a single line
SweTar = "Sv"                           #Target path for Swedish text with a single line

counter = 1
while(counter<=Lines):
    # Set the text input to be synthesized
    file1 = open(SweSrc+str(counter)+".txt",encoding="utf8")
    blabla = file1.read()
    synthesis_input = texttospeech.SynthesisInput(text=blabla)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voiceS, audio_config)

    # The response's audio_content is binary.
    with open(SweTar+str(counter)+".mp3", 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        
    c = c+1