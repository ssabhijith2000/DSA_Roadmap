def reverse(strng):
    if len(strng) < 1:
        return strng
    return strng[-1] + reverse(strng[0:-1])


print(reverse('python'))  # 'nohtyp'
print(reverse('appmillers'))  # 'srellimppa'
