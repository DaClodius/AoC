import re

def part_one():
    valid_passports = 0
    for passport in get_passports():
        if check_primary_rule(passport):
            valid_passports += 1
    return valid_passports

def part_two():
    valid_passports = 0
    for passport in get_passports():
        if check_primary_rule(passport) and check_extended_rules(passport):
            valid_passports += 1
    return valid_passports

def get_passports():
    passports = [{}]
    with open('input/day4') as _file:
        passport_batches = _file.read().split('\n\n')
    for passport_batch in passport_batches:
        passport = {}
        for batch_field in re.split(' |\n', passport_batch.rstrip()):
            passport[batch_field.split(':')[0]] = batch_field.split(':')[1]
        passports.append(passport)
    return passports

def check_primary_rule(passport):
    return all(keys in passport.keys() for keys in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

def check_extended_rules(passport):
    try:
        assert 1920 <= int(passport['byr']) <= 2002
        assert 2010 <= int(passport['iyr']) <= 2020
        assert 2020 <= int(passport['eyr']) <= 2030
        assert passport['hgt'][-2:] in ['cm', 'in']
        height = int(passport['hgt'][:-2])
        if(passport['hgt'][-2:] == 'cm'):
            assert 150 <= height <= 193
        else: assert 59 <= height <= 76
        assert re.compile('^#[0-9a-f]{6}$').match(passport['hcl'])
        assert passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        assert re.compile('^[0-9]{9}$').match(passport['pid'])
    except AssertionError:
        return False
    return True

print(part_one())
print(part_two())
