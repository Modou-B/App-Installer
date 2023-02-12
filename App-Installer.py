import os
import subprocess

dir = "E:/Apps/App Setups/"
InstalledList = []
NotInstalledList = []
continueInstallation = "n"


os.system("cls")
for app in os.listdir(dir):
    appPath = os.path.join(dir, app)
    if os.path.isfile(appPath):
        fileName = (os.path.splitext(app)[0])
        
        print("")
        print("------------------------------------")
        print("Install: "+fileName)
        print("------------------------------------")
        continueInstallation = input("y/n?: (x = exit)")
        print("")
        
        if (continueInstallation == "x"):
            print("------------------------------------")
            print("")
            print("Exit installation")
            print("")
            print("------------------------------------")
            break
                    
        if (continueInstallation == "y"):
            InstalledList.append(fileName)
            subprocess.call(appPath,shell=True)
        else:
            NotInstalledList.append(fileName)

os.system("cls")
print("")
print("[Installed]: ")
print("[=========================================]")
for i in InstalledList:
    print(i)
print("[=========================================]")
print("")
print("")
print("[Not installed]:")
print("[=========================================]")
for i in NotInstalledList:
    print(i)
print("[=========================================]")
print("")