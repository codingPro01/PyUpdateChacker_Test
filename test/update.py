import urllib.request
checkverpage = str(urllib.request.urlopen("https://codingpro01-versionsave.netlify.app/test/version.txt").read()).replace("b'", "")
checkver = checkverpage.replace("\\n'", "")
nowversionopen = open("version.txt", "r")
nowversion = nowversionopen.read()
if nowversion != checkver:
    print("Update available. ")
    print(f"Now version: {nowversion}")
    print(f"New version: {checkver}")
    confirm_new_version_download = input(f"Download {checkver} program? (y/n): ")
    if confirm_new_version_download == "y":
        newappdnpage = str(urllib.request.urlopen("https://raw.githubusercontent.com/codingPro01/PyUpdateChacker_Test/main/test/update.py").read()).replace("b'", "")
        newappdn = newappdnpage.replace("\\n", "\n")
        newappdn = newappdn[:-1]
        newappins = open(f"updatecheck_{checkver}.py", "w+")
        newappins.write(newappdn)
if nowversion == checkver:
    print("Program up to date. ")
 
