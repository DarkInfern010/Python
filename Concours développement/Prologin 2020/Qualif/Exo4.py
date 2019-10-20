"""
3
4
0 0 0
2 0 1
0 3 1
1 3 2
5
0 1 2 1 2

6

3
5
0 1 0
1 1 1
6 2 0
6 0 1
7 1 2
14
1 0 1 0 1 2 0 1 0 1 2 0 0 1

24

"""

def capitalisme_interplanetaire(t, n, planetes, d, mission):
    """
    :param t: nombre de types de planètes distincts
    :type t: int
    :param n: le nombre de planètes dans le système
    :type n: int
    :param planetes: les planètes du système
    :type planetes: list[dict["x": int, "y": int, "k": int]]
    :param d: la durée de la mission à traiter
    :type d: int
    :param mission: pour chaque jour de la mission, le type de planète à visiter
    :type mission: list[int]
    """
    # TODO Affichez un entier : la distance minimale à parcourir pour remplir
    # la mission décrite. Les distances devront être calculées en utilisant la
    # distance de Manhattan, décrite ci-dessus.



#endef


if __name__ == '__main__':
    t = int(input())
    n = int(input())
    planetes = [dict(zip(("x", "y", "k"), map(int, input().split()))) for _ in range(n)]
    d = int(input())
    mission = list(map(int, input().split()))
    capitalisme_interplanetaire(t, n, planetes, d, mission)
