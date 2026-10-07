class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        address = 0
        for part in ip.split("."):
            address = (address << 8) | int(part)
        blocks: list[str] = []
        remaining = n
        while remaining:
            alignment = 32 if address == 0 else (address & -address).bit_length() - 1
            size_power = min(alignment, remaining.bit_length() - 1)
            prefix = 32 - size_power
            octets = [(address >> shift) & 255 for shift in (24, 16, 8, 0)]
            blocks.append(".".join(map(str, octets)) + "/" + str(prefix))
            block_size = 1 << size_power
            address += block_size
            remaining -= block_size
        return blocks
