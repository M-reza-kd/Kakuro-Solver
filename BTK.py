class BackTrackSolver:
    def __init__(self):
        self.variables = {}
        self.constraints = []

    def add_variable(self, variable, domain):
        self.variables[variable] = domain

    def add_constraint(self, constraint):
        self.constraints.append(constraint)

    def solve(self):
        solutions = []
        self.backtrack({}, solutions)
        return solutions

    def is_consistent(self, assignment):
        for constraint in self.constraints:
            variables, constraint_function = constraint
            constrained_values = [assignment[var] for var in variables]
            if not constraint_function(*constrained_values):
                return False
        return True

    def backtrack(self, assignment, solutions):
        if len(assignment) == len(self.variables):
            solutions.append(assignment.copy())
            return

        unassigned_var = [
            var for var in self.variables if var not in assignment]
        var = unassigned_var[0]

        for value in self.variables[var]:
            assignment[var] = value
            if self.is_consistent(assignment):
                self.backtrack(assignment, solutions)
            assignment.pop(var)


# Example usage:
""" if __name__ == "__main__":
    csp_solver = MyCSPSolver()

    # Define variables and domains
    variables = ['A', 'B', 'C']
    domains = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}

    # Add variables and their domains to the solver
    for var in variables:
        csp_solver.add_variable(var, domains[var])

    # Define constraints (Example: A + B = C)
    def sum_constraint(a, b, c):
        return a + b == c

    constraint = (['A', 'B', 'C'], sum_constraint)
    csp_solver.add_constraint(constraint)

    # Solve the CSP
    solutions = csp_solver.solve()

    # Display solutions
    if solutions:
        print("Solutions found:")
        for solution in solutions:
            print(solution)
    else:
        print("No solutions found.")

 """
