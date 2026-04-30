# Clustering Assignment Solutions

## Question 1: K-means Algorithm (6 points)

## Given data points

- \(s_1 = (6,11)\)
- \(s_2 = (3,4)\)
- \(s_3 = (8,6)\)
- \(s_4 = (9,7)\)
- \(s_5 = (7,10)\)
- \(s_6 = (10,6)\)
- \(s_7 = (4,7)\)
- \(s_8 = (4,12)\)

## Initial centers

- Cluster 1 center: \(s_2(3,4)\)
- Cluster 2 center: \(s_5(7,10)\)
- Cluster 3 center: \(s_8(4,12)\)

### First Round of Execution

#### Step 1: Assign to nearest center

- \(s_1=(6,11)\):
  \[
  \begin{aligned}
  d(s_1,C_1) &= \sqrt{(6-3)^2+(11-4)^2}=\sqrt{9+49}=\sqrt{58}\approx7.62\\
  d(s_1,C_2) &= \sqrt{(6-7)^2+(11-10)^2}=\sqrt{1+1}=\sqrt{2}\approx1.41\\
  d(s_1,C_3) &= \sqrt{(6-4)^2+(11-12)^2}=\sqrt{4+1}=\sqrt{5}\approx2.24
  \end{aligned}
  \] \(\Rightarrow\) **assign** \(s_1\) to Cluster 2.

  <hr>

- \(s_2=(3,4)\):
  \[
  \begin{aligned}
  d(s_2,C_1) &= 0\\
  \end{aligned}
  \] \(\Rightarrow\) **assign** \(s_2\) to Cluster 1.

  <hr>

- \(s_3=(8,6)\):
  \[
  \begin{aligned}
  d(s_3,C_1) &= \sqrt{(8-3)^2+(6-4)^2}\approx 5.39\\
  d(s_3,C_2) &= \sqrt{(8-7)^2+(6-10)^2}\approx 4.12\\
  d(s_3,C_3) &= \sqrt{(8-4)^2+(6-12)^2}\approx 7.21
  \end{aligned}
  \] \(\Rightarrow\) **assign** \(s_3\) to Cluster 2.

  <hr>

- \(s_4=(9,7)\):
  \[
  \begin{aligned}
  d(s_4,C_1) &= \sqrt{(9-3)^2+(7-4)^2}\approx 6.71\\
  d(s_4,C_2) &= \sqrt{(9-7)^2+(7-10)^2}\approx 3.61\\
  d(s_4,C_3) &= \sqrt{(9-4)^2+(7-12)^2}\approx 7.07
  \end{aligned}
  \] \(\Rightarrow\) **assign** \(s_4\) to Cluster 2.

  <hr>

- \(s_5=(7,10)\):
  \[
  \begin{aligned}\\
  d(s_5,C_2) &= \sqrt{(7-7)^2+(10-10)^2} = 0\\
  \end{aligned}
  \] \(\Rightarrow\) **assign** \(s_5\) to Cluster 2.

  <hr>

- \(s_6=(10,6)\):
  \[
  \begin{aligned}
  d(s_6,C_1) &= \sqrt{(10-3)^2+(6-4)^2}\approx 7.28\\
  d(s_6,C_2) &= \sqrt{(10-7)^2+(6-10)^2}\approx 5\\
  d(s_6,C_3) &= \sqrt{(10-4)^2+(6-12)^2}\approx 8.49
  \end{aligned}
  \] \(\Rightarrow\) **assign** \(s_6\) to Cluster 2.

  <hr>

- \(s_7=(4,7)\):
  \[
  \begin{aligned}
  d(s_7,C_1) &= \sqrt{(4-3)^2+(7-4)^2}\approx 3.16\\
  d(s_7,C_2) &= \sqrt{(4-7)^2+(7-10)^2}\approx 4.24\\
  d(s_7,C_3) &= \sqrt{(4-4)^2+(7-12)^2}\approx 5
  \end{aligned}
  \] \(\Rightarrow\) **assign** \(s_7\) to Cluster 1.

  <hr>

- \(s_8=(4,12)\):
  \[
  \begin{aligned}
  d(s_8,C_3) &= \sqrt{(4-4)^2+(7-12)^2}\approx 0
  \end{aligned}
  \] \(\Rightarrow\) **assign** \(s_8\) to Cluster 3.

  <hr>

#### Step 2: Find new centers

**After First Round:**

- **Cluster 1**: ${s_2(3,4), s_7(4,7)}$
  - New center: $((3+4)/2, (4+7)/2) = (3.5, 5.5)$
    <br>
- **Cluster 2**: ${s_1(6,11), s_3(8,6), s_4(9,7), s_5(7,10), s_6(10,6)}$
  - New center: $((6+8+9+7+10)/5, (11+6+7+10+6)/5) = (8, 8)$
    <br>
- **Cluster 3**: ${s_8(4,12)}$
  - New center: $(4, 12)$

### Second Iteration

Using new centers: $C_1(3.5, 5.5), C_2(8, 8), C_3(4, 12)$

**Reassignment:**

- **Cluster 1**: ${s_2(3,4), s_7(4,7)}$
- **Cluster 2**: ${s_3(8,6), s_4(9,7), s_6(10,6)}$
- **Cluster 3**: ${s_1(6,11), s_5(7,10), s_8(4,12)}$

**New centers:**

- **Cluster 1**: $(3.5, 5.5)$
- **Cluster 2**: $((8+9+10)/3, (6+7+6)/3) = (9, 6.33)$
- **Cluster 3**: $((6+7+4)/3, (11+10+12)/3) = (5.67, 11)$

### Third Iteration (Final)

Using centers: $C_1(3.5, 5.5), C_2(9, 6.33), C_3(5.67, 11)$

**Final assignment:**

- **Cluster 1**: ${s_2(3,4), s_7(4,7)}$
  - Final center: $(3.5, 5.5)$
    <br>
- **Cluster 2**: ${s_3(8,6), s_4(9,7), s_6(10,6)}$
  - Final center: $(9, 6.33)$
    <br>
- **Cluster 3**: ${s_1(6,11), s_5(7,10), s_8(4,12)}$
  - Final center: $(5.67, 11)$
    <br>

## Question 2: Clustering Method Suitability (4 points)

### Density-based Clustering (DBSCAN) vs. Partitioning-based (K-means)

**Conditions under which DBSCAN is more suitable over K-means:**

1. **Non-spherical clusters**: DBSCAN can find clusters of any shapes
2. **Cluster densities**: DBSCAN handles clusters with different densities
3. **Outliers**: DBSCAN looks for and excludes outliers
4. **Unknown number of clusters**: DBSCAN doesn't need to pre-specify k

```
     Scenario favoring DBSCAN

     Y
     |
  10 |    * * *
     |  *       *
   8 | *         *    o (outlier)
     | *         *
   6 |  *       *
     |    * * *
   4 |              * * *
     |            *       *
   2 |           *         *
     |            *       *
   0 |              * * *
     +-------------------------> X
     0  2  4  6  8  10  12  14

     In this scenario, there are two oval shaped clusters with an outlier.
     DBSCAN, in this scenario, would correctly identify both ovals.
     Meanwhile, K-means would split these two into spherical regions.
     K-means assumes spherical clusters nad equal densities.
```

### Hierarchical Clustering vs. Partitioning-based (K-means)

**Conditions where Hierarchical Clustering is more suitable over K-means:**

1. **Cluster hierarchy**: When you need to see how clusters form smaller subclusters
2. **No predetermined k**: When the number of clusters is unknown
3. **Dendrogram visualization**: When you want a full picture of how clusters merge and relate
4. **Small to medium datasets**: Hierarchical clustering is computationally expensive for large datasets
5. **Varying cluster sizes**: When clusters have different sizes

**Graphical Illustration:**

```
     Scenario favoring Hierarchical Clustering

     Y
     |
  10 | ** ** ** **
     | ** ** ** **      (Large dense cluster)
   8 | ** ** ** **
     |
   6 |     *
     |     *   (Medium cluster)
   4 |     *
     |
   2 |         *  (Small cluster)
     |         *
   0 |
     +-------------------------> X
     0  2  4  6  8  10  12

  Hierarchical clustering naturally identifies the large, medium,
  and small clusters without forcing them into similar sizes.
  A dendrogram also shows how the clusters merge step by step.
  On the other hand, K-means is bad with clusters of different
  sizes and could split the large cluster or force all groups to be
  more similar when they're not.
```
