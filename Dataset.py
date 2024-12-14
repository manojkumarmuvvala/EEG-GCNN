import matplotlib.pyplot as plt
import pandas as pd

# Load the data
data = pd.read_csv('D:\pythonProject\master_metadata_index.csv')

# Plot histograms for numerical columns
numerical_columns = ['record_length_seconds', 'record_length_samples', 'sampling_freq', 'start_sample_index', 'end_sample_index']
for column in numerical_columns:
    plt.figure(figsize=(8, 6))
    plt.hist(data[column], bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

# Plot bar chart for categorical column 'label'
plt.figure(figsize=(8, 6))
data['label'].value_counts().plot(kind='bar', color='orange')
plt.title('Distribution of Labels')
plt.xlabel('Label')
plt.ylabel('Count')
plt.grid(axis='y')
plt.show()