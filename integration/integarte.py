import numpy as np

def integrate(f, a, b):
    """
    a : lower limit
    b : upper limit
    f : lambda function in numpy
    """
    x = np.random.uniform(a, b, 100000)
    expectation = f(x).mean()
    return (b-a) * expectation
    
print(integrate(lambda x: np.exp(-x**2), 1, 2))
print(integrate(lambda x: x**2, 3, 6))
