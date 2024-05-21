class TriangleChecker:
    def __init__(self, a, b, c):
        self.sides = [a, b, c]

    def check_triangle_validity(self):
        if any(side <= 0 for side in self.sides):
            return "Cannot form a triangle with non-positive side lengths."
        if any(not isinstance(side, (int, float)) for side in self.sides):
            return "Please enter only numbers for the side lengths."
        a, b, c = sorted(self.sides)
        if a + b > c:
            return "Yay, a triangle can be formed!"
        return "Unfortunately, a triangle cannot be formed with these side lengths."


checker = TriangleChecker(3, 4, 5)
print(checker.check_triangle_validity())
