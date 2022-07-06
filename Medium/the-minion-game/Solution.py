def minion_game(string):
    vowels = 'AEIOU'
    kev = 0
    stu = 0
    for x in range(len(string)):
        if s[x] in vowels:
            kev+=len(s)-x
        else:
            stu+=len(s)-x
    if kev>stu:
        print("Kevin",kev)
    elif kev<stu:
        print("Stuart", stu)
    else:
        print("Draw")