import psutil
import win32com.client
shell = win32com.client.Dispatch("WScript.Shell")

banner = ("#################################\n"
          "##    BUFFER OVERFLOW FUZZER   ##\n"
          "##  Coded By: Joel Aviad Ossi  ##\n"
          "#################################")
print(banner)
print('')

process = raw_input("Process Name to Fuzz (Without .exe): ")

def check_process():
    if str(process + ".exe") in (p.name() for p in psutil.process_iter()):
        return True
    else:
        return False

amount = 1

def fuzzer(amount):
    shell.AppActivate(str(process))
    shell.SendKeys(chr(65) * amount)
    shell.SendKeys("{Enter}", 0)

while check_process():
    print("[+] Fuzzing: " + str(amount))
    fuzzer(amount)
    amount += 1
else:
    print("\n"+"[!] Crashed or Process is not Running, Last tested character: " + str(amount - 1))
