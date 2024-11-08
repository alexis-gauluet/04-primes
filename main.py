"""ajoute au code la fonction racine carré"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """retourne un booléen. Si vrai le nombre passé en paramètre est premier"""
    racine=int(sqrt(p))
    prime=True
    for n in range(2,racine+1):
        if p%n==0:
            prime=False
    if p<=1:
        prime=False
    return prime



#### Fonction principale


def main():
    """fonction principale du code"""
    # vos appels à la fonction secondaire ici
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
