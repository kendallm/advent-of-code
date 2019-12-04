from collections import Counter

def is_valid_password(passwd):
    password = str(passwd)
    prev_base = 1
    base = 10
    digits = []
    while base < 10000000:
        digit = (passwd % base) / (prev_base)
        digits.append(int(digit))
        prev_base = base
        base *= 10
    digits.reverse()
    
    for i, digit in enumerate(digits):
        if i == 0:
            continue
        if digits[i] < digits[i - 1]:
            return False
    
    for v in Counter(digits).values():
        if v == 2:
            return True

    return False
    

if __name__ == "__main__":
    # input range 264793-803935
    result = list(filter(is_valid_password, range(264793, 803935 + 1)))
    print(len(result))
    