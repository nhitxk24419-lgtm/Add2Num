"""
MyBigNumber - Core module for adding two large numbers represented as strings.
Algorithm mirrors elementary school addition (right to left, with carry).

Uses pre-allocated array and fills from right to left for O(n) performance.
"""

import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


class MyBigNumber:
    """Provides big-number arithmetic using string representations."""

    def sum(self, stn1: str, stn2: str) -> str:
        """
        Add two non-negative integers represented as strings.

        The algorithm:
          1. The result has at most max(len(stn1), len(stn2)) + 1 digits.
          2. Pre-allocate a list of that size filled with '0'.
          3. Walk both inputs from right to left, writing each result
             digit directly into its correct position in the list.
          4. Join the list → done.

        Parameters
        ----------
        stn1 : str  First number (digits only).
        stn2 : str  Second number (digits only).

        Returns
        -------
        str  The sum as a string.
        """
        logger.info("sum() called with stn1=%r, stn2=%r", stn1, stn2)

        len1 = len(stn1)
        len2 = len(stn2)
        max_len = max(len1, len2) + 1          # +1 for possible carry

        # Pre-allocate result array, filled with '0'
        result = ['0'] * max_len

        carry = 0
        # k = write position in result (starts at the rightmost slot)
        k = max_len - 1
        i = len1 - 1
        j = len2 - 1
        step = 1

        while i >= 0 or j >= 0 or carry:
            digit1 = int(stn1[i]) if i >= 0 else 0
            digit2 = int(stn2[j]) if j >= 0 else 0

            carry_in = carry
            total = digit1 + digit2 + carry
            carry = total // 10
            digit_out = total % 10

            logger.debug(
                "Step %d: digit1=%d  digit2=%d  carry_in=%d  "
                "total=%d  digit_out=%d  carry_out=%d",
                step, digit1, digit2, carry_in,
                total, digit_out, carry,
            )

            # Write directly to correct position
            result[k] = str(digit_out)

            k -= 1
            i -= 1
            j -= 1
            step += 1

        # If there was no final carry, result[0] is still '0' → skip it
        output = "".join(result) if result[0] != '0' else "".join(result[1:])

        logger.info("Result: %s + %s = %s", stn1, stn2, output)
        return output
