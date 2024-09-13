"""
on importe dans la bibliothèque math la fonction racine
"""
from math import sqrt
#### Fonction secondaire
def isprime(p):
    """
        la fonction prend en entrée un entier et détermine si le nombre est premier ou non
    """
    # votre code ici
    if p in (0,1):
        return False
    rac=sqrt(p)
    for d in range(2,int(rac)+1): 
        if p%d == 0:
            return False
    return True
#### Fonction principale
def main():
    """
    la fonction effectue determine parmis les 100 premiers nombres ceux qui sont premier
    """
    # vos appels à la fonction secondaire ici
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()


if __name__ == "__main__":
    main()
