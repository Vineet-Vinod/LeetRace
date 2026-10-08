class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP:
            parts = queryIP.split(".")
            if len(parts) != 4:
                return "Neither"
            for part in parts:
                if (
                    not part
                    or (len(part) > 1 and part[0] == "0")
                    or not part.isdigit()
                    or int(part) > 255
                ):
                    return "Neither"
            return "IPv4"
        if ":" in queryIP:
            parts = queryIP.split(":")
            if len(parts) != 8:
                return "Neither"
            allowed = set("0123456789abcdefABCDEF")
            if all(
                1 <= len(part) <= 4 and all(char in allowed for char in part)
                for part in parts
            ):
                return "IPv6"
        return "Neither"
