class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        graph: dict[str, set[str]] = {}
        for a, b in synonyms:
            graph.setdefault(a, set()).add(b)
            graph.setdefault(b, set()).add(a)
        choices: dict[str, list[str]] = {}
        for word in graph:
            if word in choices:
                continue
            component = set()
            stack = [word]
            while stack:
                current = stack.pop()
                if current in component:
                    continue
                component.add(current)
                stack.extend(graph[current] - component)
            options = sorted(component)
            for member in component:
                choices[member] = options
        sentences = [""]
        for word in text.split():
            options = choices.get(word, [word])
            sentences = [
                prefix + (" " if prefix else "") + option
                for prefix in sentences
                for option in options
            ]
        return sorted(sentences)
