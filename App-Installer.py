import os
import subprocess


def main():
    dir = "D:/Apps/App Setups/"
    run_installer(dir)




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


def run_installer(dir):
    
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




if __name__ == "__main__":
    main()