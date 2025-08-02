import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data', color='blue')

    # Create first line of best fit (1880 to 2050)
    full_slope, full_intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_full = pd.Series(range(1880, 2051))
    y_full = full_slope * x_full + full_intercept
    plt.plot(x_full, y_full, 'r', label='Best Fit: 1880–2050')

    # Create second line of best fit (2000 to 2050)
    df_recent = df[df['Year'] >= 2000]
    recent_slope, recent_intercept, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = recent_slope * x_recent + recent_intercept
    plt.plot(x_recent, y_recent, 'green', label='Best Fit: 2000–2050')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    plt.grid(True)


    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()