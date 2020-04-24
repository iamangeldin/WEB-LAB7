#####  HW 8   #####
import math
##########################################
print('Task 17.2')
p_one = 150/178
print(p_one)
p_two = 27/52
print(p_two)
odds_one = p_one/(1 - p_one)
print(odds_one)
odds_two = p_two/(1 - p_two)
print(odds_two)

############################################
print('Task 17.4')
math.log10(odds_one)
print(math.log10(odds_one))
math.log10(odds_two)
print(math.log10(odds_two))

###########################################
print('Task 17.6')
b_0 = math.log10(odds_two)
print(b_0)
b_1 = math.log10(odds_one) - b_0
print(b_1)
odds_ratio = math.exp(b_1)
print(odds_ratio)

##########################################
