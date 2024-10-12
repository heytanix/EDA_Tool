# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set visual style
sns.set(style="whitegrid")

# Function to perform EDA
def perform_eda(file_path, category):
    # Load Dataset
    try:
        data = pd.read_csv(file_path)
        print("Dataset loaded successfully!")
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return

    # Display first few rows
    print("\nFirst 5 rows of the dataset:")
    print(data.head())

    # 1. Data Cleaning
    # Check for missing values
    print("\nMissing values in each column:")
    print(data.isnull().sum())

    # Data types
    print("\nData types of each column:")
    print(data.dtypes)

    # 2. Data Exploration
    print("\nDescriptive Statistics:")
    print(data.describe(include='all'))

    # 3. Data Visualization
    # Check if category exists in the dataset
    if category in data.columns:
        # Pairplot to see relationships between features
        sns.pairplot(data, hue=category)
        plt.title(f"Pairplot of {category} in the Dataset")
        plt.show()

        # Boxplot to visualize distribution for a specified category
        numerical_columns = data.select_dtypes(include=np.number).columns.tolist()
        
        if numerical_columns:
            plt.figure(figsize=(10, 6))
            sns.boxplot(data=data, x=category, y=numerical_columns[0])
            plt.title(f"Boxplot of {numerical_columns[0]} by {category}")
            plt.show()
        else:
            print("No numerical columns available for boxplot.")

        # Heatmap to visualize correlations if numerical columns exist
        if len(numerical_columns) > 1:
            plt.figure(figsize=(8, 6))
            correlation_matrix = data[numerical_columns].corr()
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
            plt.title("Correlation Heatmap")
            plt.show()
        else:
            print("Not enough numerical columns for correlation heatmap.")

    else:
        print(f"\n'{category}' is not a valid column in the dataset.")

    # Insights
    print("\nInsights:")
    print("Analyze the visualizations to gain insights into the dataset.")

# Main Function
def main():
    # User input for dataset path and category
    file_path = input("Enter the dataset path (CSV file): ").strip()
    
    # Check if the file exists
    if not os.path.isfile(file_path):
        print("The provided file path does not exist. Please check and try again.")
        return

    category = input("Enter the category (column name) to analyze: ").strip()

    # Perform EDA
    perform_eda(file_path, category)

# Entry Point
if __name__ == "__main__":
    main()
