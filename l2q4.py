def onehot_encoding(EX):
    encoding={}
    for i in EX:
        encoding[i]=[0]*len(EX)
        index=EX.index(i)
        encoding[i][index]=1
    return encoding

EX=['AB+','AB-','A+','A-']
print("one-hot encoding:",onehot_encoding(EX))
