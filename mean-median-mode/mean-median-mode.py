from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
 
    n=len(x)
    mean=sum(x)/n
    sorted_x=sorted(x)
    mid=n//2
    if n%2==0:
        median=(sorted_x[mid-1]+sorted_x[mid])/2
    else:
        median=sorted_x[mid]
    counts={}
    for num in x:
        counts[num]=counts.get(num,0)+1
    mode=float(max(counts,key=lambda k:(counts[k],-k)))
    return {
        "mean":float(mean),
        "median":float(median),
        "mode":mode
    }
    pass