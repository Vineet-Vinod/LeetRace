class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        children: Dict[int, List[int]] = {}
        for process, parent in zip(pid, ppid):
            children.setdefault(parent, []).append(process)
        killed: List[int] = []
        stack = [kill]
        while stack:
            process = stack.pop()
            killed.append(process)
            stack.extend(children.get(process, []))
        return sorted(killed)
