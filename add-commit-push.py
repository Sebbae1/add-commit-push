import os
import sys
print("testing")
numOfArgs = len(sys.argv)
print("Number of Arguments Passed:  " + str(numOfArgs))
message = "Update files"
if numOfArgs == 3:
    if sys.argv[1] == "-m":
        print("Number of Arguments = 3 and p2 = -m")
        message = sys.argv[2]
        
print(message)
#W3C Schools


print("Add, Commit, Push with Python")
print("\ngit status")
os.system("git status")

#W3C School's Code Lines 4-6
print("Do you want to continue with add, commit, push? (y)")
confirm = input()
if confirm != "y" and confirm !="-f":
    print("Canceling: ", confirm)
    quit()
    
if confirm =="y":     
    print("\ngit add -A")
    os.system("git add -A")
    commitStatement = '\ngit commit -m "' + message + '"'
    print(commitStatement)
    os.system(commitStatement)
    print('\ngit commit -m "Update files"')
    os.system('git commit -m "Update files."')
    print("\ngit push")
    os.system("git push")
    
if confirm == "-f":
    print("Executing -f")
    print("\ngit add -A")
    os.system("git add -A")
    commitStatement = '\ngit commit -m "' + message + '"'
    os.system(commitStatement)
    os.system('git commit -m "Update files."')
    os.system("git push")   