import re

def partOne():
    validPassports = 0
    passports = getPassports()
    for passport in passports:
        if(checkPrimaryRule(passport)):
            validPassports += 1
    return(validPassports)

def partTwo():
    validPassports = 0
    passports = getPassports()
    for passport in passports:
        if(checkPrimaryRule(passport)):
            if(checkExtendedRules(passport)):
                validPassports += 1
    return(validPassports)

def getPassports():
    passports = [{}]
    with open('input.txt') as file:
        passportBatches = file.read().split('\n\n')
    for passportBatch in passportBatches:
        passport = {}
        passportBatch = passportBatch.replace('\n', ' ').rstrip()
        for batchField in passportBatch.split(' '):
            keyValuePair = batchField.split(':')
            passport[keyValuePair[0]] = keyValuePair[1]
        passports.append(passport)
    return passports

def checkPrimaryRule(passport):
    necessaryPassportKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return all(keys in passport.keys() for keys in necessaryPassportKeys)

def checkExtendedRules(passport):
    pidRegEx = '^[0-9]{9}$'
    hclRegEx = '^#[0-9a-f]{6}$'
    allowedEclTypes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    try:
        assert 1920 <= int(passport['byr']) <= 2002
        assert 2010 <= int(passport['iyr']) <= 2020
        assert 2020 <= int(passport['eyr']) <= 2030
        assert passport['hgt'][-2:] in ['cm', 'in']
        height = int(passport['hgt'][:-2])
        if(passport['hgt'][-2:] == 'cm'):
            assert 150 <= height <= 193
        else:
            assert 59 <= height <= 76
        assert re.compile(hclRegEx).match(passport['hcl'])
        assert passport['ecl'] in allowedEclTypes
        assert re.compile(pidRegEx).match(passport['pid'])
    except AssertionError:
        return False
    return True

print(partOne())
print(partTwo())
