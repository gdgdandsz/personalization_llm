import pandas as pd
from sklearn.model_selection import train_test_split

# Load the data
data_path = '/scratch/wd2148/prompt_optimization/data/clustered_data_label_0.csv'
data = pd.read_csv(data_path)

# Split the data into train and test sets
train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)

# Save the train and test sets to new CSV files
train_set.to_csv('/scratch/wd2148/prompt_optimization/data/cluster_0_train_set.csv', index=False)
test_set.to_csv('/scratch/wd2148/prompt_optimization/data/cluster_0_test_set.csv', index=False)
