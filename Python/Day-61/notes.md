# Day 61 — ML Foundations

## 1. What is Machine Learning?

Machine learning is a way of getting a computer to make predictions by
learning patterns from data, instead of me writing explicit rules for
every situation. In traditional programming, I write the rules myself
(e.g. `if marks >= 40: pass`) and the computer just applies them. In
machine learning, I give the computer data and examples, and it figures
out the pattern (the "model") on its own, which it then uses to make
predictions on new, unseen data.

## 2. Types of ML

| Type          | Learns from        | Example               |
|---------------|---------------------|------------------------|
| Supervised    | Labeled data         | Spam detection         |
| Unsupervised  | Unlabeled data        | Customer clustering    |
| Reinforcement | Rewards/penalties     | Game AI                |

## 3. Features & Labels

Example given:
```
Hours studied → Exam score
2 → 45
4 → 55
6 → 70
8 → 85
```
- Feature: Hours studied
- Label/Target: Exam score

My own examples:

1. **House size (sq. ft.) → House price**
   - Feature: size of the house
   - Label: price of the house

2. **Number of hours slept → Focus score at work**
   - Feature: hours slept
   - Label: focus score
