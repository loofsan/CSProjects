# Assignment 6 - Matrices in R

## Exercise 1

```
m1[,2] <- m1[,1] + m1[,3]
```

## Exercise 2

#### 1) Create a 6 × 6 matrix mTest with all 36 elements equal to 0.

```
mTest <- matrix(0, nrow=6, ncol=6)
```

#### 2) Check what the functions row and col return when applied to mTest

```
row(mTest)

      [,1] [,2] [,3] [,4] [,5] [,6]
[1,]    1    1    1    1    1    1
[2,]    2    2    2    2    2    2
[3,]    3    3    3    3    3    3
[4,]    4    4    4    4    4    4
[5,]    5    5    5    5    5    5
[6,]    6    6    6    6    6    6
```

```
col(mTest)

      [,1] [,2] [,3] [,4] [,5] [,6]
[1,]    1    2    3    4    5    6
[2,]    1    2    3    4    5    6
[3,]    1    2    3    4    5    6
[4,]    1    2    3    4    5    6
[5,]    1    2    3    4    5    6
[6,]    1    2    3    4    5    6
```

#### 3) Accordingly, create the following matrix m2:

```
m2 <- mTest
m2[row(mTest) == col(mTest) + 1] <- 1
m2[row(mTest) == col(mTest) - 1] <- 1
```

## Exercise 3

```
m3 <- outer(0:9,0:9,"+")%%10
```

## Exercise 4

```
m4 <- outer(0:8, 0:8, "-")%%9
```
