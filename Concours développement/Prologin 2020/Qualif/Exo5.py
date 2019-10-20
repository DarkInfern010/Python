"""
5
5
3
3 2 4 3
1 3 5 4
3 4 4 5

2

5
5
2
0 2 2 4
3 2 4 3

3

"""


def forcecontreflotte(l, h, n, flotte):
    """
    :param l: la largeur de la zone
    :type l: int
    :param h: la hauteur de la zone
    :type h: int
    :param n: Le nombre de vaisseaux dans la flotte
    :type n: int
    :param flotte: une liste de vaisseaux
    :type flotte: list[dict["x": int, "y": int, "u": int, "v": int]]
    """
    # TODO Afficher le nombre minimal de lignes de force à déployer pour
    # couvrir toute la flotte.
    pass


if __name__ == '__main__':
    l = int(input())
    h = int(input())
    n = int(input())
    flotte = [
        dict(zip(("x", "y", "u", "v"), map(int, input().split())))
        for _ in range(n)
        ]
    forcecontreflotte(l, h, n, flotte)
