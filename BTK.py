import time
import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


class BackTrackSolver:
    def __init__(self, data_table):
        self.variables = {}
        self.constraints = []
        self.unassigned_var = []
        self.data_table = data_table
        self.var_constraint = {}

    def add_variable(self, variable, domain):
        self.variables[tuple(variable)] = domain
        self.unassigned_var.append(tuple(variable))

    def add_constraint(self, constraint):
        self.constraints.append(constraint)

    def solve(self):
        solutions = []
        self.backtrack({}, solutions)
        return solutions

    def is_consistent(self, assignment):
        constraint_function = self.BT_constraint
        for constraint in self.constraints:
            variables = constraint
            if not constraint_function(*variables):
                return False
        return True

    def BT_constraint(self, variables, target_sum):
        assigned_values = [self.data_table[var[0]][var[1]] for var in variables if
                           self.data_table[var[0]][var[1]] != 0]
        # print("BTK", variables, assigned_values, target_sum)
        if len(assigned_values) != len(set(assigned_values)):
            # print("tekrari")
            return False
        if sum(assigned_values) > target_sum:
            # print("sum ziad")
            # print("assigned_values", assigned_values, target_sum)
            return False
        if len(assigned_values) == len(variables) and sum(assigned_values) != target_sum:
            # print("set shodane hame vali barabar nabodan shart")
            return False
        return True

    def is_consistent_var(self, var):
        # print("var constraint ", var, self.var_constraint[var])
        constraint_function = self.BT_constraint
        for i in self.var_constraint[var]:
            constraint = self.constraints[i]
            variables = constraint
            if not constraint_function(*variables):
                return False
        return True

    def backtrack(self, assignment, solutions):
        if len(assignment) == len(self.variables):
            solutions.append(assignment.copy())
            return
        # print("unassigned_var :", self.unassigned_var)
        var = self.unassigned_var[-1]
        # print("selected variable:", var)
        # print(self.unassigned_var)
        self.unassigned_var.pop(-1)

        # print("showing variables : ", self.variables[var], self.variables)
        for value in self.variables[var]:
            assignment[var] = value
            print("assigned variable:", len(assignment))
            # print("all variables :", self.variables)
            self.data_table[var[0]][var[1]] = value
            if self.is_consistent_var(var):
                self.backtrack(assignment, solutions)
                if len(solutions) == len(self.variables):
                    break
            self.data_table[var[0]][var[1]] = 0
            assignment.pop(var)
        self.unassigned_var.append(var)


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
