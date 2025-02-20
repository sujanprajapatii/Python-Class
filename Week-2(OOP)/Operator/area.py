class Shapes:
    def __init__(self, no_sides):
        self.n = no_sides
        self.sides = [0 for _ in range(no_sides)]

    def take_sides(self):
        self.sides = [float(input(f"Enter side {i+1}: ")) for i in range(self.n)]

    def dis_sides(self):
        for i in range(self.n):
            print(f"Side {i+1} is {self.sides[i]}")

class Rec(Shapes):
    def __init__(self):
        super().__init__(2)  # A rectangle needs only 2 sides (length & breadth)

    def find_area(self):
        a, b = self.sides  # Extract length and breadth
        area = a * b  # Corrected formula for area
        print(f'The area of the rectangle is {area}')

# Example Usage:
r = Rec()
r.take_sides()
r.dis_sides()
r.find_area()