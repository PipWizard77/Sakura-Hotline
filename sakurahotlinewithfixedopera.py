import os
import time
import webbrowser
os.system('color 5f')
print("                         ")
print("                         ")
print("                         ")
print("                         ")
print("💮What website would you like to open?💮")
print("                         ")
print("1:Microsoft Start💮                      ")
print("2:Microsoft News💮                       ")
print("3:Google💮                               ")
print("4:Yahoo💮                                ")
print("5:Google Chrome💮                        ")
print("6:Mozilla Firefox 💮                     ")
print("7:Opera💮                                ")
print("8:Nepscape ISP💮                         ")
print("9:Vivaldi💮                              ")
print("10:Brave💮                               ")
print("                                          ")
opener=input("")

if opener=="1" or opener=="2" or opener=="3" or opener=="4" or opener=="5" or opener=="6" or opener=="7" or opener=="8" or opener=="9" or opener=="10":
    if opener=="1":
        webbrowser.open_new_tab('microsoftstart.com')
        os.system('cls')

    if opener=="2":
        os.system('start iexplore')
        os.system('cls')

    if opener=="3":
        webbrowser.open_new_tab('google.com')
        os.system('cls')

    if opener=="4":
        webbrowser.open_new_tab('yahoo.com')
        os.system('cls')

    if opener=="5":
        webbrowser.open_new_tab('chrome.com')
        os.system('cls')

    if opener=="6":
        webbrowser.open_new_tab('firefox.com')
        os.system('cls')

    if opener=="7":
        webbrowser.open_new_tab('opera.com')
        os.system('cls')

    if opener=="8":
        webbrowser.open_new_tab('isp.netscape.com')
        os.system('cls')

    if opener=="9":
        webbrowser.open_new_tab('vivaldi.com')
        os.system('cls')

    if opener=="10":
        webbrowser.open_new_tab('brave.com')
        os.system('cls')
else:
    print("💮Not Valid Answer!💮")
    time.sleep(1)
    os.system('cls')
    quit()