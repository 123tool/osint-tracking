import requests
from concurrent.futures import ThreadPoolExecutor
from core.banner import Wh, Cy, Re, Ye, Gr, Bl, display_user_banner

def check_site(site, username):
    url = site['url'].format(username)
    try:
        response = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200:
            return site['name'], url, True
    except:
        pass
    return site['name'], url, False

def track_username_footprint():
    display_user_banner()
    try:
        username = input(f"\n {Wh}Enter Targeted Username : {Cy}")
        print(f"\n {Wh}========== {Cy}THREADED ALIAS FOOTPRINT ENUMERATION {Wh}==========")
        print(f" {Wh}[*] Launching parallel checking vectors...\n")
        
        social_media = [
            {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.twitter.com/{}", "name": "Twitter/X"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
            {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
            {"url": "https://www.youtube.com/{}", "name": "Youtube"},
            {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
            {"url": "https://www.behance.net/{}", "name": "Behance"},
            {"url": "https://www.medium.com/@{}", "name": "Medium"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
            {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
            {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
            {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
            {"url": "https://www.telegram.me/{}", "name": "Telegram"},
            {"url": "https://pastebin.com/u/{}", "name": "Pastebin User"},
            {"url": "https://www.reddit.com/user/{}", "name": "Reddit User"}
        ]

        with ThreadPoolExecutor(max_workers=15) as executor:
            futures = [executor.submit(check_site, site, username) for site in social_media]
            for future in futures:
                name, url, found = future.result()
                if found:
                    print(f" {Wh}[ {Gr}+ {Wh}] {name:<15} : {Gr}{url}")
                else:
                    print(f" {Wh}[ {Re}- {Wh}] {name:<15} : {Bl}Account Not Found")
                    
    except KeyboardInterrupt:
        print(f" {Wh}[{Ye}!{Wh}] {Ye}PROCESS TERMINATED...")
