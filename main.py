# linux folder organiser
# Author : Gaurav Raj
# website : http://gauravraj.cf/
# Note : Give Credit before committing any changes.

# imports
import os
import shutil
from colorama import Fore, Style
import pyfiglet


def banner():
    bn = pyfiglet.figlet_format(" Folder Organiser", font='slant')
    print(f"{Fore.GREEN}{bn}{Style.RESET_ALL}")


def mkd():
    s_n = 0
    for i in dirs_lst:
        if i not in os.listdir(user_path):
            os.mkdir(user_path + '/' + i)
        else:
            pass
        s_n = s_n + 1
        print(f" {s_n}. {Fore.GREEN}{i}{Style.RESET_ALL}")
    print()


def org_dirs(dirs, user_path):
    for i in os.listdir(user_path):
        if os.path.isfile(f"{user_path}/{i}"):
            file_src = user_path + '/' + i
            for key in dirs:
                extn = dirs[key]
                if i.endswith(extn):
                    dest_path = os.path.join(user_path, key, i)
                    shutil.move(file_src, dest_path)
                    break
    print()


def org_rmn_file(user_path):
    for i in os.listdir(user_path):
        if os.path.isfile(f"{user_path}/{i}"):
            file_src = user_path + '/' + i
            dest_path = os.path.join(user_path, "others", i)
            shutil.move(file_src, dest_path)
    print()


dirs_lst = ["HTML", "Images", "Videos", "Documents", "Compressed", "Audio", "Python", "Programs", "Others", "Folders"]


try:
    if __name__ == '__main__':
        banner()
        print()
        user = input(" Enter Name of Linux User : " + Fore.GREEN)
        print(Style.RESET_ALL)
        user_path = f"/home/{user}/Downloads/"
        dirs = {
            "HTML": (".html5", ".html", ".htm", ".xhtml"),
            "Images": (".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg",
                       "svg",
                       ".heif", ".psd"),
            "Videos": (".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",
                       ".mng",
                       ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"),
            "Documents": (".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf",
                          ".ods",
                          ".odt", ".pdf", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                          ".rvg", ".rtf", ".txt", ".in", ".out", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                          "pptx"),
            "Compressed": (".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                         ".dmg", ".rar", ".xar", ".zip"),
            "Audio": (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p",
                      ".mp3",
                      ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"),
            "Python": ".py",
            "Programs": ".exe",
            "Others": "",
            "Folders": ""
        }

        print(f"{Fore.GREEN}\t Creating Folders...{Style.RESET_ALL}\n")
        mkd()
        print(f"{Fore.GREEN}\t Organising Folders...{Style.RESET_ALL}")
        org_dirs(dirs, user_path)
        print(f"{Fore.GREEN}\t Organising Remaining Folders...{Style.RESET_ALL}")
        org_rmn_file(user_path)
        print(f"{Fore.GREEN}\t Directory Organising Completed...{Style.RESET_ALL}")
        print(f"""
        \t{Fore.LIGHTGREEN_EX}==================================
        \t||    {Style.RESET_ALL}Project by : {Fore.GREEN}Gaurav Raj{Fore.LIGHTGREEN_EX}   ||
        \t==================================
        {Style.RESET_ALL}""")

except FileNotFoundError as f_err1:
    print(f"{Fore.RED} Error Encountered, File not Found !!!{Style.RESET_ALL}")
except FileExistsError as f_err2:
    print(f"{Fore.RED} Error Encountered, File already Exists !!!{Style.RESET_ALL}")
except ImportError as imp_err:
    print(f"{Fore.RED} Error Encountered, Error Importing Module !!!{Style.RESET_ALL}\n {imp_err}")
except KeyboardInterrupt as keyerr:
    print(f"{Fore.RED} Exiting Code.\t {Fore.GREEN}Thank You For Using ...{Style.RESET_ALL}")
except EOFError as eo_err:
    print(f"{Fore.RED} Exiting Code.\t {Fore.GREEN}Thank You For Using ...{Style.RESET_ALL}")
