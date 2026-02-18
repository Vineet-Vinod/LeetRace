"""Shared utility functions for the LeetRace server."""

import re

# Maps ASCII digits to their Unicode superscript equivalents.
_SUP_DIGITS = str.maketrans("0123456789", "\u2070\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079")


def fix_exponents(text: str) -> str:
    """Convert exponent notation in problem descriptions to Unicode superscripts.

    Handles two forms that appear after scraping LeetCode HTML:
    - Explicit caret:  '10^5'  → '10⁵',  '2^31' → '2³¹'
    - Collapsed form:  '105'   → '10⁵'   (standalone base-10 exponents 4–9)
    - Collapsed 2^31/32: '231' → '2³¹',  '232'  → '2³²'
    """
    # Explicit carets: 10^5 → 10⁵
    text = re.sub(
        r"(\d+)\^(\d+)",
        lambda m: m.group(1) + m.group(2).translate(_SUP_DIGITS),
        text,
    )
    # Collapsed base-10 exponents: standalone 10[4-9] → 10⁴..10⁹
    text = re.sub(
        r"(?<!\d)(-?)10([4-9])(?!\d)",
        lambda m: m.group(1) + "10" + m.group(2).translate(_SUP_DIGITS),
        text,
    )
    # Collapsed 2^31 / 2^32: standalone 231 or 232 → 2³¹ or 2³²
    text = re.sub(
        r"(?<!\d)(-?)2(3[12])(?!\d)",
        lambda m: m.group(1) + "2" + m.group(2).translate(_SUP_DIGITS),
        text,
    )
    return text
