from subprocess import Popen, PIPE, STDOUT
import asyncio

def do_work(a, b, c, d, e):
    x = Popen(['/Users/kendall/.pyenv/shims/python', './aoc_day_7.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)

    inputs = [a, b, c, d, e]
    seed = "0\n"
    seeding = False
    idx = 0
    while x.poll() is None:
        child_output = x.stdout.readline().strip()
        child_output = child_output.decode("utf-8")
        if 'Input value' in child_output:
            if(seeding):
                x.stdin.write(bytes(seed, encoding="utf-8"))
            else:
                x.stdin.write(bytes(str(inputs[idx]) + "\n", encoding='utf-8'))
                idx += 1
            seeding = not seeding
            x.stdin.flush()
        elif child_output.strip() != "":
            seed = child_output.strip() + "\n"
    x.stdout.close()
    x.stdin.close()
    print(a,b,c,d,e)
    return int(seed.strip())

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

# print(do_work(0,1,2,3,4))
# print(do_work_feedback_loop(9,7,8,5,6))
maximum = 0
for a in range(5, 10):
    for b in range(5, 10):
        if a == b:
            continue
        for c in range(5, 10):
            if c == a or c == b:
                continue
            for d in range(5, 10):
                if d == a or d == b or d == c:
                    continue
                for e in range(5, 10):
                    if e == a or e == b or e == c or e == d:
                        continue
                    # print(a, b, c, d, e)
                    val = do_work_feedback_loop(a, b, c, d, e)
                    maximum = max(val, maximum)
# for a in range(5):
#     for b in range(5):
#         if a == b:
#             continue
#         for c in range(5):
#             if c == a or c == b:
#                 continue
#             for d in range(5):
#                 if d == a or d == b or d == c:
#                     continue
#                 for e in range(5):
#                     if e == a or e == b or e == c or e == d:
#                         continue
#                     val = do_work(a, b, c, d, e)
#                     maximum = max(val, maximum)

print(maximum)