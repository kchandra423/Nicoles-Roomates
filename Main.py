from ortools.sat.python import cp_model
from ortools.sat.python.cp_model import VarArraySolutionPrinter


def main():
    # Create the model.
    m = cp_model.CpModel()

    # Create the variables.
    bin = m.NewBoolVar('Bin')
    nat = m.NewBoolVar('Nat')
    jason = m.NewBoolVar('Jason')
    kevin = m.NewBoolVar('Kevin')
    yugeon = m.NewBoolVar('Yugeon')


    # Assume there is a room with 3 people and the other has 2
    # A "true" value will indicate that this person is in the double, and a false will indicate they are in the other
    # Since the double can only fit 2 people, we know that the sum of all our terms will be 2
    # because a true value represents a 1, and a false value represents a 0

    m.Add(sum([bin, nat, jason, kevin, yugeon]) == 2)

    # Add the constraints.
    # Kevin must be in the double
    m.Add(kevin == True)

    # Yugeon and Jason cannot be in the same room (one of them must be in the double)
    m.Add(yugeon !=jason)
    # This code also works
    # m.AddBoolXOr(yugeon, jason)

    # Bin cant be with jason AND kevin
    # This means that the sum of the 3 terms must be at least 1 since
    # If the sum was 0 they would all be in the triple
    # And they all obvously cant be true because the double cant have 3 people
    m.Add(bin + jason + nat >= 1)

    # Create a solver and solve.
    solver = cp_model.CpSolver()
    # Not super neccesary, but just demonstrates there's only one solution
    solver.parameters.enumerate_all_solutions = True
    solution_printer = VarArraySolutionPrinter([bin, nat, jason, kevin, yugeon])

    solver.Solve(m, solution_printer)


if __name__ == '__main__':
    main()
