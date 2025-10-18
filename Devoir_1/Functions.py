# Alfredo Eduardo TREJO MARTINEZ – UL1IN001 EAD – Devoir 1
#lien de github :D - https://github.com/eduardo-trejo-es

import math

# =========================
#     Exercice 1 : Triangles
# =========================

# Exercice 1, question 1.1
def definit_triangle(a: float, b: float, c: float) -> bool:
    """Précondition : a > 0 and b > 0 and c > 0
    Retourne True si a, b, c peuvent être les côtés d'un triangle.
    Critère utilisé : chaque côté est strictement inférieur à (a+b+c)/2.
    """
    if not (a > 0 and b > 0 and c > 0):
        return False
    s = (a + b + c) / 2
    # Condition équivalente aux inégalités triangulaires
    return (a < s) and (b < s) and (c < s)

#  tests (1.1)
"""assert definit_triangle(1, 1, 20) is False
assert definit_triangle(4, 2, 3) is True
assert definit_triangle(4, 4, 4) is True"""


# Exercice 1, question 1.2
def aire_bis(a: float, b: float, c: float) -> float:
    """Précondition : definit_triangle(a,b,c) == True
    Calcule l'aire du triangle (a,b,c) via u1 <= u2 <= u3 puis la formule donnée :
    On prend u3 comme base, on projette u1 sur cette base et on utilise
    A = (1/2)*u3*sqrt(u1^2 - x^2) avec x = (u1^2 - u2^2 + u3^2)/(2*u3).
    """
    # ordonnancement basique sans structures avancées
    u1 = min(a, b, c)
    u3 = max(a, b, c)
    u2 = a + b + c - u1 - u3
    # hauteur par projection (loi des cosinus)
    x = (u1*u1 - u2*u2 + u3*u3) / (2 * u3)
    h_sq = u1*u1 - x*x
    # Par prudence numérique si h_sq ~ 0 négatif par arrondi
    if h_sq < 0 and h_sq > -1e-12:
        h_sq = 0.0
    h = math.sqrt(h_sq)
    return 0.5 * u3 * h

#  tests (1.2)
"""assert abs(aire_bis(4, 2, 3) - 2.9047375096555625) < 1e-12
assert abs(aire_bis(4, 3, 3) - 4.47213595499958) < 1e-12
assert abs(aire_bis(4, 4, 4) - 6.928203230275509) < 1e-12
assert abs(aire_bis(3, 4, 5) - 6.0) < 1e-12"""


# Exercice 1, question 1.3
def nb_triangles_speciaux(n: int, p: int) -> int:
    """Précondition : n > 0 and p >= n
    Compte les triangles (a<=b<=c) avec n <= a,b,c <= p, tels que
    l'aire est égale au périmètre. Aucun n-uplet ni liste n'est nécessaire.
    """
    compte = 0
    a = n
    while a <= p:
        b = a
        while b <= p:
            c = b
            while c <= p:
                if definit_triangle(a, b, c):
                    perim = a + b + c
                    # Aire via Héron (stable ici) pour comparer simplement
                    s = perim / 2.0
                    area_sq = s * (s - a) * (s - b) * (s - c)
                    if area_sq >= 0:
                        area = math.sqrt(area_sq)
                        if abs(area - perim) < 1e-9:
                            compte += 1
                c += 1
            b += 1
        a += 1
    return compte

#  tests (1.3)
"""assert nb_triangles_speciaux(1, 20) == 4"""


# =========================
#      Exercice 2 : Boucles
# =========================

# Définition de f (formule modifiée le 10/10 à 19h30)
# Exercice 2, question 2.1
def calcule_f(n: int) -> int:
    """Retourne f(n) définie par:
    - n impair et n > 5  -> n - 1
    - n impair et n <= 5 -> (n + 1)^2
    - sinon (pair ou autre) -> n/2 + 1
    """
    # impair si n % 2 != 0
    if (n % 2 != 0):
        if n > 5:
            return n - 1
        else:
            m = n + 1
            return m * m
    else:
        # division entière + 1 (Z -> Z):
        return (n // 2) + 1

# tests (2.1)
"""assert calcule_f(0) == 1
assert calcule_f(51) == 50
assert calcule_f(-8) == -3"""


# Exercice 2, question 2.2
def calcule_suite(a: int, n: int) -> int:
    """Précondition : n >= 0
    Retourne u_n défini par : u_0 = a, u_{k+1} = f(u_k).
    """
    i = 0
    u = a
    while i < n:
        u = calcule_f(u)
        i = i + 1
    return u

# tests (2.2)
"""assert calcule_suite(5, 3) == 18
assert calcule_suite(0, 6) == 8
assert calcule_suite(-8, 15) == 16"""


# Exercice 2, question 2.3
def val_max(a: int, n: int) -> int:
    """Précondition : n >= 0
    Retourne la plus grande valeur parmi u0..un pour la suite définie par u0=a, u_{k+1}=f(u_k).
    Implémentation en une seule passe (sans rappeler calcule_suite à chaque fois).
    """
    i = 0
    u = a
    maxi = u
    while i < n:
        u = calcule_f(u)
        if u > maxi:
            maxi = u
        i = i + 1
    return maxi

#  tests (2.3)
"""assert val_max(5, 20) == 36
assert val_max(0, 6) == 16
assert val_max(-100, 10) == 2304"""


# Exercice 2, question 2.4
def indice_max(a: int, n: int) -> int:
    """Précondition : n >= 0
    Retourne l'indice du plus grand terme parmi u0..un (plus petit indice en cas d'égalité).
    Implémentation efficace (une passe).
    """
    # u0
    i = 0
    u = a
    maxi = u
    idx = 0
    # construire u1..un
    while i < n:
        u = calcule_f(u)
        if u > maxi:
            maxi = u
            idx = i + 1  # on vient de calculer u_{i+1}
        i = i + 1
    return idx

# tests (2.4)
"""assert indice_max(5, 20) == 1
assert indice_max(0, 6) == 4
assert indice_max(-100, 10) == 2"""


# Exercice 2, question 2.5
def grands(a: int, n: int, s: float) -> bool:
    """Précondition : n >= 0
    Retourne True si u_n >= s et u_{n+1} >= s, sinon False.
    """
    # calcule u_n puis u_{n+1}
    i = 0
    u = a
    while i < n:
        u = calcule_f(u)
        i = i + 1
    # u est maintenant u_n
    if u < s:
        return False
    u_suiv = calcule_f(u)
    return u_suiv >= s

#  tests (2.5)
"""assert grands(0, 4, 18.7) is False
assert grands(0, 4, 15.2) is False
assert grands(0, 4, 2.4) is True"""


# Exercice 2, question 2.6
def indice_dec(a: int) -> int:
    """Retourne le plus petit n tel que u_{n+1} < u_n pour la suite u_0=a, u_{k+1}=f(u_k).
    """
    n = 0
    u = a
    v = calcule_f(u)  # u1
    while not (v < u):
        u = v
        v = calcule_f(u)
        n = n + 1
    return n

#  tests (2.6)
"""assert indice_dec(0) == 2
assert indice_dec(-10) == 5
assert indice_dec(8) == 0"""


# ======================================
# Exercice 3 : Chaînes de caractères
# ======================================

# Exercice 3, question 3.1
def est_prefixe(p: str, s: str) -> bool:
    """Retourne True si p est un préfixe de s (y compris chaîne vide).
    Implémentation simple, caractère par caractère.
    """
    # si p est plus longue que s, impossible
    if len(p) > len(s):
        return False
    i = 0
    ok = True
    while i < len(p) and ok:
        if p[i] != s[i]:
            ok = False
        i = i + 1
    return ok

#  tests (3.1)
"""assert est_prefixe("", "") is True
assert est_prefixe("py", "python") is True
assert est_prefixe("", "python") is True
assert est_prefixe("python", "python") is True
assert est_prefixe("hon", "python") is False
assert est_prefixe("python", "py") is False"""


# Exercice 3, question 3.2
def est_present(s: str, c: str, n: int) -> bool:
    """Précondition : len(c) == 1 and n > 0
    Retourne True si s contient au moins n occurrences du caractère c.
    """
    i = 0
    compte = 0
    while i < len(s) and compte < n:
        if s[i] == c:
            compte = compte + 1
        i = i + 1
    return compte >= n

#  tests (3.2)
"""assert est_present("Ceci est une phrase", "e", 2) is True
assert est_present("Ceci est une phrase", "e", 5) is False
assert est_present("Ceci est une phrase", "t", 3) is False
assert est_present("Ceci est une phrase", "z", 1) is False
assert est_present("", "e", 1) is False"""


# Exercice 3, question 3.3
def cacher(s: str, c: str, code: str) -> str:
    """Précondition : len(code) > 0 and len(c) == 1
    Remplace chaque occurrence de c dans s par les caractères de 'code' cyclés.
    Exemple : cacher("aaaa", "a", "xy") -> "xyxy"
    """
    res = ""
    k = 0  # index dans code
    i = 0
    L = len(code)
    while i < len(s):
        ch = s[i]
        if ch == c:
            res = res + code[k]
            k = k + 1
            if k == L:  # cycle simple (plutôt que % pour rester très basique)
                k = 0
        else:
            res = res + ch
        i = i + 1
    return res

#  tests (3.3)
"""assert cacher("Ceci est une phrase", "e", "papillon") == "Cpci ast unp phrasi"
assert cacher("aaaaaaaaaaaaaaaaaaaaaaaaaaaa", "a", "papillon") == "papillonpapillonpapillonpapi"""