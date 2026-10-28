samples = {"A1": 3.2, "B2": 4.7, "C3": 1.9}
print(f"samples['B2'] = {samples["B2"]}")

samples["A1"] = 5.0
samples["D4"] = 2.5
print(f"len(samples) = {len(samples)}")

print(f"C3 in samples = {"C3" in samples}")
print(f"samples.get('E5', 0) = {samples.get('E5', 0)}")

total = 0
for key in samples:
    total += samples[key]
print(f"total = {total:.2f}")