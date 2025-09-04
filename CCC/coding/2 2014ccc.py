num = int(input())
votes = input()
votesA = int(votes.count('A'))
votesB = int(votes.count('B'))
if votesB > votesA:
    print('B')
elif votesA > votesB:
    print('A')
else:
    print('Tie')