import statistics
import math
#implementation of the pearson coefficient


def rcoefficient(a: list[float], b:list[float]) -> float:
     averagea = sum(a)/len(a)
     averageb = sum(b)/len(b)
     n = len(a)
     nenner = 0
     zählera = 0
     zählerb = 0
     for i in range(n):
        nennera = a[i]- averagea
        nennerb = b[i]- averageb
        nenner += nennera * nennerb
        zählera += nennera**2
        zählerb += nennerb**2
      
     zähler = math.sqrt(zählera) * math.sqrt(zählerb)
     if zähler == 0:
        raise ZeroDivisionError("Standard deviation is zero.")  
     r = nenner /  zähler
     return r