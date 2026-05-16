import os
from sys import stderr

# Terminal Colors
Bl = '\033[30m'
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_main_banner():
    clear_screen()
    stderr.writelines(f"""{Cy}
    ____        __                                     ____  _____ _____   __  __
   / __ \____ _/ /_____ _     _____  ____  _________  / __ \/ ___//_  _/  /  |/  /
  / / / / __ `/ __/ __ `/ |  / / _ \/ __ \/ ___/ _ \ / / / /\__ \  / /   / /|_/ / 
 / /_/ / /_/ / /_/ /_/ /| |/ /  __/ / / / /__/  __// /_/ /___/ /_/ /_  / /  / /  
/_____/\__,_/\__/\__,_/ |___/\___/_/ /_/\___/\___/ \____//____//_____/ /_/  /_/   
                                                                                  
          {Wh}[ + ]  MULTIPLE INTELLIGENCE AGGREGATOR SYSTEM  [ + ]  
        
    {Wh}[ 1 ] {Cy}IP Tracker (Target IP Address)
    {Wh}[ 2 ] {Cy}Show Your Local/Public IP Info
    {Wh}[ 3 ] {Cy}Phone Tracker & Carrier Analysis
    {Wh}[ 4 ] {Cy}Asynchronous Username Tracker
    {Wh}[ 0 ] {Re}Exit System
""")

def display_ip_banner():
    clear_screen()
    stderr.writelines(f"""{Cy}
  ___ ____    _____               _               
 |_ _|  _ \  |_   _| __ __ _  ___| | _____ _ __   
  | || |_) |   | || '__/ _` |/ __| |/ / _ \ '__|  
  | ||  __/    | || | | (_| | (__|   <  __/ |     
 |___|_|       |_|_|  \__,_|\___|_|\_\___|_|     
                                                  
    """)

def display_myip_banner():
    clear_screen()
    stderr.writelines(f"""{Cy}
 __     __                _            ____  
 \ \   / /__  _   _ _ __ (_) _ __     |  _ \ 
  \ \ / / _ \| | | | '__|| || '_ \    | |_) |
   \ V / (_) | |_| | |   | || |_) |   |  __/ 
    \_/ \___/ \__,_|_|   |_|| .__/    |_|    
                            |_|              
""")

def display_phone_banner():
    clear_screen()
    stderr.writelines(f"""{Cy}
  ____  _                      _____               _               
 |  _ \| |__   ___  _ __   ___|_   _| __ __ _  ___| | _____ _ __   
  | |_) | '_ \ / _ \| '_ \ / _ \| || '___/ _` |/ __| |/ / _ \ '__|  
  |  __/| | | | (_) | | | |  __/| || |  | (_| | (__|   <  __/ |     
 |_|    |_| |_|\___/|_| |_|\___||_||_|   \__,_|\___|_|\_\___|_|     
                                                                    
    """)

def display_user_banner():
    clear_screen()
    stderr.writelines(f"""{Cy}
  _   _                                           _____               _               
 | | | |___  ___ _ __ _ __   __ _ _ __ ___   ___ |_   _| __ __ _  ___| | _____ _ __   
  | ||  __/  | || | | (_| | (__|   <  __/ |     
   \___/|___/\___|_|  |_| |_|\__,_|_| |_| |_|\___||_||_|   \__,_|\___|_|\_\___|_|     
                                                                                      
    """)
