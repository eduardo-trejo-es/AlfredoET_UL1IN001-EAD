# Alfredo Eduardo TREJO MARTINEZ – UL1IN001 EAD – Devoir 1 
# N etudiant : 21513946
# Alfredo.Trejo@etu.sorbonne-universite.fr 
# lien GitHub : https://github.com/eduardo-trejo-es

import math

# =========================
#     Exercice 1 : Triangles
# =========================

# Exercice 1, question 1.1
def definit_triangle(a: float, b: float, c: float) -> bool:
    """Renvoie True si a, b et c peuvent former un triangle."""
    s: float = (a + b + c) / 2
    # Précondition : a > 0, b > 0, c > 0.
    # Renvoie True si a, b et c peuvent former un triangle.
    # Idée : chaque côté doit être < (a + b + c)/2.
    if not (a > 0 and b > 0 and c > 0):
        return False
    # Condition équivalente aux inégalités triangulaires
    return (a < s) and (b < s) and (c < s)

#  tests (1.1)
assert not definit_triangle(1, 1, 20)
assert definit_triangle(4, 2, 3)
assert definit_triangle(4, 4, 4)


# Exercice 1, question 1.2
def aire_bis(a: float, b: float, c: float) -> float:
    """Calcule l'aire du triangle (a,b,c) par la méthode décrite."""
    # Précondition : definit_triangle(a, b, c) == True.
    # Calcule l'aire du triangle.
    # On range u1 ≤ u2 ≤ u3. On prend u3 comme base et on projette u1.
    # Formules : x = (u1^2 - u2^2 + u3^2) / (2*u3),
    # A = 1/2 * u3 * sqrt(u1^2 - x^2).
    # ordonnancement basique sans structures avancées
    u1: float = min(a, b, c)
    u3: float = max(a, b, c)
    u2: float = a + b + c - u1 - u3
    # hauteur par projection (loi des cosinus)
    x: float = (u1*u1 - u2*u2 + u3*u3) / (2 * u3)
    h_sq: float = u1*u1 - x*x
    # Par prudence numérique si h_sq ~ 0 négatif par arrondi
    if h_sq < 0 and h_sq > -1e-12:
        h_sq = 0.0
    h: float = math.sqrt(h_sq)
    return 0.5 * u3 * h

#  tests (1.2)
assert abs(aire_bis(4, 2, 3) - 2.9047375096555625) < 1e-12
# assert abs(aire_bis(4, 3, 3) - 4.47213595499958) < 1e-12
# assert abs(aire_bis(4, 4, 4) - 6.928203230275509) < 1e-12
# assert abs(aire_bis(3, 4, 5) - 6.0) < 1e-12


# Exercice 1, question 1.3
def nb_triangles_speciaux(n: int, p: int) -> int:
    """Compte les triangles (a≤b≤c) avec n≤a,b,c≤p tels que aire = périmètre."""
    # Précondition : n > 0 et p >= n.
    # Compte les triangles (a ≤ b ≤ c) avec n ≤ a, b, c ≤ p
    # tels que l'aire est égale au périmètre.
    # Utilise des boucles simples, sans listes.
    compte: int = 0
    a: int = n
    while a <= p:
        b: int = a
        while b <= p:
            c: int = b
            while c <= p:
                if definit_triangle(a, b, c):
                    perim: int = a + b + c
                    # Aire via Héron (stable ici) pour comparer simplement
                    s: float = perim / 2.0
                    area_sq: float = s * (s - a) * (s - b) * (s - c)
                    if area_sq >= 0:
                        area: float = math.sqrt(area_sq)
                        if abs(area - perim) < 1e-9:
                            compte = compte + 1
                c = c + 1
            b = b + 1
        a = a + 1
    return compte

#  tests (1.3)
assert nb_triangles_speciaux(1, 20) == 4


# =========================
#      Exercice 2 : Boucles
# =========================

# Définition de f (formule modifiée le 10/10 à 19h30)
# Exercice 2, question 2.1
def calcule_f(n: int) -> int:
    """Définition piècewise de f(n) (impair/pair)."""
    # Renvoie f(n) :
    # - si n est impair et n > 5  → n - 1
    # - si n est impair et n ≤ 5  → (n + 1)^2
    # - sinon (pair)              → n//2 + 1
    # impair si n % 2 != 0
    if (n % 2 != 0):
        m: int = n + 1
        if n > 5:
            return n - 1
        else:
            return m * m
    else:
        # division entière + 1 (Z -> Z):
        return (n // 2) + 1

# tests (2.1)
assert calcule_f(0) == 1
# assert calcule_f(51) == 50
# assert calcule_f(-8) == -3


# Exercice 2, question 2.2
def calcule_suite(a: int, n: int) -> int:
    """Renvoie u_n pour u_0=a et u_{k+1}=f(u_k)."""
    # Précondition : n ≥ 0.
    # Renvoie u_n défini par u_0 = a et u_{k+1} = f(u_k).
    i: int = 0
    u: int = a
    while i < n:
        u = calcule_f(u)
        i = i + 1
    return u

# tests (2.2)
assert calcule_suite(5, 3) == 18
# assert calcule_suite(0, 6) == 8
# assert calcule_suite(-8, 15) == 16


# Exercice 2, question 2.3
def val_max(a: int, n: int) -> int:
    """Max des valeurs u_0…u_n de la suite définie par f."""
    # Précondition : n ≥ 0.
    # Renvoie la plus grande valeur parmi u_0…u_n.
    # Fait en une seule passe.
    i: int = 0
    u: int = a
    maxi: int = u
    while i < n:
        u = calcule_f(u)
        if u > maxi:
            maxi = u
        i = i + 1
    return maxi

#  tests (2.3)
assert val_max(5, 20) == 36
# assert val_max(0, 6) == 16
# assert val_max(-100, 10) == 2304


# Exercice 2, question 2.4
def indice_max(a: int, n: int) -> int:
    """Indice du plus grand terme parmi u_0…u_n (plus petit indice si égalité)."""
    # Précondition : n ≥ 0.
    # Renvoie l'indice du plus grand terme parmi u_0…u_n
    # (on prend le plus petit indice en cas d'égalité).
    # u0
    i: int = 0
    u: int = a
    maxi: int = u
    idx: int = 0
    # construire u1..un
    while i < n:
        u = calcule_f(u)
        if u > maxi:
            maxi = u
            idx = i + 1  # on vient de calculer u_{i+1}
        i = i + 1
    return idx

# tests (2.4)
assert indice_max(5, 20) == 1
# assert indice_max(0, 6) == 4
# assert indice_max(-100, 10) == 2


# Exercice 2, question 2.5
def grands(a: int, n: int, s: float) -> bool:
    """True si u_n ≥ s et u_{n+1} ≥ s."""
    # Précondition : n ≥ 0.
    # Renvoie True si u_n ≥ s et u_{n+1} ≥ s.
    # calcule u_n puis u_{n+1}
    i: int = 0
    u: int = a
    while i < n:
        u = calcule_f(u)
        i = i + 1
    # u est maintenant u_n
    if u < s:
        return False
    u_suiv: int = calcule_f(u)
    return u_suiv >= s

#  tests (2.5)
# assert grands(0, 4, 18.7) is False
# assert grands(0, 4, 15.2) is False
assert grands(0, 4, 2.4)


# Exercice 2, question 2.6
def indice_dec(a: int) -> int:
    """Plus petit n tel que u_{n+1} < u_n."""
    # Renvoie le plus petit n tel que u_{n+1} < u_n
    # pour la suite u_0 = a, u_{k+1} = f(u_k).
    n: int = 0
    u: int = a
    v: int = calcule_f(u)  # u1
    while not (v < u):
        u = v
        v = calcule_f(u)
        n = n + 1
    return n

#  tests (2.6)
assert indice_dec(0) == 2
# assert indice_dec(-10) == 5
# assert indice_dec(8) == 0


# ======================================
# Exercice 3 : Chaînes de caractères
# ======================================

# Exercice 3, question 3.1
def est_prefixe(p: str, s: str) -> bool:
    """True si p est un préfixe de s (la chaîne vide marche aussi)."""
    # Renvoie True si p est un préfixe de s (la chaîne vide marche aussi).
    # Parcours caractère par caractère.
    # si p est plus longue que s, impossible
    if len(p) > len(s):
        return False
    i: int = 0
    ok: bool = True
    while i < len(p) and ok:
        if p[i] != s[i]:
            ok = False
        i = i + 1
    return ok

#  tests (3.1)
assert est_prefixe("", "")
# assert est_prefixe("py", "python") is True
# assert est_prefixe("", "python") is True
# assert est_prefixe("python", "python") is True
# assert est_prefixe("hon", "python") is False
# assert est_prefixe("python", "py") is False


# Exercice 3, question 3.2
def est_present(s: str, c: str, n: int) -> bool:
    """True si s contient au moins n fois le caractère c."""
    # Précondition : len(c) == 1 et n > 0.
    # Renvoie True si s contient au moins n fois le caractère c.
    i: int = 0
    compte: int = 0
    while i < len(s) and compte < n:
        if s[i] == c:
            compte = compte + 1
        i = i + 1
    return compte >= n

#  tests (3.2)
assert est_present("Ceci est une phrase", "e", 2)
# assert est_present("Ceci est une phrase", "e", 5) is False
# assert est_present("Ceci est une phrase", "t", 3) is False
# assert est_present("Ceci est une phrase", "z", 1) is False
# assert est_present("", "e", 1) is False


# Exercice 3, question 3.3
def cacher(s: str, c: str, code: str) -> str:
    """Remplace chaque c par les lettres de code en boucle (ex: 'aaaa','a','xy'→'xyxy')."""
    # Précondition : len(code) > 0 et len(c) == 1.
    # Remplace chaque caractère c de s par les lettres de code en boucle.
    # Exemple : cacher("aaaa","a","xy") → "xyxy".
    res: str = ""
    k: int = 0  # index dans code
    i: int = 0
    L: int = len(code)
    while i < len(s):
        ch: str
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
assert cacher("Ceci est une phrase", "e", "papillon") == "Cpci ast unp phrasi"
# assert cacher("aaaaaaaaaaaaaaaaaaaaaaaaaaaa", "a", "papillon") == "papillonpapillonpapillonpapi"
