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

    def is_consistent(self):
        constraint_function = self.BT_constraint
        for constraint in self.constraints:
            variables = constraint
            if not constraint_function(*variables):
                return False
        return True

    def BT_constraint(self, variables, target_sum):
        assigned_values = [self.data_table[var[0]][var[1]] for var in variables if
                           self.data_table[var[0]][var[1]] != 0]
        if len(assigned_values) != len(set(assigned_values)):
            return False
        if sum(assigned_values) > target_sum:
            return False
        if len(assigned_values) == len(variables) and sum(assigned_values) != target_sum:
            return False
        return True

    def is_consistent_var(self, var):
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
        var = self.unassigned_var[-1]
        self.unassigned_var.pop(-1)

        for value in self.variables[var]:
            assignment[var] = value
            self.data_table[var[0]][var[1]] = value
            if self.is_consistent():
                self.backtrack(assignment, solutions)
                if len(solutions) == len(self.variables):
                    break
            self.data_table[var[0]][var[1]] = 0
            assignment.pop(var)
        self.unassigned_var.append(var)

