# Assignment 5 - R Vectors

## 1. Create the vectors:

### (1.a) (1,2,3,...,29,30,29,28,...,2,1)

```
vector1 <- c(1:30, 29:1)
```

### (1.b) (7, 9, 5) and assign it to the name tmp

```
tmp <- c(7, 9, 5)
```

### (1.c) (7,9,5,7,9,5,...,7,9,5,7) where there are 11 occurrences of 7, 10 occurrences of 9 and 10 occurrences of 5

```
vector2 <- c(rep(tmp, 10), 7)
```

## 2. Create the following vector:

### (0.1^3^0.2^1^,0.1^6^0.2^4^,...,0.1^36^0.2^34^)

```
tmp2 <- seq(1,34,3)
tmp3 <- seq(3,36,3)
vector3 <- (0.1 ^ tmp2) * (0.2 ^ tmp3)
```

## 3. Calculate the following:

$$\sum_{k=10}^{100} (k^3+4k^2)$$

```
k <- 10:100
tmp4 <- (k ^ 3) + 4 * (k ^ 2)
result <- sum(tmp4)
result
```

## 4. The following segment of R code creates two vectors of random integers. Each of the created vectors have 100 elements. Furthermore, the elements are selected with replacement from the set of all non-negative integers between 0 and 9999. For set.seed( ), see the “Setting the random number seed” section from Roger Peng’s textbook.

```
set.seed(50)
aVector <- sample(0:9999, 100, replace=T)
bVector <- sample(0:9999, 100, replace=T)
```

### (4.a) Create the vector (b2 − a1, b3 − a2, ... ,bn − an−1)

```
tmpBVector <- bVector[2:100]
tmpAVector <- aVector[1:99]
vector4 <- tmpBVector - tmpAVector
```

### (4.b) Create the vector (a1 + 2a2 − a3, a2 + 2a3 − a4,...,an−2 + 2an−1 − an)

```
tmpAV1 <- aVector[1:98]
tmpAV2 <- aVector[2:99]
tmpAV3 <- aVector[3:100]
vector5 <- tmpAV1 + (2 * tmpAV2) - tmpAV3
```

### (4.c) Pick out the values in bVector which are greater than 5555.

```
vector6 <- bVector[bVector > 5555]
```

### (4.d) Create the vector ( |a1 − A|1/2, |a2 − A|1/2, . . . , |an − A|1/2) where A denotes the mean of aVector = (a1,a2,...,an) and |x| denotes the absolute value of x.

```
vector7 <- (abs(aVector - A)) ^ (1/2)
```
