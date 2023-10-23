def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    elif len(s1) == 1:
        return s1 == s2
    else:
        return (s1[0] in s2) and is_anagram(s1[1:], s2.replace(s1[0], '', 1))
print(is_anagram("silent", "listen"))