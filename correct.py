import random
import time
random_number = random.randint(1,3)


tf = random.randint(0,1)
if tf == 0:
    tf = False
else:
    tf = True

f = open('ghouls.txt','a',encoding='utf8')

# x = 1000
# while x > 0:
#     f.write(f'{x}\n')
#     x = x - 7

ghouls = ["zxc", "god", "ghoul", "mode","zitraks","dead","cursed","blessed","died","tears","kill me","hate","sad","immortal","eternal","despair","pain","loser","hollow"]
symbols = ["ル","玉","ィ","り","フ","Ѫ",]
nickname = 'x'

x = random.choice(ghouls)
y = random.choice(symbols)
def Infinity():
    while True:
        random_number = random.randint(1,3)
        x = random.choice(ghouls)
        y = random.choice(symbols)

        tf = random.randint(0,1)
        if tf == 0:
            tf = False
        else:
            tf = True
        
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
            nickname = random.choice(ghouls)
        f.write(f'{nickname}\n')

def impulse(x):
    for i in range(x):
            random_number = random.randint(1,3)
            x = random.choice(ghouls)
            y = random.choice(symbols)

            tf = random.randint(0,1)
            if tf == 0:
                tf = False
            else:
                tf = True
            
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
                nickname = random.choice(ghouls)
            f.write(f'{nickname}\n')



TEST = int(input('ПРИВЕТ ЕБНУТЫЙ ДЕД ИНСАЙД ТЫСЯЧА МИНУС СЕМЬ 97 ПРИВЕТ ВЫБИРАЙ 1(вечные ники) ИЛИ 2(сам выбираешь сколько) '))
if TEST == 1:
    Infinity()
elif TEST == 2:
    numb = int(input('ЧЕ ЕБЛАН СКОЛЬКО ТЕБЕ НИКОВЗХЗЫФЩХВЩХФЫЗВЩХЗФЫ: '))
    impulse(numb)