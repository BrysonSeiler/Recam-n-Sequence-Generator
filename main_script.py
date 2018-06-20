'''
This script generates the Recaman Sequence.

@author: Bryson Seiler
'''

sequence_length = int(input("Enter Sequence Length: "))

hop_size = 0
current_value = 0
sequence = [0]

for i in range(sequence_length):

    hop_size = i + 1

    if hop_size < current_value and (current_value - hop_size) not in sequence:
        current_value = current_value - hop_size
        sequence.append(current_value)

    else:
        current_value = current_value + hop_size
        sequence.append(current_value)

print(sequence)