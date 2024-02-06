def ED(v1,v2):
    ED=0
    for i in range(len(v1)):
        ED+=(v1[i]-v2[i])**2
    return ED**0.5

def MD(v1,v2):
    MD=0
    for i in range(len(v1)):
        MD+=(v1[i]-v2[i])
    return MD

v1=[1,2]
v2=[1,3]
ed=ED(v1,v2)
md=MD(v1,v2)
print("euclidean distance:",ed)
print("manhattan distance:",md)
