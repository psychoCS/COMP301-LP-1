import statistics as S
from fractions import Fraction as F

grades = [65, 75.8, 82.1, 83.00, 66, 77, 25, 100, 99, 86, 80]

grades = sorted(grades)

print(f"sorted grades: {grades}")

mean = S.mean(grades)
median = S.median(grades)
mode = S.mode(grades)

print(f"The Means is: {mean}")
print(f"The Median is: {median}")
print(f"The Mode is: {mode}")

half = F(1, 2)
print(half)
