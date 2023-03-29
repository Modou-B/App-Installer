import os
import subprocess
import requests
import urllib.request
import urllib.error
import socket
from pathlib import Path
from urllib.parse import urlparse
import zipfile

urls = [
    "https://us.download.nvidia.com/Windows/531.41/531.41-desktop-win10-win11-64bit-international-dch-whql.exe",
    
    #X "https://drivers.amd.com/drivers/amd_chipset_software_5.02.19.2221.exe", 
    #X "https://drivers.amd.com/drivers/whql-amd-software-adrenalin-edition-23.3.2-win10-win11-mar22.exe",
    
    "https://www.google.com/intl/de_de/chrome/thank-you.html?statcb=0&installdataindex=empty&defaultbrowser=0#",
    "https://nzxt-app.nzxt.com/NZXT-CAM-Setup.exe",
    "https://download01.logi.com/web/ftp/pub/techsupport/gaming/lghub_installer.exe",
    "https://rzr.to/synapse-3-pc-download",
    "https://downloads.corsair.com/Files/CUE/iCUESetup_4.33.138_release.msi",
    "https://download.msi.com/uti_exe/vga/MSIAfterburnerSetup.zip?__token__=exp=1680257471~acl=/*~hmac=d84a8d2164c0b747d17dd7e9b0459da7485922f1df023a6b7cc4030cbdf1b280",
    "https://download.cpuid.com/cpu-z/cpu-z_2.05-rog-en.exe",
    "https://download.cpuid.com/hwmonitor/hwmonitor_1.50.exe",
    "https://download.aida64.com/aida64extreme688.exe",
    
    #X "https://app.prntscr.com/build/setup-lightshot.exe",
    #X "https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86",
    
    "https://cdn.cloudflare.steamstatic.com/client/installer/SteamSetup.exe",
    "https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi",
    "https://www.battle.net/download/getInstallerForGame?os=win&gameProgram=BATTLENET_APP&version=Live",
    "https://ubi.li/4vxt9",
    "https://github.com/git-for-windows/git/releases/download/v2.40.0.windows.1/Git-2.40.0-64-bit.exe",
    "https://code.visualstudio.com/download#",
    "https://download.semiconductor.samsung.com/resources/software-resources/Samsung_Magician_Installer_Official_7.3.0.1100.zip",
    "https://www.gskill.com/gskill-device/memory/G.SKILL-Trident-Z-Lighting-Control-v1.00.31.zip",
    
    #X "https://www.notion.so/desktop/windows/download"
]

topLevelDomains = [
    ".com",
    ".net",
    ".de",
    ".li",
    ".so",
    ".to"
]

fileFormats = [
    ".exe",
    ".msi"
]

folderFormats = [
    ".zip"
]

def main():
    # os.system("cls")
    mode = ChooseMode()
    if int(mode) == 1:
        automaticInstaller(urls, topLevelDomains,fileFormats,folderFormats)
        exit
    if int(mode) == 2:
        manuelInstaller()
        exit
    if int(mode) != 1 and int(mode) != 2:
        print("invalid mode")
        exit

def CheckIfFileExits(url):
    countNumbers = True
    i = 0
    if os.path.exists(url):
        while countNumbers:
            i += 1   
            if not os.path.exists(url+str(i)):
                countNumbers = False
                return(url+str(i))
    else:
        return(url)
        

def url_retrieve(url: str, outfile: Path, overwrite: bool = False,):
    # if is_downloadable(url):
        outfile = Path(outfile).expanduser().resolve()
        if outfile.is_dir():
            raise ValueError("Please specify full filepath, including filename")
        # need .resolve() in case intermediate relative dir doesn't exist
        if overwrite or not outfile.is_file():
            outfile.parent.mkdir(parents=True, exist_ok=True)
            urllib.request.urlretrieve(url, str(outfile))
            # try:
            #     urllib.request.urlretrieve(url, str(outfile))
            # except (socket.gaierror, urllib.error.URLError) as err:
            #     raise ConnectionError(
            #         "could not download {} due to {}".format(url, err)
            #     )
    # else:
    #     print(Path+' is not a downloadable'+'\n')

def ChooseMode():
    return int(input("Choose 1 = Automatic, 2 = Manual: "))

def CheckIfFullyAuto():
    return int(input("Fully automatic? yes = 1, no = 2: "))

def automaticInstaller(urls= [], topLevelDomains = [], fileFormats = [], folderFormats = []):
    os.system("cls")
    print("Automatic installation")
    
    fullyAuto = CheckIfFullyAuto();
    if fullyAuto == False:
        dir = ChooseDestinationDirectory();
    else:
        dir = "C:/Users/modou/Downloads/TempApps/"
    
    numOfUrls = str(len(urls))
    count = 0
    for url in urls:
        count += 1;
        
        print(str(count)+'/'+numOfUrls)
        t = (urlparse(url).netloc)
        parsedUrl = '.'.join(t.split('.')[-2:])
        for tldomoin in topLevelDomains:
            parsedUrl = str(parsedUrl).removesuffix(tldomoin)
            
        print(str(parsedUrl))
        print('#--------#')
        print('')

        fileName = dir+str(count)+'. '+str(parsedUrl)
        fileName = CheckIfFileExits(fileName)
        # if is_downloadable(url):
        isFile = False
        isFolder = False
        notFound = False
        for file in fileFormats:
            if file in url:
                url_retrieve(url,fileName+file,True)
                isFile = True
                break
        
        if isFile == False:    
            for folder in folderFormats:
                if folder in url:
                    fileName = "C:/Users/modou/Downloads/TempApps/"+str(parsedUrl)
                    url_retrieve(url,fileName+folder,True)
                    isFolder = True
                    break
        if isFile == False and isFolder == False: 
            print("Download")
            url_retrieve(url,fileName+'.exe',True)
    run_automatic_installer("C:/Users/modou/Downloads/TempApps/", folderFormats)

def manuelInstaller():
    print("Manuel installation")
    dir = ChooseSourceDirectory()
    run_manuel_installer(dir)
    

def ChooseSourceDirectory():
    return input("Choose the setup source directory (D:\Apps\App Setups\): ")

def ChooseDestinationDirectory():
    return input("Choose the setup destination directory (C:/Users/modou/Downloads/TempApps/): ")


def print_list_of_installed_programs(list_of_installed_apps):
    # print("")
    print("\n"+"[Installed Apps]: ")
    print("[=========================================]")
    for installed_app in list_of_installed_apps:
        print(installed_app)
    print("[=========================================]"+"\n\n")


def print_list_of_not_installed_programs(list_of_not_installed_apps):
    print("\n\n"+"[Not installed Apps]: ")
    print("[=========================================]")
    for installed_app in list_of_not_installed_apps:
        print(installed_app)
    print("[=========================================]"+"\n\n\n")


def print_file_info(fileName):
    print("\n"+"------------------------------------")
    print("Install: "+fileName)
    print("------------------------------------")  


def continue_installation():
    continue_value = input("y/n?: (x = exit)")
    return continue_value


def run_manuel_installer(dir):
    
    os.system("cls")
    list_of_not_installed_apps = []
    list_of_installed_apps = []
    app_folder = os.listdir(dir)

    for app in app_folder:
        app_path = os.path.join(dir, app)
        
        if os.path.isfile(app_path):
            file_name = (os.path.splitext(app)[0])
            print_file_info(file_name)
            
            value_of_continue_installation = continue_installation()
            
            if (value_of_continue_installation == "y"):
                list_of_installed_apps.append(file_name)
                subprocess.call(app_path,shell=True)
                
            elif (value_of_continue_installation == "x"):
                break
            else: 
                list_of_not_installed_apps.append(file_name)         
    os.system("cls")           
    print_list_of_installed_programs(list_of_installed_apps)
    print_list_of_not_installed_programs(list_of_not_installed_apps)

# def UnzipFiles(dir, folderFormats = []):
#     app_folder = os.listdir(dir)
#     for app in app_folder:
#         app_path = os.path.join(dir, app)
        
#         for folder in folderFormats:
#                 if folder in app_path:
#                     if os.path.isfile(app_path):
#                         f_format = str(folder)[1:4]
#                         with zipfile.ZipFile(app_path, 'r') as zip_ref:
#                             zip_ref.extractall(dir)

def run_automatic_installer(dir, folderFormats = []):
    os.system("cls")
    list_of_installed_apps = []
    app_folder = os.listdir(dir)
    
    for app in app_folder:
        app_path = os.path.join(dir, app)
        
        for folder in folderFormats:
            if folder in app_path:
                file_name = (os.path.splitext(app)[0])
                print_file_info(file_name)
                list_of_installed_apps.append(file_name)
                subprocess.call(app_path,shell=True)
                break
    
        if os.path.isfile(app_path):
            file_name = (os.path.splitext(app)[0])
            print_file_info(file_name)
            list_of_installed_apps.append(file_name)
            subprocess.call(app_path,shell=True)     
    os.system("cls")           
    print_list_of_installed_programs(list_of_installed_apps)

if __name__ == "__main__":
    main()