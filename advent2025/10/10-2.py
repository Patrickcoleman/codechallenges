input = open("advent2025/10/data.txt")

machines = []

for line in input:
    raw_line = line.strip().split(" ")
    machine = {}
    buttons = []
    for data in raw_line:
        if '[' in data:
            lights = []
            for char in data:
                if char == '.':
                    lights.append(0)
                elif char == '#':
                    lights.append(1)
            machine['lights'] = lights
        elif '(' in data:
            button = []
            for char in data:
                if char not in ['(', ')',',']:
                    button.append(int(char))
            buttons.append(button)
        elif '{' in data:
            data = data[1:-1]
            joltages = data.split(',')
            machine['joltage'] = []
            for joltage in joltages:
                machine['joltage'].append(int(joltage))
    machine['buttons'] = buttons
    machines.append(machine)


running_mins = 0
machine_count = len(machines)
machine_number = 0

for machine in machines:
    machine_number += 1
    current_joltages = []
    seen_joltages = []
    next_joltages = [[0 for _ in range(len(machine['joltage']))]]
    target_joltages = machine['joltage']
    pushes = 0
    found = False
    
    while True:
        print(f"Machine {machine_number}/{machine_count}, button press {pushes+1}, next joltages {len(next_joltages)}")
        if found:
            running_mins += pushes
            break

        current_joltages = next_joltages.copy()
        next_joltages = []
        pushes += 1
        for joltage_set in current_joltages:
            for button in machine['buttons']:
                next_joltage = joltage_set.copy()
                for light in button:
                    next_joltage[light] += 1

                add = True
                good = True

                for i in range(len(next_joltage)):
                    if next_joltage[i] > target_joltages[i]:
                        add = False
                        good = False
                        break
                    elif next_joltage[i] != target_joltages[i]:
                        good = False
                
                if good:
                    found = True

                if add:
                    if next_joltage not in seen_joltages:
                        seen_joltages.append(next_joltage)
                        next_joltages.append(next_joltage)

print(running_mins)