from functools import lru_cache
def next_output(outputs_list) -> int:
    res = 0
    for otp in outputs_list:
        outs = paths.get(otp)
        if outs[0] == 'out':
            res += 1
        else:
            res += next_output(outs)
    return res

# DFS with memoization
def next_output_2(outputs_list, fft_cntr, dac_cntr) -> int:
    has_fft = fft_cntr > 0
    has_dac = dac_cntr > 0
    return _next_output_2(tuple(outputs_list), has_fft, has_dac)

@lru_cache(maxsize=None)
def _next_output_2(outputs_tuple, has_fft: bool, has_dac: bool) -> int:
    res = 0
    for otp in outputs_tuple:
        cur_fft = has_fft or (otp == 'fft')
        cur_dac = has_dac or (otp == 'dac')

        if otp == 'out' and cur_fft and cur_dac:
            res += 1
        else:
            outs = paths.get(otp)
            if outs is None:
                continue
            res += _next_output_2(tuple(outs), cur_fft, cur_dac)
    return res

# read file
with open("input.txt", "r") as file:
    lines = [line.rstrip() for line in file]

paths = dict()

for l in lines:
    d = l.index(':')
    paths[l[:d]] = [otp for otp in l[d+2:].split()]

#print(paths)

path_cntr = 0
path_cntr2 = 0

fft_cntr = 0
dac_cntr = 0
for k, v in paths.items():
    if k == 'you':
        path_cntr = next_output(v)
    elif k == 'svr':
        path_cntr2 = next_output_2(v, fft_cntr, dac_cntr)
print(f'Part 1:{path_cntr}')
print(f'Part 2:{path_cntr2}')
