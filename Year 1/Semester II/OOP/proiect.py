from abc import ABC, abstractmethod


'''
CERINTA PROBLEMEI
10.	Structură ierarhică de clase privitoare la figuri plane, care conţine  o clasă abstractă, din care derivă clase care reprezintă: puncte (date prin perechi de coordonate exprimate în pixeli, perechile fiind date cu ajutorul  unei structuri definite separat);  segmente orizontale  (date prin 3 numere reprezentând ordonata comună şi cele două abscise ale capetelor, exprimate în pixeli);  segmente verticale  (date prin 3 numere reprezentând abscisa comună şi cele două ordonate ale capetelor, exprimate în pixeli); dreptunghiuri (date printr-un punct reprezentând vârful din stânga sus şi două numere reprezentând laturile dreptunghiului, exprimate în pixeli). Operatorii +, * sunt supraîncărcaţi cu operaţiile de translaţie, respectiv de scalare (adică modificarea fiecărei coordonate a punctelor figurii prin înmulţirea cu un număr real numit factor de scalare ataşat respectivei coordonate). Ambele operaţii au primul operand o figură, iar al doilea operand o pereche de numere reprezentând  vectorul de translaţie, respectiv perechea de factori de scalare, rezultatul fiind o figură. Operaţiile se dau ca metode virtuale pure în clasa abstractă şi se definesc pentru fiecare clasă reprezentând figuri particulare. Se vor scrie metode de afişare a figurilor, prin supradefinirea unei metode virtuale pure din clasa abstractă, utilizându-se funcţii din bibliotecile grafice. Clasa abstractă are o dată membră de tip int reprezentând tipul de figură, iar fiecare constructor al unei clase derivate dă acestui câmp o valoare proprie clasei: 0 pentru puncte, 1 pentru segmente orizontale , 2 pentru segmente verticale , 3 pentru dreptunghiuri.
'''



# input: (x1,y1)
class Coordonate():
    pass

class Vector2D():
    pass

# de definit in clasa abstracta
# operatii pentru fiecare subclasa: 
# + = operatie de translatie (Shape + Vector Translatie = Translated Shape)
# * = operatie de scalare (Shape + Scalar Pair = Scaled Shape)
class Forma(ABC):

    @abstractmethod
    def __add__(self, other:Vector2D):
        pass

    @abstractmethod
    def __mul__(self, other: float):
        pass


# input: (x1,y1), (x2,y2) foloseste clasa coordonate
class Punct(Forma):
    def __init__(self) -> None:
        super().__init__()

    def __add__(self, other:Vector2D):
        pass

    def __mul__(self, other: float):
        pass

# input: y, x1, x2
class SegmentOrizontal(Forma):
    pass

# input: x, y1, y2
class SegmentVertical(Forma):
    pass

# input: pct stanga sus (x1,y1) si lungime, latime
class Dreptunghi(Forma):
    pass

p = Punct()




