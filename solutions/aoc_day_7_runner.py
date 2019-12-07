from subprocess import Popen, PIPE, STDOUT
import itertools
from tqdm import tqdm

def do_work_feedback_loop(a, b, c, d, e):
    x = Popen(['/Users/kendall/.pyenv/shims/python', './aoc_day_7_feedback_loop.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)

    inputs = [a, b, c, d, e]
    seed = "0"
    seeding = False
    idx = 0
    while x.poll() is None:
        child_output = x.stdout.readline().strip()
        child_output = child_output.decode("utf-8")
        # print(f"s {seed}")
        if 'Input value' in child_output:
            if(seeding):
                x.stdin.write(bytes(seed, encoding="utf-8"))
                x.stdin.write(b"\n")
            else:
                x.stdin.write(bytes(str(inputs[idx]), encoding='utf-8'))
                x.stdin.write(b"\n")
                idx += 1
            if(idx < 5):
                seeding = not seeding
            else:
                seeding = True
            x.stdin.flush()
        elif child_output.strip() != "":
            seed = child_output.strip()

    x.stdout.close()
    x.stdin.close()
    return int(seed.strip())

maximum = 0
codes = list(itertools.permutations(range(5)))
for [a, b, c, d, e] in tqdm(codes, total=len(codes)):
    val = do_work_feedback_loop(a, b, c, d, e)
    maximum = max(val, maximum)
print(f'\npart 1 {maximum}')

maximum = 0
codes = list(itertools.permutations(range(5, 10)))
for [a, b, c, d, e] in tqdm(codes, total=len(codes)):
    val = do_work_feedback_loop(a, b, c, d, e)
    maximum = max(val, maximum)
print(f'\npart 2 {maximum}')