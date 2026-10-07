
class Particle:

    def __init__(self, x1, v1):
        self.x = x1
        self.v = v1

    def step(self, dt):
        self.x = self.x + dt * self.v
        print(f"The position is now {self.x}")

my_particle = Particle(1.0, 10.0)
my_part2 = Particle(2, -10)
#print(f"my_particle = {my_particle}")
print(f"    my_particle.x = {my_particle.x}")
print(f"    my_particle.v = {my_particle.v}")

for i in range(10):
    print(f"Particle 1: \n")
    my_particle.step(0.01)

    print(f"Particle 2: \n")
    my_part2.step(0.01)
    print("-----")

