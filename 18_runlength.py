def run_length_encoding(input_array):
    i = 0
    result = []
    while i < len(input_array):
        count = 1
        while i + 1 < len(input_array) and input_array[i] == input_array[i+1]:
            i += 1
            count += 1
        result.append((input_array[i], count))
        i += 1
    return result

# Your data
data = [1,1,1,1,2,2,2,2,2,7,7,7,7,7,8,8,1,1,1]

# Apply run-length encoding
encoded_data = run_length_encoding(data)
print(encoded_data)
