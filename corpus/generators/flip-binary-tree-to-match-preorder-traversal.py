import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: tree has 1..100 nodes with unique values 1..n; voyages are unique permutations, generators construct connected trees."""
    rng = random.Random(seed)
    calls = {
        "candidate(root=tree_node([1, 2, 3]), voyage=[1, 3, 2])",
        "candidate(root=tree_node([1, 2]), voyage=[2, 1])",
    }
    while len(calls) < 600:
        size = rng.randint(1, 25)
        values = rng.sample(range(1, size + 1), size)
        tree: list[int | None] = [values[0]]
        children: list[list[int]] = [[] for _ in values]
        queue = [0]
        cursor = 0
        next_value = 1
        while next_value < size:
            parent = queue[cursor]
            cursor += 1
            slots = 1 if next_value == size - 1 else rng.randint(1, 2)
            if slots == 1 and rng.random() < 0.5:
                tree.extend([None, values[next_value]])
                child_index = next_value
                len(tree) - 1
                children[parent].append(child_index)
                queue.append(child_index)
                next_value += 1
            else:
                tree.append(values[next_value])
                children[parent].append(next_value)
                queue.append(next_value)
                next_value += 1
                if slots == 2 and next_value < size:
                    tree.append(values[next_value])
                    children[parent].append(next_value)
                    queue.append(next_value)
                    next_value += 1
                else:
                    tree.append(None)
        # Generate a valid preorder by independently choosing child order at every node.
        flips: set[int] = set()

        def traverse(node: int) -> list[int]:
            order = children[node][:]
            if len(order) == 2 and rng.random() < 0.5:
                order.reverse()
                flips.add(values[node])
            result = [values[node]]
            for child in order:
                result.extend(traverse(child))
            return result

        voyage = traverse(0)
        calls.add(f"candidate(root=tree_node({tree!r}), voyage={voyage!r})")
    return sorted(calls)
