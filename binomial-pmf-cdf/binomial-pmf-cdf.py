import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    def factorial(num: int)->int:
        fact=1
        while num>0:
            fact=fact*num
            num-=1    
        return fact
    sucess=p**k
    fail=(1-p)**(n-k)
    pmf=(factorial(n)/(factorial(n-k)*factorial(k)))*sucess*fail
    i=k
    cdf=0
    while i>-1:
        Sucess=p**i
        failure=(1-p)**(n-i)
        cdf+=(factorial(n)/(factorial(n-i)*factorial(i)))*Sucess*failure
        i-=1
    return {
        "pmf": float(pmf),
        "cdf": float(cdf)
    }
    pass