message = ['CU', "see you", ':-)', "I'm happy", ':-(', "I'm unhappy", ';-)', "wink", ':-P', "stick out my tongue", '(~.~)', "sleepy", 'TA', "totally awesome", 'CCC', "Canadian Computing Competition", 'CUZ', "because", 'TY', "thank-you" 'YW', "you're welcome", 'TTYL', "talk to you later"]
a = input()
z = []
total = 0
while a != 'TTYL':
    try:
        num = message.index(a)
        z.append(message[num + 1])
        total += 1
    except:
        z.append(a)
        total += 1
    finally:
        a = input()
z.append('talk to you later')
for y in range(total+1):
    print(z[y])
