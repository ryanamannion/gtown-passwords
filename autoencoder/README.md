# Autoencoder

The autoencoder model includes an encoder and a decoder, where the encoder captures significant information by mapping original passwords into lower dimension vectors, and the decoder uses the information to recreate the original passwords. The intuition is to use the encoder to learn the patterns (e.g., capital letters, English words, numbers, special characters) in the training data and then use the decoder to generate new passwords with similar patterns, by minimizing the difference between the original passwords and the reconstructed ones.

Two models, Stanndard Autoencoder and Variational Autoencoder (VAE) are included in [`autoencoder/model`](https://github.com/ryanamannion/gtown-passwords/edit/main/autoencoder/model).

## Data

The data we use are included in [`autoencoder/data`](https://github.com/ryanamannion/gtown-passwords/edit/main/autoencoder/data). Go to this directory for more information.

## To Run

It's very easy to run the code on Google Colab directly, just follow these steps:

- Open a new Colab notebook here https://research.google.com/colaboratory/
- Git the repository to your own Google Drive using the code below:

  ```python
  from google.colab import drive
  drive.mount('/content/drive/')

  %cd '/content/drive/My Drive' 

  !git clone https://github.com/ryanamannion/gtown-passwords.git
  ```
