class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        counts: dict[str, int] = {}
        for message, sender in zip(messages, senders):
            counts[sender] = counts.get(sender, 0) + message.count(" ") + 1
        return max(counts, key=lambda name: (counts[name], name))
