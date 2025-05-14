from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Bidirectional, LSTM, Dense

model = Sequential()

model.add(Embedding(input_dim=10000, output_dim=128, input_length=100))
model.add(Bidirectional(LSTM(64, return_sequences=True)))
model.add(Bidirectional(LSTM(64)))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

# The model is a simple bidirectional LSTM for binary classification.
# The input dimension is 10000 (vocabulary size), the output dimension of the embedding layer is 128,
# and the LSTM has 64 units. The final layer is a Dense layer with a sigmoid activation function for binary classification.
# The model is compiled with binary crossentropy loss and the Adam optimizer.
# The model summary will show the architecture of the model, including the number of parameters in each layer.

 #PyTorch equivalent of the Keras code above
# Uncomment the following lines to run the PyTorch version

#import torch
#import torch.nn as nn

#class BRNN(nn.Module):
#    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim):
#        super().__init__()
#        self.embedding = nn.Embedding(vocab_size, embedding_dim)
#        self.rnn = nn.LSTM(embedding_dim, hidden_dim, bidirectional=True)
#        self.fc = nn.Linear(hidden_dim * 2, output_dim)

#    def forward(self, text):
#        embedded = self.embedding(text)
#        output, (hidden, cell) = self.rnn(embedded)
#        hidden = torch.cat((hidden[-2,:,:], hidden[-1,:,:]), dim=1)
#        return self.fc(hidden)

# Split data into training and validation sets

import numpy as np
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.33, random_state = 42)

print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

model.fit(X_train, Y_train, epochs=20, batch_size=128, verbose=2)

import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train'], loc='upper left')
plt.show()


score, acc = model.evaluate(X_test, Y_test, verbose=2, batch_size=64)
print("score: %.2f" % (score))
print("acc: %.2f" % (acc))








