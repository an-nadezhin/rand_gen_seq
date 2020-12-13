import math
from gf2matrix import count_ones_zeroes

def monobit_test(bits):
    
    zeroes, ones = count_ones_zeroes(bits)
    print("  Ones count   = %d" % ones)
    print("  Zeroes count = %d" % zeroes)
    
    p = math.erfc(float(abs(ones - zeroes))/(math.sqrt(float(len(bits))) * math.sqrt(2.0)))
    print(p)
    success = (p >= 0.01)
    return success, p, None
