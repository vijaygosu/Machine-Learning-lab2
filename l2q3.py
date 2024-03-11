def label_encoding(EX):
    encoding = {}  # Initialize an empty dictionary
    label = 0  # Initialize the label value
    for i in EX:
        encoding[i] = label  # Assign a label to each unique element in EX
        label += 1  # Increment the label for the next element
    return encoding  

EX = ['AB+', 'AB-', 'A+', 'A-']  
print("label encoding:", label_encoding(EX))  
