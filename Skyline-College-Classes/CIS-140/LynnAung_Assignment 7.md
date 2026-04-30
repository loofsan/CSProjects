# Building a Classification Model

## First Step: Initial Entropy

We are going to calculate the entrpy to measure the amount of uncertainty we have. To calculate the entropy of the entire dataset, we will take into account the different possibilities.

- High Risk: 6
- Moderate Risk: 3
- Low Risk: 5

$$Entropy(S) = -(\frac{6}{14})\times\log_2(\frac{6}{14}) - (\frac{3}{14})\times\log_2(\frac{3}{14}) - (\frac{5}{14})\times\log_2(\frac{5}{14})$$
$$Entropy(S) = 1.531$$

## Second Step: Calculate Information Gain

We are going to calculate the information gain which measures how much uncertainty is reduced by considering its features.

We are going to do that for each attribute:

- Security
- Salary
- Debt
- Reputation

Security Attribute:

- Adequate: 3
- None: 11

$$Entropy(S_{adequate}) = -(\frac{0}{3})\times\log_2(\frac{0}{3}) - (\frac{1}{3})\times\log_2(\frac{1}{3}) - (\frac{2}{3})\times\log_2(\frac{2}{3})$$

$$Entropy(S_{adequate}) = 0.918$$
$$Entropy(S_{none}) = -(\frac{6}{11})\times\log_2(\frac{6}{11}) - (\frac{2}{11})\times\log_2(\frac{2}{11}) - (\frac{3}{11})\times\log_2(\frac{3}{11})$$

$$Entropy(S_{none}) = 1.435$$
$$Entropy(S, Security) = 1.531 - [(3/14)\times0.918 + (11/14)\times1.435] = 1.530 - [0.197 + 1.127] = 0.206$$

Salary Attribute

- $0 to $30K: 4
- $30K to $60K: 4
- over $60K: 6

$$Entropy(S_{0-30K}) = -(4/4)×log₂(4/4) = 0$$
$$Entropy(S_{30-60K}) = -(2/4)×log₂(2/4) - (2/4)×log₂(2/4) = 1.0$$
$$Entropy(S_{over60K}) = -(0/6)×log₂(0/6) - (1/6)×log₂(1/6) - (5/6)×log₂(5/6) = 0.650$$
$$Gain(S, Salary) = 1.530 - [(4/14)×0 + (4/14)×1.0 + (6/14)×0.650] = 0.965$$

Debt Attribute

high: 7
low: 7

$$Entropy(S_{high}) = -(3/7)×log₂(3/7) - (2/7)×log₂(2/7) - (2/7)×log₂(2/7) = 1.556$$
$$Entropy(S_{low}) = -(3/7)×log₂(3/7) - (1/7)×log₂(1/7) - (3/7)×log₂(3/7) = 1.449$$
$$Gain(S, Debt) = 1.530 - [(7/14)×1.556 + (7/14)×1.449] = 0.027$$

Reputation Attribute

bad: 3
unknown: 5
good:6

$$Entropy(S_{bad}) = 0 $$
$$Entropy(S\_{unknown}) = -(2/5)×log₂(2/5) - (1/5)×log₂(1/5) - (2/5)×log₂(2/5) = 1.522$$
$$Entropy(S_good) = -(1/6)×log₂(1/6) - (2/6)×log₂(2/6) - (3/6)×log₂(3/6) = 1.459$$
$$Gain(S, Reputation) = 1.530 - [(3/14)×0 + (5/14)×1.522 + (6/14)×1.459] = 0.361$$

From this, we can see the respective information gains of all features:

- Salary: 0.965
- Reputation: 0.361
- Security: 0.206
- Debt: 0.027

## Step 4: Build Decision Tree

We are going to build the decision tree with the root node being the highest information gain.

Salary
/ | \
 $0-30K $30K-60K over $60K
| | |
[4H,0M,0L] [2H,2M,0L] [0H,1M,5L]

```

### Branch 1: Salary = "$0 to $30K"
All 4 instances are High risk → **Leaf node: High**

### Branch 2: Salary = "$30K to $60K"
Need to split further. Calculate gain for remaining attributes:

Dataset: Instances 2, 3, 14 (2 high, 2 moderate)

Entropy = -(2/4)×log₂(2/4) - (2/4)×log₂(2/4) = 1.0

**Security:**
- none: [2H, 2M] → Entropy = 1.0
- adequate: [0H, 0M] → no instances

Gain = 1.0 - 1.0 = 0

**Debt:**
- high: [2H, 1M] → Entropy = 0.918
- low: [0H, 1M] → Entropy = 0

Gain = 1.0 - [(3/4)×0.918 + (1/4)×0] = 0.311

**Reputation:**
- bad: [1H, 0M] → Entropy = 0
- unknown: [1H, 1M] → Entropy = 1.0
- good: [0H, 1M] → Entropy = 0

Gain = 1.0 - [(1/4)×0 + (2/4)×1.0 + (1/4)×0] = 0.5

Best attribute: **Reputation** (Gain = 0.5)

### Branch 3: Salary = "over $60K"
Dataset: 6 instances (0 high, 1 moderate, 5 low)

Since the majority class is Low (5 out of 6), and entropy is relatively low (0.650), we could make this a leaf node: **Low**

However, for completeness, let's check if we can improve:

**Security:**
- adequate: [0H, 1M, 2L] → majority is Low
- none: [0H, 0M, 3L] → all Low

**Reputation:**
- bad: [0H, 1M, 0L] → Moderate
- unknown: [0H, 0M, 2L] → Low
- good: [0H, 0M, 3L] → Low

## Final Decision Tree
```

                         Salary
              /            |              \
         $0-30K       $30K-60K         over $60K
            |              |                |
          HIGH        Reputation           LOW
                     /    |    \
                  bad  unknown good
                   |      |     |
                 HIGH    HIGH  MODERATE
