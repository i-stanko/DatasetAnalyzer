import numpy as np
from sequences import find_longest_sequences

def compute_dataset_metrics(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = np.loadtxt(file, dtype=int)

        max_number = np.max(numbers)
        min_number = np.min(numbers)
        median = int(np.median(numbers))
        mean = int(np.mean(numbers))

        longest_inc, longest_dec = find_longest_sequences(numbers)

        return {
            'Max Number': max_number,
            'Min Number': min_number,
            'Median': median,
            'Arithmetic Mean': mean,
            'Increasing Sequence': longest_inc,
            'Decreasing Sequence': longest_dec
        }

    except FileNotFoundError:
        return 'File not found. Check the file path.'
    except Exception as e:
        return f'An error occurred while reading the file: {e}'


if __name__ == '__main__':
    file_path = input('Enter the file path: ')
    data = compute_dataset_metrics(file_path)

    for key, value in data.items():
        if isinstance(value, list):
            print(f'{key}: Length = {len(value)}, Sequence = {value[:3]}...{value[-3:]}')
            # print(f'{key}: Length = {len(value)}, Sequence = {value[:]}')
        else:
            print(f'{key}: {value}')
