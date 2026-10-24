def resolver(graph):
    visited = set()
    order = []

    def dfs(module):
        if module in visited:
            return

        visited.add(module)

        for dependency in graph.get(module, []):
            dfs(dependency)

        order.append(module)

    for module in graph:
        dfs(module)

    return order


# Main
n = int(input("Enter number of modules: "))

graph = {}

for i in range(n):
    module = input("Enter module name: ")
    deps = input("Enter dependencies: ").split()
    graph[module] = deps

try:
    result = resolver(graph)

    print("\nLoading Order:")
    print(" -> ".join(result))

except Exception as e:
    print("Error:", e)