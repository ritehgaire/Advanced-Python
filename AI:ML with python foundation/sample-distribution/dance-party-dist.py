from helper_functions import choose_statistic, population_distribution, sampling_distribution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import codecademylib3

# Load the Spotify dataset
spotify_data = pd.read_csv("spotify_data.csv")

# Preview the dataset
print(spotify_data.head())

# Select the 'tempo' column for analysis
song_tempos = spotify_data['tempo']

# Plot the population distribution with the mean labeled
population_distribution(song_tempos)

# Generate and plot the sampling distribution of the sample mean (sample size = 30)
sampling_distribution(song_tempos, 30, "Mean")

# Generate and plot the sampling distribution of the sample minimum (sample size = 30)
sampling_distribution(song_tempos, 30, "Minimum")

# Generate and plot the sampling distribution of the sample variance (sample size = 30)
sampling_distribution(song_tempos, 30, "Variance")

# Calculate the population mean and standard deviation of song tempos
population_mean = np.mean(song_tempos)
population_std = np.std(song_tempos)

# Calculate the standard error of the mean for samples of size 30
standard_error = population_std / (30 ** 0.5)

# Calculate the probability of observing an average tempo of 140 bpm or lower from a sample of 30 songs
print(stats.norm.cdf(140, population_mean, standard_error))

# Calculate the probability of observing an average tempo of 150 bpm or higher from a sample of 30 songs
print(1 - stats.norm.cdf(150, population_mean, standard_error))
