class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        answer = []
        for path in sorted(folder):
            if not answer or not path.startswith(answer[-1] + "/"):
                answer.append(path)
        return answer
