n = int(input())
expr = {}

for _ in range(n):
    name, value = input().split("=", 1)
    expr[name.strip()] = value.strip()

target = input().strip()

memo = {}
visiting = set()


def solve_var(name):
    if name in memo:
        return memo[name]

    if name in visiting:
        raise Exception("CYCLE")

    if name not in expr:
        raise Exception("INVALID")

    visiting.add(name)

    try:
        value = eval_expr(expr[name])
        memo[name] = value
        visiting.remove(name)
        return value
    except:
        raise


def eval_expr(s):
    s = s.replace(" ", "")

    # Replace variables with their calculated values
    tokens = []
    i = 0

    while i < len(s):

        if s[i].isdigit():
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            tokens.append(s[i:j])
            i = j

        elif s[i].isalpha() or s[i] == "_":
            j = i
            while j < len(s) and (s[j].isalnum() or s[j] == "_"):
                j += 1
            tokens.append(str(solve_var(s[i:j])))
            i = j

        else:
            tokens.append(s[i])
            i += 1

    # Safe expression evaluation
    return eval("".join(tokens), {"_builtins_": None}, {})


try:
    print(eval_expr(target))

except Exception as e:
    if str(e) == "CYCLE":
        print("CYCLE")
    else:
        print("INVALID")