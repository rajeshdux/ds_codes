
d1={'id1':1,'id2':4,'id3':5}
d2={'id1':5,'id2':50,'id4':20}
#d3={'id':6,'id2':54,'id3':5,'id5':20}

'''
Add these list d1 d2 index values ..result should be list d3
'''

d3={}

for (k1,v1),(k2,v2) in zip(d1.items(),d2.items()):
    if k1==k2:
        d3.update({k1:(v1+v2)})
    else:
        d3.update({k1:v1})
        d3.update({k2:v2})

print(d3)
