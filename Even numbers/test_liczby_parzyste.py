# Testy to liczb parzystych
# Autor: Adam BOCZULA
# Data: 27.05.2014 r.

# importy
import unittest
from liczby_parzyste import Liczby_parzyste

class TestCutter(unittest.TestCase):
    # test nr 1
    # @unittest.skip('Not yet implemented')
    def test_spawn_object_Liczby_parzyste(self):
        liczby_parzyste = Liczby_parzyste()
        self.assertIsInstance(liczby_parzyste, Liczby_parzyste)
    
    # test nr 2
    def test_a_rowne_b(self):
        liczby_parzyste = Liczby_parzyste()
        a = 0
        b = 0
        self.assertEqual(-1,liczby_parzyste.wyznacz_parzyste(a,b))

    # test nr 3
    def test_a_wieksze_b(self):
        liczby_parzyste = Liczby_parzyste()
        a = 1
        b = 0
        self.assertEqual(-1,liczby_parzyste.wyznacz_parzyste(a,b))

    # test nr 4
    def test_zwroc_brak_parzystych_z_przedzialu_(self):
        l = Liczby_parzyste()
        a = 1
        b = 2
        self.assertEqual([],l.wyznacz_parzyste(a,b))

    # test nr 5
    def test_zwroc_jedna_parzysta_z_przedzialu(self):
        l = Liczby_parzyste()
        a = 1
        b = 3
        self.assertEqual([2],l.wyznacz_parzyste(a,b))

    # test nr 6 
    def test_zwroc_wszystkie_parzyste_z_przedzialu(self):
        l = Liczby_parzyste()
        a = 1
        b = 5
        self.assertEqual([2,4],l.wyznacz_parzyste(a,b))

    # test nr 7
    def test_nie_bierz_zero_za_parzysta(self):
        l = Liczby_parzyste()
        a = -1
        b = 1
        self.assertEqual([],l.wyznacz_parzyste(a,b))

if __name__ == "__main__":
    unittest.main()

# koniec pliku
