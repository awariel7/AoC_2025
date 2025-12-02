# read file
with open("input.txt", "r") as file:
    lines = [line.rstrip() for line in file]
    for l in lines:
        ids = [d.split("-") for d in lines[0].split(',')]

print(ids)
total_sum_1 = 0
total_sum_2 = 0
for i in ids:
    for id_num in range(int(i[0]), int(i[1]) + 1):
        # start string
        s_id_num = str(id_num)
        len_s_id_num = len(s_id_num)
        # for every substring with length no more than half of the current string
        for j in range(len_s_id_num//2):
            # get substring
            word = s_id_num[0:j+1]
            # get possible repetitions
            if len_s_id_num%len(word) == 0:
                repetitions = len_s_id_num//len(word)
                if word * repetitions == s_id_num:
                    if flag_part_1 == False and repetitions == 2:
                        total_sum_1 += int(id_num)
                        flag_part_1 = True
                    if flag_part_2 == False:
                        total_sum_2 += int(id_num)
                        flag_part_2 = True
                    if flag_part_1 == True and flag_part_2 == True:
                        break
        flag_part_1 = False
        flag_part_2 = False
print(f'Part1: {total_sum_1}')
print(f'Part2: {total_sum_2}')
