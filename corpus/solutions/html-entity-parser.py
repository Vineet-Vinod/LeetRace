class Solution:
    def entityParser(self, text: str) -> str:
        entities = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/",
        }
        result = []
        index = 0
        while index < len(text):
            if text[index] == "&":
                end = text.find(";", index + 1)
                entity = text[index : end + 1] if end != -1 else ""
                if entity in entities:
                    result.append(entities[entity])
                    index = end + 1
                    continue
            result.append(text[index])
            index += 1
        return "".join(result)
