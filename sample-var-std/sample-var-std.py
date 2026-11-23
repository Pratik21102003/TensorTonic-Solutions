import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    ans=0.0
    n=len(x)
    mean=sum(x)/n
    for i in range (n):
        ans=ans+(x[i]-mean)**2
    var=ans/(n-1)
    st_dev=var**0.5
    return {
        "variance":var,
        "standard_deviation":st_dev
    }
    pass