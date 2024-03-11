def onehot_encoding(EX):
    encoding = {}  
    for i in EX:
        encoding[i] = [0] * len(EX)  # Create a list of zeros with length equal to the number of unique elements in EX
        index = EX.index(i)  # Get the index of the current element in EX
        encoding[i][index] = 1  # Set the corresponding index to 1 for the current element
    return encoding  

EX = ['AB+', 'AB-', 'A+', 'A-']  
print("one-hot encoding:", onehot_encoding(EX))  
