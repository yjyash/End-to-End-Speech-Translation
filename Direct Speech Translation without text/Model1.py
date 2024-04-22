#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 14:30:36 2021

@author: limbu
"""

#Model 1 A simple Encoder Decoder LSTM network

from keras.models import Model
from keras.layers import Dense, LSTM, RepeatVector, Input, TimeDistributed
from keras import layers
import pickle

Eng_Pickle = 'Eng.pckl'                                #Load English .pckl file
Swe_Pickle = 'Swe.pckl'                                #Load Swedish .pckl file

f = open(Eng_Pickle, 'rb')
train = pickle.load(f)
f.close()
g = open(Swe_Pickle, 'rb')
target = pickle.load(g)
g.close()

timesteps = 200
features = 128
latent_dim = 128
#Dropout Rate for both encoder and decoder inputs
dropout_rate = 0.2

inputs = Input(shape=(timesteps, features))

#Encoder
masked_encoder_inputs = layers.Masking(inputs)
encoder_lstm = (LSTM(latent_dim,return_state=True))
encoder_outputs, state_h, state_c = encoder_lstm(masked_encoder_inputs)
encoder_states = [state_h, state_c]

#Decoder
decoder_inputs = RepeatVector(timesteps)(encoder_outputs)
decoder_lstm = LSTM(latent_dim, return_state=True,return_sequences=True)
decoder_outputs, _, _ = decoder_lstm(decoder_inputs, initial_state = encoder_states)
decoder_outputs = TimeDistributed(Dense(features, activation='relu'))(decoder_outputs)

model = Model(inputs, decoder_outputs)
encoder = Model(inputs, encoder_outputs)

#Plot Model FlowChart
from keras.utils import plot_model
plot_model(model, to_file='model1.png', show_shapes=True, show_layer_names=True)

# Compile Model
model.compile(optimizer='adam', loss='mean_squared_error')

# Run Training
model.fit(train, target,
          batch_size=64,
          epochs=1000,
          validation_split=0.2)

#Save Model Weights
model.save('s2sI.h5')

#Prediction model for training samples
y_predS = model.predict(train)

#Predicted 1st Sample Audio
start = time.time()
print("Timing starts now")
mel = np.abs(np.exp(y_predS[0].T))
res = librosa.feature.inverse.mel_to_audio(mel)
res = (np.iinfo(np.int32).max * (res/np.abs(res).max())).astype(np.int32)
end = time.time() 
print(end - start)

#Output Predicted Audio
import IPython.display as ipd
ipd.Audio(res,rate = sr)
