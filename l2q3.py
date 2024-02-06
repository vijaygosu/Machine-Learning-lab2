def label_encoding(EX):
    encoding={}
    label=0
    for i in EX:
            encoding[i]=label
            label+=1
    return encoding

EX=['AB+','AB-','A+','A-']
print("label encoding:",label_encoding(EX))
