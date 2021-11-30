# Auth.GG Manager
# Date: 11.30.21
# Author @irxv

import os, requests, json, time

BANNER = '''
\n\t\t\033[0;95m     _         _   _      ____  ____                                               
\t\t\033[0;95m    / \\  _   _| |_| |__  / ___|/ ___|  _ __ ___   __ _ _ __   __ _  __ _  ___ _ __ 
\t\t\033[0;95m   / _ \\| | | | __| '_ \\| |  _| |  _  | '_ ` _ \\ / _` | '_ \\ / _` |/ _` |/ _ \\ '__|
\t\t\033[0;95m  / ___ \\ |_| | |_| | | | |_| | |_| | | | | | | | (_| | | | | (_| | (_| |  __/ |   
\t\t\033[0;95m /_/   \\_\\__,_|\\__|_| |_|\\____|\\____| |_| |_| |_|\\__,_|_| |_|\\__,_|\\__, |\\___|_|   
\t\t\033[0;95m                                                                   |___/           
\033[0;97m
'''

AUTHKEY = "AUTH KEY HERE"

def CheckAuthKey(key:str):
    result = requests.get("https://developers.auth.gg/USERS/?type=count&authorization="+key)
    resultjson = result.json()
    if resultjson['status'] == "success":
        return True
    else:
        return False


def main():
    if CheckAuthKey(AUTHKEY) == True:
        print("Auth key is valid! Please wait...")
        time.sleep(3)
        os.system("cls")
        print(BANNER)
        print("\t[1] Users")
        print("\t[2] License")
        print("\t[3] HWID")
        command = input("> ")
        
        # Users
        if command == "1":
            os.system("cls")
            print(BANNER)
            print("\t[1] Fetch Users Information")
            print("\t[2] Delete User")
            print("\t[3] Edit user variable")
            print("\t[4] Change Password")
            print("\t[5] User Count")
            userscommand = input("> ")
            
            # Fetch users information
            if userscommand == "1":
                username = input("Username> ")
                URL = requests.get("https://developers.auth.gg/USERS/?type=fetch&authorization=" + AUTHKEY + "&user=" + username)
                urljson = URL.json()
                if urljson["status"] == "failed":
                    exit()
                else:
                    print("Username: "+urljson["username"]+"")
                    print("Status: "+urljson["status"]+"")
                    print("Email: "+urljson["email"]+"")
                    print("Rank: "+urljson["rank"]+"")
                    print("HWID: "+urljson["hwid"]+"")
                    print("Variable: "+urljson["variable"]+"")
                    print("Last-Login: "+urljson["lastlogin"]+"")
                    print("Last-IP: "+urljson["lastip"]+"")
                    print("Expiry: "+urljson["expiry"]+"")
        
            # Delete user
            if userscommand == "2":
                username = input("Username> ")
                URL = requests.get("https://developers.auth.gg/USERS/?type=delete&authorization=" + AUTHKEY + "&user=" + username)
                urljson = URL.json()
                print("Status: "+urljson["status"]+"")
                print("Info: "+urljson["info"]+"")
            
            # Edit user variable
            if userscommand == "3":
                username = input("Username> ")
                variable = input("Variable> ")
                URL = requests.get("https://developers.auth.gg/USERS/?type=editvar&authorization=" + AUTHKEY + "&user=" + username + "&value=" + variable)
                urljson = URL.json()
                print("Status: "+urljson["status"]+"")
                print("Info: "+urljson["info"]+"")
                
            # Change password
            if userscommand == "4":
                username = input("Username> ")
                password = input("Password> ")
                URL = requests.get("https://developers.auth.gg/USERS/?type=changepw&authorization=" + AUTHKEY + "&user=" + username + "&password=" + password)
                urljson = URL.json()
                print("Status: "+urljson["status"]+"")
                print("Info: "+urljson["info"]+"")
                
            # User Count
            if userscommand == "5":
                URL = requests.get("https://developers.auth.gg/USERS/?type=count&authorization=" + AUTHKEY)
                urljson = URL.json()
                print("Status: "+urljson["status"]+"")
                print("Value: "+urljson["value"]+"")
        
        # License
        if command == "2":
            os.system("cls")
            print(BANNER)
            print("\t[1] Generate Licenses")
            print("\t[2] Unuse License")
            print("\t[3] Use License")
            print("\t[4] Delete License")
            print("\t[5] License information")
            print("\t[6] Count Licenses")
            licensecommand = input("> ")
            
            # Generate Licenses 
            if licensecommand == "1":
                days = input("Days> ")
                amount = input("Amount (maximum 25)> ")
                level = input("Level> ")
                URL = requests.get("https://developers.auth.gg/LICENSES/?type=generate&days=" + days + "&amount=" + amount + "&level=" + level + "&authorization=" + AUTHKEY)
                urljson = URL.json()
                for x in range(0, int(amount)):
                    print("" + str(urljson[str(x)]) + "")
            
            # Unuse License
            if licensecommand == "2":
                license = input("License> ")
                URL = requests.get("https://developers.auth.gg/LICENSES/?type=unuse&license=" + license + "&authorization=" + AUTHKEY)
                urljson = URL.json()
                print("Status: "+urljson["status"]+"")
                print("Info: "+urljson["info"]+"")
                
            # Use License
            if licensecommand == "3":
                license = input("License> ")
                URL = requests.get("https://developers.auth.gg/LICENSES/?type=use&license=" + license + "&authorization=" + AUTHKEY)
                urljson = URL.json()
                print("Status: "+urljson["status"]+"")
                print("Info: "+urljson["info"]+"")
            
            # Delete License
            if licensecommand == "4":
                license = input("License> ")
                URL = requests.get("https://developers.auth.gg/LICENSES/?type=delete&license=" + license + "&authorization=" + AUTHKEY)
                urljson = URL.json()
                print("Status: "+urljson["status"]+"")
                print("Info: "+urljson["info"]+"")
                
            
            # License Information
            if licensecommand == "5":
                license = input("License> ")
                URL = requests.get("https://developers.auth.gg/LICENSES/?type=fetch&authorization=" + AUTHKEY + "&license=" + license)
                urljson = URL.json()
                print("Status: "+urljson["status"]+"")
                print("License: "+urljson["license"]+"")
                print("Rank: "+urljson["rank"]+"")
                print("Used: "+urljson["used"]+"")
                print("Used by: "+urljson["used_by"]+"")
                print("Created: "+urljson["created"]+"")
                
            
            # Count Licenses
            if licensecommand == "6":
                URL = requests.get("https://developers.auth.gg/LICENSES/?type=count&authorization=" + AUTHKEY)
                urljson = URL.json()
                print("Status: "+urljson["status"]+"")
                print("Total: "+urljson["value"]+"")
        
        if command == "3":
            os.system("cls")
            print(BANNER)
            print("\t[1] HWID Information")
            print("\t[2] Reset HWID from License")
            hwidcommand = input("> ")
            
            # HWID Information
            if hwidcommand == "1":
                license = input("License> ")
                URL = requests.get("https://developers.auth.gg/HWID/?type=fetch&authorization=" + AUTHKEY + "&user=" + license)
                urljson = URL.json()
                print("Status: "+urljson["status"]+"")
                print("Info: "+urljson["value"]+"")
            
            # Reset HWID from License
            if hwidcommand == "2":
                license = input("License> ")
                URL = requests.get("https://developers.auth.gg/HWID/?type=reset&authorization=" + AUTHKEY + "&user=" + license)
                urljson = URL.json()
                print("Status: "+urljson["status"]+"")
                print("Value: "+urljson["value"]+"")
            
    
    elif CheckAuthKey(AUTHKEY) == False:
        print("Auth key is invalid!")
    
    
if __name__ == "__main__":
    main()