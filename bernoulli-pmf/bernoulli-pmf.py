import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    pmf=np.array([])
    for i in range (len(x)):
        if(x[i]==0):
            pmf=np.append(pmf,1-p)
        else:
            pmf=np.append(pmf,p)
    var=p*(1-p)
    return {
        "pmf": pmf,
        "mean": float(p),
        "variance": float(var)
    
    }
    pass