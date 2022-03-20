import discord
import asyncio
import time
import random
import datetime
import pytz
import sys
from exitstatus import ExitStatus
import time

chaton = True #setup
adminlist = ['']
t1 = 0
second = 0
minute = 0
hour = 0
day = 0
t2 = 0
t3 = 0
t4 = 0
t5 = 0
cooltime1 = 0
t6 = 0
t7 = 0
t8 = 0
t9 = 0
t10 = 0
t11 = 0
t12 = 0
t13 = 0
t14 = 0
pracinfo = 0
t15 = 0
t16 = 0
user = 0
url = ""
with open("bitcoin-price.txt", 'r') as readBTC:
    bitcoin = int(readBTC.readline())
yes = ['yes', 'Yes', 'Y', 'y', '네', 'YES']
no = ['no', 'N', '아니요', '아니오', 'NO', 'n']
history = []
practiced = ['안녕', '디보']
playing = True
blacklist = ['즘', '틱', '늄', '슘', '퓸', '늬', '뺌', '섯', '숍', '튼', '름', '늠', '쁨']
sgame = False
prefix = "!"
pw1 = 0
path = "cromedriver.exe"
fuck = True
numud = 0
song_tkdtn = "https://www.youtube.com/watch?v=wbHweCdCRQE"
ranud = 0
runtime = 0
nums = []
cb = False
wt = False
pw = 0
c = 1
detfuck = False
adminsay = 0
admincheck = 0
admin = ['DIBO | 디보', 'ko_Kr_gg ( | 코르 1세 | )', '유보 (YOU-BO)']
position = "원활"
firstime = time.time()
secondtime = time.time()
wtm = False
admin_1 = 0
blackuserlist = [1]
admin_2 = 0
bankey = True
admin_3 = 0
admin_4 = 0
bothap = 0
is_closed = False
hook = 0
money = 0
uptime = 0

client = discord.Client()

with open("token.txt", "r") as file:
    token = file.read()
    print(token)

@client.event #start
async def on_ready():
    global bitcoin
    global uptime
    global minute
    global hour
    global day
    global second

    print('Logged in! start DIBO - bot v2 \n welcome!')
    game = discord.Game(name=f'{len(client.guilds)}개의 서버에서 사용되어지는 중', url='https://www.twitch.tv/gguni1118')
    await client.change_presence(status=discord.Status.online, activity=game)

    while not client.is_closed():
        while True:
            second += 1
            if second >= 60:
                minute += 1
                second = 0
            elif minute >= 60:
                minute = 0
                hour += 1
            elif hour >= 24:
                day += 1
                hour = 0
            game = discord.Game(name=f'{len(client.guilds)}개의 서버에서 사용되어지는 중', url='https://www.twitch.tv/gguni1118')
            await client.change_presence(status=discord.Status.online, activity=game)
            await asyncio.sleep(1)
        

@client.event #command
async def on_message(message):
    global admincheck
    global firstime
    global secondtime
    global bitcoin
    global runtime
    global t1
    global t2
    global t3
    global t4
    global is_closed
    global t5
    global t6
    global t7
    global pracinfo
    global uptime
    global t8
    global t9
    global t10
    global t11
    global t12
    global t13
    global t14
    global t15
    global t16
    global pw1
    global c
    global bankey
    global cb
    global cooltime1
    global pw
    global prefix
    global ranud
    global user
    global blackuserlist
    global hook
    global sgame
    global url
    global chaton
    global wt
    global detfuck
    global bothap
    global money
    if message.content == prefix + "종료":
        if message.author.name == "노현균":
            await message.reply(f'{message.author.name} 님의 요청으로 봇이 종료되었습니다 ! \n!시작 으로 재시작 하실 수 있습니다')
            is_closed = True
    
    if message.content == prefix + "시작":
        if message.author.name == "노현균":
            await message.reply(f'{message.author.name} 님의 요청으로 봇이 시작되었습니다 !')
            is_closed = False

    if message.content == prefix + "봇":
        if is_closed != True:
            firstime = time.time()
            await message.reply("RUNTIME 측정중...")
            secondtime = time.time()
            runtime1 = secondtime - firstime
            runtime = round(runtime1, 2)
            if runtime < 0.4:
                position = "매우 원활"
            if 0.41 < runtime < 0.5:
                position = "매우 원활"
            if 0.51 < runtime < 0.6:
                position = "원활"
            if 0.61 < runtime < 0.65:
                position = "원활"
            if 0.66 < runtime < 0.69:
                position = "양호"
            if 0.7 < runtime:
                position = "혼잡"
            embed = discord.Embed(title="[ 봇 ]", description="DI-BOT", color=0x00ff00)
            embed.add_field(name="[ 봇 ]", value=f"현재 봇의 상태는 {position} 합니다!", inline=False)
            embed.add_field(name="[ RUNTIME ]", value=f"{runtime} ms", inline=False)
            embed.add_field(name="[ ✏️ 소개 ]", value=f"봇 이름 - 디보(DIBO) | DI-BO", inline=False)
            embed.add_field(name="[ 채팅 로그 ]", value="채팅 로그는 서버 파일에 1주일동안 기록된 후 지워집니다 ( 채팅 로그는 개인의 목적으로 열람하지 않습니다 )", inline=False)
            embed.add_field(name="[ 제작자 유튜브 ]", value="[제작자 유튜브 링크](<https://www.youtube.com/channel/UCLxuaPUJvnFHvuChjQquJUA>)", inline=False)
            embed.set_footer(text="노현균#4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.reply(embed=embed)
    
    if message.content == prefix + "invite":
        invite = await message.channel.create_invite()
        await message.reply(f'{invite}')


    if ((message.content == prefix + "업타임") or (message.content.startswith (prefix + "업타임"))):
        if is_closed != True:
            uptime = (f'`{day} 일 {hour} 시간 {minute} 분 {second} 초`')
            await message.reply(f'{uptime}')
    
    if message.content.startswith (prefix + "입금"):
        if is_closed != True:
            if message.content.startswith (prefix + "입금 "):
                willgivemoney = int(message.content.split(' ')[1])
                target = message.content.replace(prefix + f'입금 {willgivemoney} ' , "")
                roomId = message.guild.id
                target0 = message.author.id
                with open(f'{roomId},{target0}_money.txt', 'r') as readMoney:
                    money = int(readMoney.readline())
                    if money >= willgivemoney:
                        money -= willgivemoney
                        target11 = target.replace('<@', '').replace('>', '').replace('!', '')
                        with open(f'{roomId},{target0}_money.txt', 'w') as setMoney:
                            setMoney.write(f'{money}')
                            with open(f'{roomId},{target11}_money.txt', 'r') as readMoney:
                                money = int(readMoney.readline())
                                money += willgivemoney
                                with open(f'{roomId},{target11}_money.txt', 'w') as setMoney:
                                    setMoney.write(f'{money}')
                                    await message.reply(f'{message.author.name} 님이 {willgivemoney} 원 만큼 {target} 님에게 입금하였습니다!')
                    else:
                        await message.reply("돈이 부족합니다!")

    if message.content != "spdifsdofisdpo":
        if is_closed != True:
            user = message.author
            guild = message.guild.name
            log = str("[ SERVER : " + guild + " ] [ Name : " + str(user.name) + "( " + str(user.id) + " ) ] : " + message.content)
            with open("chatlog.txt", 'a', encoding='utf-8') as chattinglog:
                chattinglog.write(f"{log}\n")
    
    if message.content.startswith (prefix + "ev "):
        name = message.author.name
        if name == "노현균":
            try:
                command = message.content.replace(prefix + "ev ", "")
                com = eval(command)
                await message.reply("명령어 수행을 완료 하였습니다!\n실행 결과 : " + str(com))
            except (TimeoutError, OSError, ValueError, RuntimeError, TypeError, NameError, SyntaxError, AttributeError) as error:
                await message.reply(f"에러가 발생했습니다! \n{error}")
    
    if message.content == prefix + "길드원수":
        if is_closed != True:
            await message.reply(message.guild.member_count)
        
    if message.content == prefix + "가입":
        if is_closed != True:
            try:
                roomId = message.guild.id
                userId = message.author.id
                targetId = f'{roomId},{userId}'
                with open(f'{targetId}_money.txt', 'r') as targetMoney:
                    targetMoney.readline()
                    await message.reply("이미 가입이 완료된 유저입니다.")
            except(FileNotFoundError):
                roomId = message.guild.id
                userId = message.author.id
                targetId = f'{roomId},{userId}'
                with open(f'{targetId}_money.txt', 'w') as targetmoney:
                    targetmoney.write("1000")
                    await message.reply("축하드립니다 가입을 완료하였습니다\n지원금 1000원을 드립니다")
                    await message.reply("!돈 또는 ㄷㅇ 으로 자신의 현재 돈을 확인 하실 수 있습니다")
                with open(f'{targetId}_bank.txt', 'w') as bank:
                    bank.write("0")
                    await message.reply("통장이 개설되었습니다")
                with open(f'{targetId}_profile.txt', 'w') as userStatus:
                    userStatus.write("PERMISSION")
    
    if message.content == prefix + "hellothisisverification":
        await message.reply("노현균#4371")
    
    if message.content == prefix + "명령어":
        if is_closed != True:
            await message.reply("(접두사 X)ㄷㅇ : 자신의 현재 돈을 확인 | (접두사 X)ㄷㅂ n : n 만큼 도박\n(접두사 X)ㄷㅂㄱ : 돈벌기 | (접두사 X)ㅇㅇ1 : 도박에 올인\n(접두사 X)ㅌㅈ : 통장 금액 확인 | !가입 : 인생게임에 가입\n !저금 n : n 만큼 통장에 저금 | !출금 n : n 만큼 통장에서 출금\n")
    
    if message.content == "ㄷㅇ":
        if is_closed != True:
            try:
                user = message.author
                roomId = message.guild.id
                userId = message.author.id
                targetId = f'{roomId},{userId}'
                with open(f'{targetId}_money.txt', 'r') as targetmoney:
                    money = targetmoney.readline()
                    with open(f'{targetId}_profile.txt', 'r') as targettitle:
                        title = targettitle.readline()
                        await message.reply(f'{user.name} 님의 현재 소지금 : {money}')
            except(FileNotFoundError):
                await message.reply("가입부터 해주세요")
    
    if message.content.startswith ("ㄷㅂ "):
        if is_closed != True:
            try:
                user = message.author
                roomId = message.guild.id
                userId = message.author.id
                targetId = f'{roomId},{userId}'
                bidmoney = message.content.replace("ㄷㅂ ", "")
                bidMoney = int(bidmoney)
                with open(f'{targetId}_money.txt', 'r') as targetMoney:
                    money = int(targetMoney.readline())
                    with open(f'{targetId}_profile.txt', 'r') as targettitle:
                        title = targettitle.readline()
                    if money > bidMoney:
                        money -= bidMoney
                        bet = random.randint(1, 2)
                        if bet == 2:
                            bset = random.randint(2, 7)
                            money += bidMoney * bset
                            await message.reply(f'{user.name}님이 도박을 성공하여 {bset} 배를 얻으셨습니다!\n현재 소지금 : {money}')
                            with open(f'{targetId}_money.txt', 'w') as targetMoney:
                                targetMoney.write(f'{money}')
                        else:
                            await message.reply(f'{user.name}님이 도박을 실패하셨습니다\n현재 소지금 : {money}')
                            with open(f'{targetId}_money.txt', 'w') as targetMoney:
                                targetMoney.write(f'{money}')
                    else:
                        await message.reply(f'돈이 부족합니다!\n{user.name}님의 현재 소지금 : {money}')
            except(FileNotFoundError):
                await message.reply("가입부터 해주세요")
    
    if message.content == "ㅇㅇ1":
        if is_closed != True:
            try:
                user = message.author
                roomId = message.guild.id
                userId = message.author.id
                targetId = f'{roomId},{userId}'
                with open(f'{targetId}_money.txt', 'r') as targetMoney:
                    money = int(targetMoney.readline())
                    with open(f'{targetId}_profile.txt', 'r') as targettitle:
                        title = targettitle.readline()
                    c = money
                    money -= c
                    bet = random.randint(1, 3)
                    if bet == 2:
                        bset = random.randint(2, 10)
                        money += c * bset
                        await message.reply(f'{user.name}님이 도박을 성공하여 {bset} 배를 얻으셨습니다!\n현재 소지금 : {money}')
                        with open(f'{targetId}_money.txt', 'w') as targetMoney:
                            targetMoney.write(f'{money}')
                    elif bet == 3:
                        bset = random.randint(2, 10)
                        money += c * bset
                        await message.reply(f'{user.name}님이 도박을 성공하여 {bset} 배를 얻으셨습니다!\n현재 소지금 : {money}')
                        with open(f'{targetId}_money.txt', 'w') as targetMoney:
                            targetMoney.write(f'{money}')
                    else:
                        await message.reply(f'{user.name}님이 도박을 실패하셨습니다\n현재 소지금 : {money}')
                        with open(f'{targetId}_money.txt', 'w') as targetMoney:
                            targetMoney.write(f'{money}')
            except(FileNotFoundError):
                await message.reply("가입부터 해주세요")
    
    if message.content == "ㅌㅈ":
        if is_closed != True:
            try:
                user = message.author
                roomId = message.guild.id
                userId = message.author.id
                targetId = f'{roomId},{userId}'
                with open(f'{targetId}_bank.txt', 'r') as targetMoney:
                    bankMoney = int(targetMoney.readline())
                    await message.reply(f'현재 {user.name}님의 통장 : {bankMoney}')
            except(FileNotFoundError):
                await message.reply("가입부터 해주세요")
    
    if message.content.startswith (prefix + "저금 "):
        if is_closed != True:
            try:
                user = message.author
                roomId = message.guild.id
                userId = message.author.id
                targetId = f'{roomId},{userId}'
                with open(f'{targetId}_money.txt', 'r') as targetMoney:
                    money = int(targetMoney.readline())
                    inMoney = message.content.replace(prefix + "저금 ", "")
                    inbankMoney = int(inMoney)
                    if money >= inbankMoney:
                        with open(f'{targetId}_bank.txt', 'r') as targetMoney:
                            bankMoney = inbankMoney + int(targetMoney.readline())
                            money -= inbankMoney
                            with open(f'{targetId}_bank.txt', 'w') as targetMoney:
                                targetMoney.write(f'{bankMoney}')
                                with open(f'{targetId}_money.txt', 'w') as targetMoney:
                                    targetMoney.write(f'{money}')
                                    await message.reply(f'{user.name}님의 소지금에서 {inMoney}원 만큼 통장에 넣었습니다\n현재 {user.name}님의 통장 : {bankMoney}원\n현재 {user.name}님의 소지금 : {money}')
                    else:
                        await message.reply(f'돈이 부족합니다!\n{user.name}님의 현재 소지금 : {money}')
            except(FileNotFoundError):
                await message.reply("가입부터 해주세요")
    
    if message.content.startswith (prefix + "후원완료"):
        await message.reply(message.author.id)
    
    if message.content.startswith (prefix + "출금 "):
        if is_closed != True:
            try:
                willoutbank = int(message.content.replace(prefix + "출금 ", ""))
                user = message.author
                roomId = message.guild.id
                userId = message.author.id
                targetId = f'{roomId},{userId}'
                with open(f'{targetId}_bank.txt', 'r') as targetMoney:
                    bankMoney = int(targetMoney.readline())
                    with open(f'{targetId}_money.txt', 'r') as targetMoney:
                        money = int(targetMoney.readline())
                        if bankMoney >= willoutbank:
                            bankMoney -= willoutbank
                            money += willoutbank
                            with open(f'{targetId}_bank.txt', 'w') as targetMoney:
                                targetMoney.write(f'{bankMoney}')
                                with open(f'{targetId}_money.txt', 'w') as targetMoney:
                                    targetMoney.write(f'{money}')
                                    await message.reply(f'{user.name}님의 통장에서 {willoutbank}원 만큼 소지금에 넣었습니다\n현재 {user.name}님의 통장 : {bankMoney}원\n현재 {user.name}님의 소지금 : {money}')
                        else:
                            await message.reply(f'돈이 부족합니다\n현재 {user.name}님의 통장 : {bankMoney}원')
            except(FileNotFoundError):
                await message.reply("가입부터 해주세요")
    
    if message.content == "ㄷㅂㄱ":
        if is_closed != True:
            try:
                user = message.author
                try: # 가입 확인
                    roomId = message.guild.id
                    userId = message.author.id
                    targetId = f'{roomId},{userId}'
                    with open(f'{targetId}_money.txt', 'r') as targetMoney:
                        money = int(targetMoney.readline())
                        addMoney = random.randint(500, 1500)
                        money += addMoney
                        await message.reply(f'{user.name}님이 {addMoney}원을 벌었습니다!\n현재 소지금 : {money}')
                        with open(f'{targetId}_money.txt', 'w') as targetMoney:
                            targetMoney.write(f'{money}')
                            await asyncio.sleep(2.5)
                except(FileNotFoundError): # 가입 확인
                    await message.reply("가입부터 해주세요")
            except(ValueError):
                await message.reply("쿨타임을 기다려 주세요")
        
client.run(token, bot=False) # if you put in () <- bot=False, self-bot start