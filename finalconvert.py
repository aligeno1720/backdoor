from os import system
from time import sleep
import random
import sys
import getpass
import time
import math
import socket
from datetime import datetime

def login():
    DNSSERVER = input("DNS SERVER: ")
    time.sleep(1)
    port = input("PORT: ")
    time.sleep(1)
    ssh = input("SSH: ")
    time.sleep(1)
    serverglobalID = input("SERVER GLOBAL ID: ")
    time.sleep(1)
    serverglobalIP = input("SERVER GLOBAL IP: ")

if __name__ == "__main__":
    login()

time.sleep(2)

def get_current_datetime():
    # Get the current date and time
    now = datetime.now()
    
    # Format the date and time as a string
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    return current_time

if __name__ == "__main__":
    current_time = get_current_datetime()
    print(f"{current_time}")

def fname(arg):
    pass
print("")
time.sleep(2)

black = "\033[0;30m"
purple = "\033[0;35m"
blue = "\033[0;34m"
green = "\033[0;32m"
red = "\033[0;31m"
yellow = "\033[0;33m"
white = "\033[0;37m"

def clear():
	system('clear')

def scrollTxt(text, color, speed):
	if color == "":
		for char in text:
			sys.stdout.write(char)
			sys.stdout.flush()
			sleep(speed)
		print()
	else:
		print(color, end="")
		for char in text:
			sys.stdout.write(char)
			sys.stdout.flush()
			sleep(speed)
		print()
		print(white, end="")
  
scrollTxt("SEARCHING >>>>>>>>>>>>>>>>>>> 3d4555926457517be3e728d2175d92a2.cloudfront.net", blue, 0.04)
time.sleep(5)

def progressBar(count_value, total, suffix=''):
	bar_length = 100
	filled_up_Length = int(round(bar_length* count_value / float(total)))
	percentage = round(100.00 * count_value/float(total),1)
	bar = '=' * filled_up_Length + '-' * (bar_length - filled_up_Length)
	sys.stdout.write('[%s] %s%s ...%s\r' %(bar, percentage, '%', suffix))
	sys.stdout.flush()
for i in range(11):
	time.sleep(random.random())
	progressBar(i,10)
#This code is Contributed by PL VISHNUPPRIYAN

print("CONNECTING")
time.sleep(4)
print("")
scrollTxt("H0DAI-AP/AS9221:/local/ns11.deutschebank.com.de'ns13", blue, 0.03)
scrollTxt("x-amz-cf-pop: VIE50-C2x-amz-cf-id: cRPQOxyIimY9Qaey4GnlLWCdWBlste23wfVgWw_B5ycGrtjo9330Qw==", blue, 0.03)
scrollTxt("x server-timing: cdn-upstream-layer;desc=Origin Shield,cdn-upstream-dns;dur=0,cdn-upstream-connect;dur=0.cdn-upstream", blue, 0.0)
scrollTxt("fbl;dur=44cdn-cache-misscdn-popdesc=VIE50-C2cdnriddesc=cRPQOxyIimY9Qaey4GnlLWCdWBlste23wfVgWw_B5ycGrtjo9330Qw==cdn-downstream-fbldur=235", blue, 0.03)
time.sleep(2)
scrollTxt("i:/C;DE/DB;Greater/L;Salford/O; BETS TNT REPAIRS (PTY) LTD / CN; BETS TNT REPAIRS (PTY) LTD", blue, 0.04)
scrollTxt("Organization Validation Secure Server CA - 1 s:/C;DE/DB;Greater/L;Salford/O; BETS TNT REPAIRS (PTY) LTD / CN; BETS TNT REPAIRS (PTY) LTD", blue, 0.03)
scrollTxt("Organization Validation Secure Server CA - 2 s:/C;DE/DB;Greater/L;Salford/O; BETS TNT REPAIRS (PTY) LTD / CN; BETS TNT REPAIRS (PTY) LTD ", blue, 0.03)
scrollTxt("Certification Authority i:/C;SE/O;AddTrust AB/OU ;AddTrust External TTP Network/ CN;Addtrust External CA Root", blue, 0.04)
time.sleep(2)
scrollTxt("AddTrustExternalTTPNetwork/CN;AddTrustExternal CA Rooti:/C;SE/OAddTrustAB/OLJ;AddTrust External TTP Network/CN;AddTrust External CA Root", blue, 0.04)
time.sleep(8)

print("")

def scrollTxt(text, color, speed):
	if color == "":
		for char in text:
			sys.stdout.write(char)
			sys.stdout.flush()
			sleep(speed)
		print()
	else:
		print(color, end="")
		for char in text:
			sys.stdout.write(char)
			sys.stdout.flush()
			sleep(speed)
		print()
		print(white, end="")

def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")
            
numbers = [x * 5 for x in range(2000, 3000)]
results = []


progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))

time.sleep(3)
print("DOWNLOADING")
time.sleep(2)
print("======================================================================================================")
time.sleep(2)
scrollTxt("BANK INSTITUTION: DEUTDEFFXXX", blue, 0.04)
scrollTxt("IDENITITY CODE: 211690455630BUE", blue, 0.04)
scrollTxt("ACCOUNT NUMBER: 947259564", blue, 0.04)
scrollTxt("CURRENCY: EUR(€)", blue, 0.04)
scrollTxt("AMOUNT:(€)5,137,653,123.00", blue, 0.04)
scrollTxt("SORT CODE NO.: 678691681", blue, 0.04)
scrollTxt("CREDIT INSTITUT: DEUTSCHE BANK AG", blue, 0.04)
scrollTxt("CLIENT NAME:  STRONG CONFIDENCE HOLDINGS LIMITED", blue, 0.04)
scrollTxt("REMIT ARRIVAL MONEY NO.: SCF-664M388RT667", blue, 0.04)
scrollTxt("WTS SERVER: 50200235", blue, 0.04)
scrollTxt("LOGON DOMAIN: HDAI-AP9221", blue, 0.04)
scrollTxt("LOGON SERVER: FRAESWDBEP 21", blue, 0.04)
scrollTxt("COMMON ACCOUNT NUMBER: CH21 0027 8278 8228 7661 F", blue, 0.04)
scrollTxt("UTR.:USCSY-GGSB1.DBFF100T.EUR/GG24314", blue, 0.04)
scrollTxt("USER ID: FGN470", blue, 0.04)
scrollTxt("CODE: A23F17.01.31.47.GTF", blue, 0.04)
time.sleep(1)
scrollTxt("DEPOSIT TRANSCATION NO: 932587UBS305079", blue, 0.04)
time.sleep(1)
scrollTxt("FINAL BLOCKING CODE: HS30148574128904", blue, 0.04)
time.sleep(1)
scrollTxt("ACTIVATION CODE:Credimais", blue, 0.04)
time.sleep(1)
scrollTxt("TRANSACTION CODE:144A:S:G4639DVY8", blue, 0.04)
time.sleep(1)
scrollTxt("ACCESS CODE: DEUT-42411550", blue, 0.04)
time.sleep(1)
scrollTxt("AMOUT: (€)5,137,653,123.00", blue, 0.04)
time.sleep(1)
scrollTxt("ACCOUNT NAME: STRONG CONFIDENCE HOLDINGS LIMITED ", blue, 0.04)
time.sleep(1)
scrollTxt("ACCOUNT NUMBER: 6392095967", blue, 0.04)
time.sleep(1)
scrollTxt("ACCOUNT SIGNATORY NAME: MR. GINTARAS GECAS", blue, 0.04)
time.sleep(1)
scrollTxt("USER NAME: 493069K1", blue, 0.04)
time.sleep(1)
scrollTxt("BANK PHONE NUMBER: +49 2533 6399 ", blue, 0.04)
time.sleep(5)

print("======================================================================================================")
time.sleep(2)

def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")
            
numbers = [x * 5 for x in range(2000, 3000)]
results = []


progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))

print("CONNECTED ")
time.sleep(5)
def get_current_datetime():
    # Get the current date and time
    now = datetime.now()
    
    # Format the date and time as a string
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    return current_time

if __name__ == "__main__":
    current_time = get_current_datetime()
    print(f"{current_time}")
time.sleep(8)
black = "\033[0;30m"
purple = "\033[0;35m"
blue = "\033[0;34m"
green = "\033[0;32m"
red = "\033[0;31m"
yellow = "\033[0;33m"
white = "\033[0;37m"

def clear():
	system('clear')


print("")
scrollTxt("--------------------------------------welcome to swift------------------------------------------------", blue, 0.04)
time.sleep(5)

scrollTxt("$ global_server/start", blue, 0.1)
time.sleep(5)

def login():
    Login = input("Login: ")
    time.sleep(1)
    Password = input("Password: ")

if __name__ == "__main__":
    login()

def fname(arg):
    pass
time.sleep(2)
print("CONNECTED")
time.sleep(1)

def get_current_datetime():
    # Get the current date and time
    now = datetime.now()
    
    # Format the date and time as a string
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    return current_time

if __name__ == "__main__":
    current_time = get_current_datetime()
    print(f"{current_time}")

time.sleep(3)

black = "\033[0;30m"
purple = "\033[0;35m"
blue = "\033[0;34m"
green = "\033[0;32m"
red = "\033[0;31m"
yellow = "\033[0;33m"
white = "\033[0;37m"


scrollTxt("$  global_server/mt103/convert/blockchain/usdt-trc20", blue, 0.04)

def login():
    RELEASECODE = input("RELEASE CODE: ")
    time.sleep(2)
    FINALCODE = input("FINAL CODE: ")

if __name__ == "__main__":
    login()

time.sleep(1)

scrollTxt("--------------------------------------- DOWNLOADING --------------------------------------------------", blue, 0.04)
time.sleep(8)
def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")
            
numbers = [x * 5 for x in range(2000, 3000)]
results = []

def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")
            
numbers = [x * 5 for x in range(2000, 3000)]
results = []


progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))
    
print("CONNECTED ")
def get_current_datetime():
    # Get the current date and time
    now = datetime.now()
    
    # Format the date and time as a string
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    return current_time

if __name__ == "__main__":
    current_time = get_current_datetime()
    print(f"{current_time}")
time.sleep(3)
scrollTxt("---------------------------------------- CONVERTING -------------------------------------------------", blue, 0.04) 
time.sleep(2)
scrollTxt(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FROM SENDING SERVER     TO     RECEIVING          SERVER OPERATOR   ", blue, 0.04)
scrollTxt("-----------------------------------------------------------------------------------------------------", blue, 0.04)
scrollTxt("Summary:FACY67711675227932/Mode:XXXXXX1720-TX DISPLAY *********193.148.16.3     KONGALI1720&GATOTKACA", blue, 0.04)
scrollTxt("-----------------------------------------------------------------------------------------------------", blue, 0.04)
scrollTxt("VICE CCY/UNIT BALANCE               |      INTEREST                  |                WTS SERVER     ", blue, 0.04)
scrollTxt("-----------------------------------------------------------------------------------------------------", blue, 0.04)
scrollTxt("FCY EUR 5,137,653,123.00            |        0.00                    |          KONGALI1720&GATOTKACA", blue, 0.04)
scrollTxt("-----------------------------------------------------------------------------------------------------", blue, 0.04)
scrollTxt("TOTAL BALANCE IN EUR *************************************************************** 5,137,653,123.00", blue, 0.04)
time.sleep(2)
scrollTxt("-----------------------------------------------------------------------------------------------------", blue, 0.04) 
time.sleep(8)
def login():
    TRANSACTIONCODE = input("TRANSACTION CODE: ")
    time.sleep(2)
    OPERATIONID = input("OPERATION ID: ")
    time.sleep(2)
    PIN = input("PIN: ")
    time.sleep(2)
if __name__ == "__main__":
    login()

scrollTxt("processing convert to BLOCKCHAIN/USDT-TRC20/---------------------------------------------------------", blue, 0.04)
time.sleep(2)
def login():
    WALLETADDRESS = input("ETHEREUM ADDRESS: ")
    time.sleep(2)
    SECRETKEY = input("PRIVATE KEY: ")
    time.sleep(2)
    
if __name__ == "__main__":
    login()
time.sleep(8)
print("")

scrollTxt("------------------------------ PROCESSING TO CONVERT ------------------------------------------------", blue, 0.04)
time.sleep(4)

def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")
            
numbers = [x * 5 for x in range(2000, 3000)]
results = []


progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))

print("PROCESSING ")
def get_current_datetime():
    # Get the current date and time
    now = datetime.now()
    
    # Format the date and time as a string
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    return current_time

if __name__ == "__main__":
    current_time = get_current_datetime()
    print(f"{current_time}")

time.sleep(10)

scrollTxt("TOTAL BALANCE IN EUR - TO - RECEIVING BALANCE IN USDT-TRC20", blue, 0.04)
time.sleep(3)
scrollTxt("-----------------------------------------------------------------------------------------------------", blue, 0.04)
time.sleep(1)
scrollTxt("5,137,653,123.00 EUR   |    556,562,081.36 USDT", blue,0.04)
time.sleep(10)
scrollTxt("-----------------------------------------------------------------------------------------------------", blue, 0.04)
time.sleep(1)

def get_current_datetime():
    # Get the current date and time
    now = datetime.now()
    
    # Format the date and time as a string
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    return current_time

if __name__ == "__main__":
    current_time = get_current_datetime()
    print(f"{current_time}")

def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")
            
numbers = [x * 5 for x in range(2000, 3000)]
results = []

print("connecting to blockchain")
time.sleep(3)

scrollTxt("YOUR TRANSACTION :", blue, 0.04)
time.sleep(2)
scrollTxt("YOUR DEPOSIT OF 5,137,653,123.00 EURO WAS NOT SUCCESS. IT IS REJECTED BY SENDING BANK", blue, 0.04)
time.sleep(2)
scrollTxt("DUE TO NO APPROVAL FROM MILLION/BILLION DEPARTMENT WE CANT'T ACCEPT UN-CLEAR FUNDS", blue, 0.04)
time.sleep(2)
scrollTxt("PLEASE CONTACT YOUR BANK FOR MORE INFORMATION", blue, 0.04)
scrollTxt("PLEASE RESET YOUR PASSWORD AND CONTACT CUSTOMER SUPPORT IMMEDIATELY", blue, 0.04)
scrollTxt("THIS IS AN AUTOMATED MESSAGE, PLEASE DO NOT REPLY", blue, 0.04)
time.sleep(10)
def login():
    doyouwanttocontinue = input("PROCEED CONTINUE? | Y/N ")
    time.sleep(2)
if __name__ == "__main__":
    login()
    
scrollTxt("finished", blue, 0.04)
time.sleep(10)


