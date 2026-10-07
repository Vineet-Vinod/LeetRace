class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        while read < len(chars):
            end = read + 1
            while end < len(chars) and chars[end] == chars[read]:
                end += 1
            chars[write] = chars[read]
            write += 1
            length = end - read
            if length > 1:
                for digit in str(length):
                    chars[write] = digit
                    write += 1
            read = end
        return write
