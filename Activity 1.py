tup=("Chris",80,15,"AKMSS")
print(tup)
print(tup[1])

tup1=(7,5,9,2)
tup2=(4,)

print("New tuple is ",tup1+tup2)

tup3=("AKMSS",[3,4,5],[6,7,8])

print(tup3[1][0])
print(tup3[0][2])
print(tup3[2][1])

tup4=('A','K','M','S','S')
for tup in tup4:
    print("Hello",tup)