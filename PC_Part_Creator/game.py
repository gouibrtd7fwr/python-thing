from classes import CPU, GPU

running = True
while running:
    creator = input('C for CPU creator, G for GPU creator')
    if creator.lower() == 'c':
        cores = int(input('Cores:'))
        threads = int(input('Threads:'))
        clock = int(input('Clock (MHz):'))
        max_clock = int(input('Max Clock (MHz):'))
        tdp = int(input('Wattage:'))
        strength = float(input('Strength: (this number will scale for better cpus guys!, but start lower!)'))
        cpu = CPU(cores, threads, clock, max_clock, tdp, strength)
        benchmark = input('Do you want to run a benchmark on this CPU? (y/n)')
        if benchmark.lower() == 'y':
            cpu.benchmark()
