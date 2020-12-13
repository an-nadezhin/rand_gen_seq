import math
from gf2matrix import count_ones_zeroes

def runs_test(bits):
    n = len(bits)
    zeroes, ones = count_ones_zeroes(bits)

    prop = float(ones)/float(n)
    tau = 2.0/math.sqrt(n)

    vobs = 1.0
    
    for i in range(n-1):
        if bits[i] != bits[i+1]:
            vobs += 1.0
      
    p = math.erfc(abs(vobs - (2.0*n*prop*(1.0-prop)))/(2.0*math.sqrt(2.0*n)*prop*(1-prop)))
    print("prob:", p)
    success = (p >= 0.01)
    
    return success, p, None