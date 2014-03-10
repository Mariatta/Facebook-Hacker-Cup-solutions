file = open("alphabet_soup.txt")
number_of_lines = int(file.readline())
line = 0
print ''
while line < number_of_lines :
    line = line + 1
    test_case = file.readline()
    chars = {}
        for character in test_case:
            if character != ' ':
                if chars.has_key(character):
                    chars[character] = chars[character] + 1
                else:
                    chars[character] = 1
    h = chars['H'] if chars.has_key('H') else 0
    a = chars['A'] if chars.has_key('A') else 0
    c = chars['C'] if chars.has_key('C') else 0
    k = chars['K'] if chars.has_key('K') else 0
    e = chars['E'] if chars.has_key('E') else 0
    r = chars['R'] if chars.has_key('R') else 0
    u = chars['U'] if chars.has_key('U') else 0
    p = chars['P'] if chars.has_key('P') else 0
    i = 0
    can_continue = True
    while can_continue :
        h = h-1
        a = a-1
        c = c-2
        k = k-1
        e = e-1
        r = r-1
        u = u-1
        p = p-1
        if h >=0 and a >=0 and c >=0 and k >=0 and e >=0 and r >=0 and u >=0 and p >=0 :
            i = i + 1
        else:
            can_continue = False
    print 'Case #%s: %s' % (line, i)