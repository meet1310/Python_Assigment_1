class InvalidFormula(Exception):
    pass


class FormulaValidator:
    def validate(self, formula):
        if not formula.strip():
            raise InvalidFormula("Formula cannot be empty")

        if "=" not in formula:
            raise InvalidFormula("Formula must contain '='")

        left, right = formula.split("=", 1)

        if not left.strip() or not right.strip():
            raise InvalidFormula("Both sides are required")

        if not any(op in right for op in "+-*/"):
            raise InvalidFormula("No mathematical operator found")

        return True


# Main
validator = FormulaValidator()

n = int(input("Enter number of formulas: "))

for i in range(n):
    formula = input("Enter formula: ")

    try:
        validator.validate(formula)
        print("Valid Formula")

    except InvalidFormula as e:
        print("Invalid Formula:", e)