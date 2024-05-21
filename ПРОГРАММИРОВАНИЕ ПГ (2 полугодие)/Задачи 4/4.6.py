import numpy as np

class LinearEquationSystemSolver:

    def __init__(self, coefficients, constants):
        self.coefficients = np.array(coefficients)
        self.constants = np.array(constants)

    def find_solution(self):
        return np.linalg.solve(self.coefficients, self.constants)

coefficients = [[2, 1], [1, 3]]
constants = [8, 13]
solver = LinearEquationSystemSolver(coefficients, constants)
solution = solver.find_solution()
print(solution)
