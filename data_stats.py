import numpy as np


def compute_dataset_metrics(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = np.fromfile(file, dtype=int, sep='\n')

        max_number = np.max(numbers)
        min_number = np.min(numbers)
        median = int(np.median(numbers))
        mean = int(np.mean(numbers))

        return {
            'Max Number': max_number,
            'Min Number': min_number,
            'Median': median,
            'Arithmetic Mean': mean
        }

    except FileNotFoundError:
        return 'File not found. Check the file path.'
    except Exception as e:
        return f'An error occurred while reading the file: {e}'


if __name__ == '__main__':
    file_path = input('Enter the file path: ')
    data = compute_dataset_metrics(file_path)
    print(data)
