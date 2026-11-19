import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    dot=0.0
    mag_a=0.0
    mag_b=0.0
    for i in range(len(a)):
        dot=dot+(a[i]*b[i])
        mag_a+=a[i]*a[i]
        mag_b+=b[i]*b[i]
    if mag_a == 0.0 or mag_b ==0:
        return 0.0
    ans=dot/(math.sqrt(mag_a)*math.sqrt(mag_b))
    return ans 
    pass