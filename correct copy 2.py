import random
import time
random_number = random.randint(1,3)

tf = random.randint(0,1)
if tf == 0:
    tf = False
else:
    tf = True

f = open('usernames.txt','a')
x = 1000
while x > 0:
    f.write(f'{x}\n')
    x = x - 7
   
f.close()


ghouls = ["zxc", "god", "ghoul", "mode","zitraks","dead","cursed","blessed","died","tears","kill me","hate","sad","immortal","eternal","despair","pain","loser","hollow","鶐"]
symbols = ["大","ル","玉","ィ","り","フ","Ѫ","༒"]


x = random.choice(ghouls)
y = random.choice(symbols)
nickname = 'x'
if tf == True:
    if random_number == 1:
        nickname = f'{y}{x}{y}'
    elif random_number == 2:
        nickname = y+x+y
        x = random.choice(ghouls)
        y = random.choice(symbols)
        nickname = f'{nickname}' + f'{x}{y}'
    elif random_number == 3:
        nickname = f'{y}{x}{y}'
        x = random.choice(ghouls)
        y = random.choice(symbols)
        nickname = f'{nickname}' + f'{x}{y}'
        x = random.choice(ghouls)
        y = random.choice(symbols)
        nickname = f'{nickname}' + f'{x}{y}'
elif tf == False:
    nickname = x = random.choice(ghouls)
print(nickname)