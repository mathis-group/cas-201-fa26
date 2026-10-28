class Particle:
    def __init__(self, x, y, v_x, v_y):
        self.x = x # Position in the x axis
        self.y = y # Position in the y axis
        self.v_x = v_x # speed in the x direction
        self.v_y = v_y # speed in the y direction

    def time_step(self):
        self.x += self.v_x
        self.y += self.v_y

my_particle = Particle(0.0, 1.0, 1.0, 1.0)
my_ceiling = 2.0
my_floor = 0.0

for i in range(10):
    print(f"At time {i}, position is {my_particle.x, my_particle.y}")
    my_particle.time_step()
    # check for collision
    if (my_particle.y >= my_ceiling) or (my_particle.y <= my_floor):
        # flip direction if collision happens
        my_particle.v_y = -my_particle.v_y

    