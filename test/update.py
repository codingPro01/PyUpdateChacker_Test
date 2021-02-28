import urllib.request
checkverpage = str(urllib.request.urlopen("https://codingpro01-versionsave.netlify.app/test/version.txt").read()).replace("b'", "")
checkver = checkverpage.replace("\\n'", "")
nowversionopen = open("version.txt", "r")
nowversion = nowversionopen.read()
if nowversion != checkver:
    print("Update available. ")
    print(f"Now version: {nowversion}")
    print(f"New version: {checkver}")
if nowversion == checkver:
    print("Program up to date. ")
