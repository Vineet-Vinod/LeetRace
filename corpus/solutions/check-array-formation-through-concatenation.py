class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        starts = {piece[0]: piece for piece in pieces}
        index = 0
        while index < len(arr):
            piece = starts.get(arr[index])
            if piece is None or arr[index : index + len(piece)] != piece:
                return False
            index += len(piece)
        return True
