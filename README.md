# Dataset Analyzer

## Description

**The Dataset Analyzer** is a Python-based tool designed to compute statistical metrics from a dataset of integers. This
tool is built to be user-friendly and easily accessible to anyone needing to analyze numerical data.

### Features

- Computes maximum and minimum values from the dataset.
- Calculates the median and arithmetic mean.
- Identifies the longest increasing and decreasing sequences of numbers.

### Requirements

- `Python 3.x`
- `NumPy library`

## Usage Instructions

### Step 1: Clone the Repository

- Clone this repository to your local machine using Git:

```commandline
git clone https://github.com/i-stanko/DatasetAnalyzer.git
```

- Navigate to the repository directory:

```commandline
cd DatasetAnalyzer
```

### Step 2: Install Dependencies

- Ensure you have Python 3 installed on your system. You will also need the NumPy library, which can be installed using
  pip:

```commandline
pip install numpy
```

### Step 3: Running the Analyzer

- To run the Dataset Analyzer, use the following command in your terminal:

```commandline
python3 data_stats.py
```

- When prompted, enter the file path to your dataset. The file should contain a series of integers, each on a new line.

```commandline
Enter the file path: path/to/your/dataset.txt
```

### Step 4: Viewing the Results

After processing, the statistical metrics and sequences will be displayed in the terminal. For long sequences, only a
portion of the sequence will be shown for readability.

## Limitations

- This tool is designed to be used by anyone with access to Python and the ability to install necessary libraries.
- The tool can process any file containing a series of integers, allowing for versatility in dataset choice.
- All software and methodologies used are open-source and legally available. Users are encouraged to attribute any
  external sources if modifications are made.
