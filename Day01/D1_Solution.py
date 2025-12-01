# read file
with open("input.txt", "r") as file:
    lines = [line.rstrip() for line in file]

# no need in dial info, cause position equals value
# dial = [n for n in range(100)]
zero_counter = 0
total_rotations_counter = 0
# The dial starts by pointing at 50.
current_position = 50
# count of full rotations on dial
rotations = 0

for l in lines:
    direction = l[0]
    # from step exclude full circles
    # remember 4 full rotations
    rotations += (int(l[1:])//100)
    # from 449 leave only 49
    step = int(l[1:]) - rotations*100
    if direction == 'R':
        current_position += step
        if current_position > 99:
            # don't add current 0 position to rotations
            if current_position%100 != 0:
                rotations += current_position//100
            current_position = current_position%100
    else:
        prev_position = current_position
        current_position -= step
        if current_position < 0:
            # don't add start 0 position to rotations
            if prev_position != 0:
                rotations += 1
            current_position += 100
    # update total rotations
    total_rotations_counter += rotations
    # update total zero positions counter
    if current_position == 0:
        zero_counter += 1
    # reset rotation counters
    rotations = 0
print(f'Part1: {zero_counter}')
print(f'Part2: {zero_counter + total_rotations_counter}')



