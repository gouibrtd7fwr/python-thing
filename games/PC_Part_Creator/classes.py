from math import *

class CPU:
    def __init__(self, cores, threads, clock, max_clock, tdp, strength):
        self.cores = cores
        self.threads = threads
        self.clock = clock
        self.max_clock = max_clock
        self.tdp = tdp
        self.strength = strength
        pass

    def benchmark(self):
        self.score = self.threads * (self.strength ** 1.75) * (self.clock ** (1/5))
        print('Your SuperBenchmarkCPU 1.6.3 score is', self.score)
        pass
    pass

class GPU:
    def __init__(self, cores, clock, mem_clock, max_clock, strength, tdp):
        self.cores = cores
        self.clock = clock
        self.mem_clock = mem_clock
        self.max_clock = max_clock
        self.strength = strength
        self.tdp = tdp
        pass
    
    def benchmark(self):
        self.score = (self.cores ** 0.55) * (self.clock ** 0.2) * self.strength
        print('Your SuperBenchmarkGPU 2.0.5 score is', self.score)
        pass
    pass