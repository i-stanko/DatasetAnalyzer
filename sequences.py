def find_longest_sequences(numbers):
    longest_inc, longest_dec = [], []
    current_inc, current_dec = [numbers[0]], [numbers[0]]

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current_inc.append(numbers[i])
            if len(current_inc) > len(longest_inc):
                longest_inc = current_inc.copy()
        else:
            current_inc = [numbers[i]]

        if numbers[i] < numbers[i - 1]:
            current_dec.append(numbers[i])
            if len(current_dec) > len(longest_dec):
                longest_dec = current_dec.copy()
        else:
            current_dec = [numbers[i]]

    return longest_inc, longest_dec
