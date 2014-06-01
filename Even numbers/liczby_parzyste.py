# Podstawy algorytmow
# Autor: Adam BOCZULA
# Data: 27.05.2014 r.

# klasa Liczby_parzyste

class Liczby_parzyste:
    def __init__(self):
        None
    
    def wyznacz_parzyste(self, a, b):
        result = []
        i = a
        if(a >= b):
            return -1
        while(i < b):
            if i%2 == 0 and i != 0:
                result.append(i)
            i = i+1
        return result

if __name__ == "__main__":
    l = Liczby_parzyste()
    a=-10
    b=21
    print(l.wyznacz_parzyste(a,b))
