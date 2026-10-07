file_name = "data/temps.txt"

with open(file_name, "r") as f:
    data = f.readlines()

print(f"data = {data}")

# first_temp = int(data[0].split()[0])
temps = [int(d.split()[0]) for d in data]
print(f"temps = {temps}")

def f_to_c(temp):
    return (temp - 32) * (5/9)

c_temps = [round(f_to_c(t),2) for t in temps]
c_temps_str = [f"{c}\n" for c in c_temps]
print(f"c_temps = {c_temps}")

new_file = "data/computed_c_temps.txt"

with open(new_file, "w") as f:
    f.writelines(c_temps_str)
