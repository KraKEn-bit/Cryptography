# Simple PRNG using Linear Congruential Generator (LCG)

class LCG_PRNG:
    def __init__(self, seed: int):
        # Parameters for LCG (commonly used values)
        self.a = 1664525      # multiplier
        self.c = 1013904223   # increment
        self.m = 2**32        # modulus
        self.state = seed     # seed / starting value

    def next(self) -> int:
        """Generating the next pseudo-random number"""
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def next_float(self) -> float:
        """Generating a pseudo-random float between 0 and 1"""
        return self.next() / self.m


prng = LCG_PRNG(seed=12345)

for _ in range(5):
    print(prng.next())     
