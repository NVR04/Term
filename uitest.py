import term
import os
import colorama
import emoji


dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]

resize = True

term.resizeTerm()
term.setOpacity(80)
term.banner("FEXP")
if term.ask("Start at C:?"): os.chdir("C:")

def main():
    while True:
        term.cls()
        files = {}
        filesRaw = os.listdir(os.getcwd())
        bigLen = 0

        for file in filesRaw:
            if len(file) > bigLen: bigLen = len(file)

        if resize: term.resizeTerm(bigLen+30, len(filesRaw)+12)

        for file in filesRaw:
            fileType = "dir" if os.path.isdir(file) else "file"
            if fileType == "dir": files.update({colorama.Fore.WHITE + emoji.emojize(":file_folder:") + " " + file: ""})
            elif file.endswith(".py"): files.update({emoji.emojize(":snake:") + " " + file:""})
            else: files.update({file:""})
        chosen = term.printOptions(files)
        if chosen != "..":
            worked = False
            for drive in drives:
                if chosen.lower().startswith(drive.lower()):
                    os.chdir(drive)
                    worked = True
                    break
            if not worked:
                chosenFile = filesRaw[int(chosen)-1]
                chosenType = "dir" if os.path.isdir(chosenFile) else "file"
                
                if chosenType == "dir": os.chdir(chosenFile)
                else: os.startfile(chosenFile)
        elif chosen == "..": os.chdir("..")

try:
    main()
except Exception:
    term.alertR("ERROR")
    input()
    main()