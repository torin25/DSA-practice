# sample=[1,2,3,4,5]
given=[4,5,1,2,3]
given_sorted=sorted(given)
for i in range(len(given)):
    if given ==given_sorted[i%len(given):]+given_sorted[:i%len(given)]:
        print(True)