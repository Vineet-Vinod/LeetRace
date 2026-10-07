class Solution:
    def evaluate(self, expression: str) -> int:
        tokens = expression.replace("(", "( ").replace(")", " )").split()
        index = 0

        def parse():
            nonlocal index
            token = tokens[index]
            index += 1
            if token != "(":
                return token
            items = []
            while tokens[index] != ")":
                items.append(parse())
            index += 1
            return items

        def evaluate(node, env):
            if isinstance(node, str):
                return int(node) if node.lstrip("-").isdigit() else env[node]
            op = node[0]
            if op == "add":
                return evaluate(node[1], env) + evaluate(node[2], env)
            if op == "mult":
                return evaluate(node[1], env) * evaluate(node[2], env)
            local = env.copy()
            for i in range(1, len(node) - 1, 2):
                local[node[i]] = evaluate(node[i + 1], local)
            return evaluate(node[-1], local)

        return evaluate(parse(), {})
