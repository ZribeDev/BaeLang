import os
import shutil
import sys
import ctypes
import winreg
from colorama import init, Fore, Style

init(autoreset=True)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def remove_from_program_files():
    program_files_dir = os.environ.get("ProgramFiles", "C:\\Program Files")
    target_dir = os.path.join(program_files_dir, "BaeLang")

    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
        print(f"Removed {target_dir}")
    else:
        print(f"{target_dir} does not exist")

def remove_bae_association():
    try:
        winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r".bae")
        print("Removed .bae key from HKEY_CLASSES_ROOT")

        user_keys = [
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.bae",
            r"SOFTWARE\Microsoft\Windows\Roaming\OpenWith\FileExts\.bae"
        ]

        for key in user_keys:
            try:
                winreg.DeleteKey(winreg.HKEY_CURRENT_USER, key)
                print(f"Removed .bae key from HKEY_CURRENT_USER\\{key}")
            except FileNotFoundError:
                print(f"Registry key HKEY_CURRENT_USER\\{key} not found")
            except OSError as e:
                print(f"Error removing registry key HKEY_CURRENT_USER\\{key}: {e}")

    except FileNotFoundError:
        print("Registry keys for .bae file association not found in HKEY_CLASSES_ROOT")
    except OSError as e:
        print(f"Error removing registry keys: {e}")

def reset_bae_association():
    try:
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r".bae")
        winreg.SetValue(key, "", winreg.REG_SZ, "")
        winreg.CloseKey(key)
        print("Reset .bae file association to default")
    except OSError as e:
        print(f"Error resetting .bae file association: {e}")

def main():
    if not is_admin():
        print(Fore.RED + Style.BRIGHT + "Error: This script must be run as an administrator.")
        sys.exit(1)
    remove_from_program_files()
    remove_bae_association()
    reset_bae_association()
    print("Uninstallation complete. Please restart your PC for changes to take effect.")

if __name__ == "__main__":
    main()
