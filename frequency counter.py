user_input = input("Enter the list elements separated by space: ")
L1 = list(map(int, user_input.split()))
frequency = {}
for item in L1:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print("Frequency of elements:")
for key, value in frequency.items():
    print(f"{key}: {value}")
most_repetitive = max(frequency, key=frequency.get)
print(f"\nThe most repetitive element is: {most_repetitive}")
