import time
from core.banner import display_main_banner, Wh, Cy, Re, Ye
from core.ip_tracker import track_target_ip, track_self_ip
from core.phone_tracker import track_phone_number
from core.osint_async import track_username_footprint

def main():
    while True:
        display_main_banner()
        input_user = input(f'\n   {Wh}INVESTIGATOR-»  {Cy}')
        
        if input_user == '1':
            track_target_ip()
            input(f"\n{Wh}Press Enter to return to main menu...")
        elif input_user == '2':
            track_self_ip()
            input(f"\n{Wh}Press Enter to return to main menu...")
        elif input_user == '3':
            track_phone_number()
            input(f"\n{Wh}Press Enter to return to main menu...")
        elif input_user == '4':
            track_username_footprint()
            input(f"\n{Wh}Press Enter to return to main menu...")
        elif input_user == '0':
            print(f"\n  {Wh}[{Ye}!{Wh}] {Cy}CLOSING TERMINAL CORE INTELLIGENCE ENVIRONMENT...")
            break
        else:
            print(f" {Re}[!] Error: Option Matrix Not Registered.")
            time.sleep(1.5)

if __name__ == '__main__':
    main()
