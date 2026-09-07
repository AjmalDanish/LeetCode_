class Solution:
    def distinctSubseqII(self, s: str) -> int:

        MOD = 10**9 + 7

        dp = 1
        last = {}

        for ch in s:

            old_dp = dp

            dp = 2 * dp

            if ch in last:
                dp -= last[ch]

            dp %= MOD

            last[ch] = old_dp

        return (dp - 1) % MOD