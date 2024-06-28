import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import codecademylib3

# Function to choose a statistic
def choose_statistic(x, sample_stat_text):
    if sample_stat_text == "Mean":
        return np.mean(x)
    elif sample_stat_text == "Minimum":
        return np.min(x)
    elif sample_stat_text == "Variance":
        return np.var(x)
    else:
        raise Exception('Make sure to input "Mean", "Minimum", or "Variance"')

# Function to plot the population distribution
def population_distribution(population_data):
    sns.histplot(population_data, stat='density')
    plt.title(f"Population Distribution")
    plt.xlabel('')
    plt.show()
    plt.clf()

# Function to plot the sampling distribution
def sampling_distribution(population_data, samp_size, stat):
    sample_stats = []
    for i in range 500):
        samp = np.random.choice(population_data, samp_size, replace=False)
        sample_stat = choose_statistic(samp, stat)
        sample_stats.append(sample_stat)
    
    pop_statistic = round(choose_statistic(population_data, stat), 2)
    sns.histplot(sample_stats, stat='density')
    plt.title(f"Sampling Distribution of the {stat} \nMean of the Sample {stat}s: {round(np.mean(sample_stats), 2)} \n Population {stat}: {pop_statistic}")
    plt.axvline(pop_statistic, color='g', linestyle='dashed', label=f'Population {stat}')
    plt.axvline(np.mean(sample_stats), color='orange', linestyle='dashed', label=f'Mean of the Sample {stat}s')
    plt.legend()
    plt.show()
    plt.clf()

# Load the Spotify dataset
spotify_data = pd.read_csv("spotify_data.csv")

# Preview the dataset
print(spotify_data.head())

# Select the relevant column for analysis
song_tempos = spotify_data['tempo']

# Plot the population distribution with the mean labeled
population_distribution(song_tempos)

# Generate and plot the sampling distribution of the sample mean
sampling_distribution(song_tempos, 30, "Mean")

# Generate and plot the sampling distribution of the sample minimum
sampling_distribution(song_tempos, 30, "Minimum")

# Generate and plot the sampling distribution of the sample variance
sampling_distribution(song_tempos, 30, "Variance")

# Calculate the population mean and standard deviation
population_mean = np.mean(song_tempos)
population_std = np.std(song_tempos)

# Calculate the standard error
standard_error = population_std / (30 ** 0.5)

# Calculate the probability of observing an average tempo of 140 bpm or lower from a sample of 30 songs
print(stats.norm.cdf(140, population_mean, standard_error))

# Calculate the probability of observing an average tempo of 150 bpm or higher from a sample of 30 songs
print(1 - stats.norm.cdf(150, population_mean, standard_error))
