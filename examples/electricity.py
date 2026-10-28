import temp
import math

import data.names as names
highs = [81, 83, 72, 90, 100]

highs_c = [temp.f_to_c(h) for h in highs]
print(highs_c)


def estimate_ac_from_high_c(temp_c):
    return math.exp(temp_c)

electric_bill = [estimate_ac_from_high_c(hc) for hc in highs_c]
print(f"electric_bill: {electric_bill}")

print(f"name1: {names.name1}")

print(f"name2: {names.name2}")