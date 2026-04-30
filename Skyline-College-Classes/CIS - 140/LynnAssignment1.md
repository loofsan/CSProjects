# Assignment 1 - Relational Algebra

## a. Give the class names and countries of the classes that carried guns of at least 16-inch bore.

**Answer:**

```
π class, country (σ bore ≥ 16 (Classes))
```

**Result:**
| class | country |
|-------|---------|
| Iowa | USA |
| North Carolina | USA |
| Yamato | Japan |

## b. Find the ships launched prior to 1921.

**Answer:**

```
π name (σ launched < 1921 (Ships))
```

**Result:**
| name |
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
| Tennessee |

## c. Find the ships sunk in the battle of the Denmark Strait.

**Answer:**

```
π ship (σ battle = 'Denmark Strait' ∧ result = 'sunk' (Outcomes))
```

**Result:**
| ship |
|------|
| Bismarck |
| Hood |

## d. The treaty of Washington in 1921 prohibited capital ships heavier than 35,000 tons. List the ships that violated the treaty of Washington.

**Answer:**

```
π name (σ displacement > 35000 (Classes ⋈ Ships))
```

**Result:**
| name |
|------|
| Iowa |
| Missouri |
| New Jersey |
| Wisconsin |
| North Carolina |
| Washington |
| Musashi |
| Yamato |

## e. List the name, displacement, and number of guns of the ships engaged in the battle of Guadalcanal.

**Answer:**

```
π name, displacement, numGuns (
  Ships ⋈ Classes ⋈ (π ship (σ battle = 'Guadalcanal' (Outcomes)))
)
```

**Result:**
| name | displacement | numGuns |
|------|--------------|---------|
| Kirishima | 32000 | 8 |
| South Dakota | NULL | NULL |
| Washington | 37000 | 9 |

## f. List all the capital ships mentioned in the database. (Remember that all these ships may not appear in the Ships relation.)

**Answer:**

```
π name (Ships) ∪ π ship (Outcomes)
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

## g. Find the classes that had only one ship as a member of that class.

**Answer:**

```
π class (Classes) - π class (
  ρS1(Ships) ⋈ S1.class = S2.class ∧ S1.name ≠ S2.name ρS2(Ships)
)
```

**Result:**
| class |
|-------|
| Tennessee |
