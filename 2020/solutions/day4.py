from functools import reduce
from collections import defaultdict

passports = defaultdict(dict)
seen = set()
all_keys = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])
idx = 0
valid_nums = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
valid_hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
with open('day4.txt') as f:
    lines = f.readlines()
    for line in lines:
        if line.rstrip() == '':
            continue
        kv = line.split(" ")
        for pair in kv:
            pair = pair.rstrip()
            k, v = pair.split(":")
            if k in seen or len(seen) == len(all_keys):
                seen = set()
                idx += 1
            seen.add(k)
            passports[idx][k] = v

count = 1

def validate_hgt(hgt):
    units = hgt[-2:]
    if units == 'cm':
        val = hgt[:-2]
        val = int(val)
        return val >= 150 and val <= 193
    if units == 'in':
        val = hgt[:-2]
        val = int(val)
        return val >= 59 and val <= 76
    return False

def validate_hcl(hcl):
    if hcl[0] == '#':
        val = hcl[1:]
        if(len(val) == 6):
            for item in val:
                if item not in valid_hex:
                    return False
            return True
    return False

def validate_pid(pid):
    if len(pid) == 9:
        for item in pid:
            if item not in valid_nums:
                print(pid)
                return False
        return True
    return False

for number, passport in passports.items():
    if len(passport.keys()) == len(all_keys):
        if int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002 and len(passport['byr']) == 4 and \
            int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020 and len(passport['iyr']) == 4 and \
            int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030 and len(passport['eyr']) == 4 and \
            validate_hgt(passport['hgt']) and \
            validate_hcl(passport['hcl']) and \
            passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and \
            validate_pid(passport['pid']):
            count += 1
    elif len(passport.keys()) == len(all_keys) - 1:
        if 'cid' not in passport.keys():
            if int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002 and len(passport['byr']) == 4 and \
                int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020 and len(passport['iyr']) == 4 and \
                int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030 and len(passport['eyr']) == 4 and \
                validate_hgt(passport['hgt']) and \
                validate_hcl(passport['hcl']) and \
                passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and \
                validate_pid(passport['pid']):
                count += 1
print(count)
