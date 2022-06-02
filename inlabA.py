def minmax(l,i=0,min=float('inf'),max=float('-inf')):
    e=l[i]

    if e<min: cmin=e
    if e>max: cmax=e
    if i==len(l)-1:
        return (min,max)
    return minmax(l,i+1,min,max)