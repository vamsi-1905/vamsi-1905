def frequency_count(list_item):

    frequency = {}

    for item in list_item:
        if item in frequency:
          frequency[item]+=1
        else:
            frequency[item]=1

    return frequency



sample_input = ['pen', 'pencil', 'eraser', 'pen', 'sharpener', 'pencil', 'ruler']
frequency = frequency_count(sample_input)
print(frequency)