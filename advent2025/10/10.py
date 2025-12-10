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
            joltage = data.split(',')
            machine['joltage'] = joltage
    machine['buttons'] = buttons
    machines.append(machine)


running_mins = 0

for machine in machines:
    current_lights = []
    next_lights = [machine['lights'].copy()]
    pushes = 0
    found = False
    
    while True:
        if found:
            running_mins += pushes
            break

        current_lights = next_lights.copy()
        next_lights = []
        pushes += 1
        for light_set in current_lights:
            for button in machine['buttons']:
                next_light = light_set.copy()
                for light in button:
                    if next_light[light] == 1:
                        next_light[light] = 0
                    else:
                        next_light[light] = 1
                if sum(next_light) == 0:#
                    found = True
                    break
                else:
                    next_lights.append(next_light)



print(running_mins)