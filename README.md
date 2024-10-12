# Exploratory Data Analysis (EDA) Tool

This Python project provides a simple command-line interface for performing exploratory data analysis (EDA) on a CSV dataset. It allows users to visualize relationships within the data, assess data quality, and gain insights through various plots.

## Features

- **Data Loading**: Load datasets from CSV files.
- **Data Cleaning**: Identify and report missing values and data types.
- **Data Exploration**: Generate descriptive statistics for a better understanding of the dataset.
- **Data Visualization**:
  - Pairplot to explore relationships between features.
  - Boxplot to visualize the distribution of a specified category.
  - Correlation heatmap to identify relationships between numerical features.

## Project Status

🚧 **This project is currently in progress.** Additional features and improvements will be added over time.

## How It Works

1. **Load the Dataset**: The user provides the path to a CSV file.
2. **Choose a Category**: The user specifies a column to analyze.
3. **Perform EDA**: The tool generates insights by performing data cleaning, exploration, and visualization.

### Usage

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/eda-tool.git
    cd eda-tool
    ```

2. **Install the required libraries**:

    Make sure you have the required libraries installed. You can install them using pip:

    ```bash
    pip install pandas numpy matplotlib seaborn
    ```

3. **Run the script**:

    ```bash
    python eda_tool.py
    ```

4. **Follow the prompts** to enter the dataset path and the category (column name) to analyze.

## Example

Here’s an example of how to use the tool:

- Enter the path to your dataset:
    ```bash
    Enter the dataset path (CSV file): /path/to/your/dataset.csv
    ```

- Specify the category (column name):
    ```bash
    Enter the category (column name) to analyze: CategoryName
    ```

- The tool will then perform EDA and display insights, visualizations, and statistics.

## Insights

The visualizations produced by this tool will help you analyze the dataset better, revealing patterns, trends, and potential outliers.

## Future Improvements

- Extend support for additional file formats (e.g., Excel, JSON).
- Implement more advanced visualizations and analysis techniques.
- Enhance error handling and user feedback for invalid inputs.

## Dependencies

- [Pandas](https://pandas.pydata.org/) – for data manipulation.
- [NumPy](https://numpy.org/) – for numerical operations.
- [Matplotlib](https://matplotlib.org/) – for plotting and visualizations.
- [Seaborn](https://seaborn.pydata.org/) – for statistical data visualization.

## Contributing

Contributions to this project are welcome! If you have suggestions or would like to add new features, feel free to open an issue or create a pull request.

---

**Note**: This project is currently a work-in-progress and will be updated with more functionality and improvements over time.
