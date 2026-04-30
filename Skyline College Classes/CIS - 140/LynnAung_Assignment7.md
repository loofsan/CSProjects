# Building a Classification Model

## Step 1: Calculate Initial Entropy

To measure the uncertainty of the dataset, we calculate its entropy based on the distribution of risk levels:

| Risk Level | Count  |
| ---------- | ------ |
| High       | 6      |
| Moderate   | 3      |
| Low        | 5      |
| **Total**  | **14** |

\[
Entropy(S) = -\left(\frac{6}{14}\right)\log_2\left(\frac{6}{14}\right) - \left(\frac{3}{14}\right)\log_2\left(\frac{3}{14}\right) - \left(\frac{5}{14}\right)\log_2\left(\frac{5}{14}\right)
\]

\[
\boxed{Entropy(S) = 1.531}
\]

---

## Step 2: Calculate Information Gain

Next, we are going to calculate the information gain which measures how much uncertainty is reduced by considering its features.

We are going to do that for each attribute:

### **Security**

| Security | Count | Class Distribution |
| -------- | ----- | ------------------ |
| Adequate | 3     | [0H, 1M, 2L]       |
| None     | 11    | [6H, 2M, 3L]       |

$$Entropy(S_{adequate}) = -(\frac{0}{3})\times\log_2(\frac{0}{3}) - (\frac{1}{3})\times\log_2(\frac{1}{3}) - (\frac{2}{3})\times\log_2(\frac{2}{3})$$

$$Entropy(S_{adequate}) = 0.918$$
$$Entropy(S_{none}) = -(\frac{6}{11})\times\log_2(\frac{6}{11}) - (\frac{2}{11})\times\log_2(\frac{2}{11}) - (\frac{3}{11})\times\log_2(\frac{3}{11})$$

$$Entropy(S_{none}) = 1.435$$
\[
Gain(S, Security) = 1.531 - \left[\frac{3}{14}\times0.918 + \frac{11}{14}\times1.435\right] = \boxed{0.206}
\]

---

### **Salary**

| Salary Range | Count | Class Distribution |
| ------------ | ----- | ------------------ |
| $0–$30K      | 4     | [4H, 0M, 0L]       |
| $30K–$60K    | 4     | [2H, 2M, 0L]       |
| Over $60K    | 6     | [0H, 1M, 5L]       |

$$Entropy(S_{0-30K}) = -(4/4)×log₂(4/4) = 0$$

$$Entropy(S_{30-60K}) = -(2/4)×log₂(2/4) - (2/4)×log₂(2/4) = 1.0$$

$$Entropy(S_{over60K}) = -(0/6)×log₂(0/6) - (1/6)×log₂(1/6) - (5/6)×log₂(5/6) = 0.650$$

\[
Gain(S, Salary) = 1.531 - \left[\frac{4}{14}\times0 + \frac{4}{14}\times1.0 + \frac{6}{14}\times0.650\right] = \boxed{0.965}
\]

---

### **Debt**

| Debt | Count | Class Distribution |
| ---- | ----- | ------------------ |
| High | 7     | [3H, 2M, 2L]       |
| Low  | 7     | [3H, 1M, 3L]       |

$$Entropy(S_{high}) = -(3/7)×log₂(3/7) - (2/7)×log₂(2/7) - (2/7)×log₂(2/7) = 1.556$$

$$Entropy(S_{low}) = -(3/7)×log₂(3/7) - (1/7)×log₂(1/7) - (3/7)×log₂(3/7) = 1.449$$

\[
Gain(S, Debt) = 1.531 - \left[\frac{7}{14}\times1.556 + \frac{7}{14}\times1.449\right] = \boxed{0.027}
\]

---

### **Reputation**

| Reputation | Count | Class Distribution |
| ---------- | ----- | ------------------ |
| Bad        | 3     | [3H, 0M, 0L]       |
| Unknown    | 5     | [2H, 1M, 2L]       |
| Good       | 6     | [1H, 2M, 3L]       |

$$Entropy(S_{bad}) = 0$$

$$Entropy(S_{unknown}) = -(2/5)×log₂(2/5) - (1/5)×log₂(1/5) - (2/5)×log₂(2/5) = 1.522$$

$$Entropy(S_{good}) = -(1/6)×log₂(1/6) - (2/6)×log₂(2/6) - (3/6)×log₂(3/6) = 1.459$$

\[
Gain(S, Reputation) = 1.531 - \left[\frac{3}{14}\times0 + \frac{5}{14}\times1.522 + \frac{6}{14}\times1.459\right] = \boxed{0.361}
\]

---

### Summary of Information Gains

| Attribute  | Information Gain |
| ---------- | ---------------- |
| **Salary** | **0.965**        |
| Reputation | 0.361            |
| Security   | 0.206            |
| Debt       | 0.027            |

We are going to build the decision tree with the root node being the highest information gain: **Salary**

---

## **Step 3: Build the Decision Tree**

### Root Node: Salary

```
                  ┌───────────────┐
                  │    Salary     │
                  └──────┬────────┘
                         │
     ┌───────────────────┼──────────────────────┐
     │                   │                      │
  $0–$30K           $30K–$60K             Over $60K
     │                   │                      │
  [4H,0M,0L]        [2H,2M,0L]             [0H,1M,5L]
     │                   │                      │
   HIGH           Split by Reputation           LOW
                         │
        ┌───────────┬───────────┬───────────┐
        │           │           │           │
       Bad       Unknown       Good      (others)
        │           │           │
      HIGH        HIGH       MODERATE
```

---

## **Final Decision Rules**

1. **If Salary = \$0–$30K → High Risk**
2. **If Salary = Over $60K → Low Risk**
3. **If Salary = \$30K–$60K:**
   - Reputation = Bad → High Risk
   - Reputation = Unknown → High Risk
   - Reputation = Good → Moderate Risk

---

### **Final Model Summary**

- **Root Node:** Salary (Highest Information Gain: 0.965)
- **Second Split (for $30K–$60K):** Reputation
- **Leaf Nodes:** High, Moderate, Low
- **Entropy Reduction:** Significant after Salary split
