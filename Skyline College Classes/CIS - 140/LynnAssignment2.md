# Assignment 2 - SQL

## a. Give the class names and countries of the classes that carried guns of at least 16-inch bore.

**Answer:**

```
SELECT class, country
FROM Classes
WHERE numGuns >= 10;
```

**Result:**
| class | country |
|-------|---------|
| Tennessee | USA |

## b. Find the names of all ships launched prior to 1918, but call the resulting column shipName.

**Answer:**

```
SELECT name AS shipName
FROM Ships
WHERE launched < 1918;
```

**Result:**
| shipName |
|------|
| Haruna |
| Hiei |
| Kirishima |
| Kongo |
| Ramillies |
| Renown |
| Repulse |
| Resolution |
| Revenge |
| Royal Oak |
| Royal Sovereign |

## c. Find the names of ships sunk in battle and the name of the battle in which they were sunk.

**Answer:**

```
SELECT ship
FROM Outcomes
WHERE battle = 'Denmark Strait' AND result = 'sunk';
```

**Result:**
| ship | battle |
|------|------|
| Arizona | Pearl Harbor
| Bismarck | Denmark Strait
| Fuso | Surigao Strait
| Hood | Denmark Strait
| Kirishima | Guadalcanal
| Scharnhorst | North Cape
| Yamashiro | Surigao Strait

## d. Find the ships heavier than 35,000 tons.

**Answer:**

```
SELECT s.name
FROM Classes c JOIN Ships s ON c.class = s.class
WHERE c.displacement > 35000;
```

**Result:**
| name |
|------|
| Iowa |
| Missouri |
| Musashi |
| New Jersey |
| North Carolina |
| Washington |
| Wisconsin |
| Yamato |

## e. List the name, displacement, and number of guns of the ships engaged in the battle of Guadalcanal.

**Answer:**

```
SELECT s.name, c.displacement, c.numGuns
FROM Ships s
JOIN Classes c ON s.class = c.class
JOIN Outcomes o ON s.name = o.ship
WHERE o.battle = 'Guadalcanal';
```

**Result:**
| name | displacement | numGuns |
|------|--------------|---------|
| Kirishima | 32000 | 8 |
| Washington | 37000 | 9 |

## f. List all the ships mentioned in the database. (Remember that all these ships may not appear in the Ships relation.)

**Answer:**

```
SELECT name FROM Ships
UNION
SELECT ship FROM Outcomes;
```

**Result:**
| name |
|------|
| California |
| Haruna |
| Hiei |
| Iowa |
| Kirishima |
| Kongo |
| Missouri |
| Musashi |
| New Jersey |
| North Carolina |
| Ramillies |
| Renown |
| Repulse |
| Resolution |
| Revenge |
| Royal Oak |
| Royal Sovereign |
| Tennessee |
| Washington |
| Wisconsin |
| Yamato |
| Arizona |
| Bismarck |
| Fuso |
| Hood |
| King George V |
| Prince of Wales |
| Rodney |
| Scharnhorst |
| South Dakota |
| West Virginia |
| Yamashiro |
| Duke of York |
