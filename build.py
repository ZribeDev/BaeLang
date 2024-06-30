import os
import shutil
import subprocess
import sys
import ctypes
import winreg

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, __file__, None, 1
        )
        sys.exit(0)

def run_pyinstaller():
    subprocess.run([
        "pyinstaller", "--onefile", "--distpath", "out", "--clean", "-y", "convert.py", "--log-level=DEBUG"
    ])
    subprocess.run([
        "pyinstaller", "--onefile", "--distpath", "out", "--clean", "-y", "run.py", "--log-level=DEBUG"
    ])
    subprocess.run([
        "pyinstaller", "--onefile", "--distpath", "out", "--clean", "-y", "code.py", "--log-level=DEBUG"
    ])

def copy_to_program_files():
    program_files_dir = os.environ.get("ProgramFiles", "C:\\Program Files")
    target_dir = os.path.join(program_files_dir, "BaeLang")

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    shutil.copy("out\\convert.exe", target_dir)
    shutil.copy("out\\run.exe", target_dir)
    shutil.copy("out\\code.exe", target_dir)

def associate_bae_with_run():
    program_files_dir = os.environ.get("ProgramFiles", "C:\\Program Files")
    target_dir = os.path.join(program_files_dir, "BaeLang")
    run_exe_path = os.path.join(target_dir, "run.exe")

    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, ".bae")
    winreg.SetValue(key, "", winreg.REG_SZ, "BaeLangFile")
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, "BaeLangFile\\shell\\open\\command")
    winreg.SetValue(key, "", winreg.REG_SZ, f'"{run_exe_path}" "%1"')

def main():
    run_as_admin()
    run_pyinstaller()
    copy_to_program_files()
    associate_bae_with_run()
    print("Build and installation complete.")

if __name__ == "__main__":
    main()
