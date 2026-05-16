import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from core.banner import Wh, Cy, Re, Ye, display_phone_banner

def track_phone_number():
    display_phone_banner()
    try:
        User_phone = input(f"\n {Wh}Enter Mobile Number Target {Cy}Ex [+628xxxxxxxxxx] {Wh}: {Cy}")
        default_region = "ID"

        parsed_number = phonenumbers.parse(User_phone, default_region)
        region_code = phonenumbers.region_code_for_number(parsed_number)
        jenis_provider = carrier.name_for_number(parsed_number, "en")
        location = geocoder.description_for_number(parsed_number, "id")
        is_valid_number = phonenumbers.is_valid_number(parsed_number)
        is_possible_number = phonenumbers.is_possible_number(parsed_number)
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        number_type = phonenumbers.number_type(parsed_number)
        timezone1 = timezone.time_zones_for_number(parsed_number)
        timezoneF = ', '.join(timezone1)

        print(f"\n {Wh}========== {Cy}PARSING CELLULAR CARRIER TELEMETRY {Wh}==========")
        print(f"\n {Wh}Base Registration Area:{Cy} {location}")
        print(f" {Wh}ISO Region Code      :{Cy} {region_code}")
        print(f" {Wh}Network Timezone     :{Cy} {timezoneF}")
        print(f" {Wh}Telco Operator       :{Cy} {jenis_provider}")
        print(f" {Wh}Integrity Status     :{Cy} Valid={is_valid_number} | Match Probability={is_possible_number}")
        print(f" {Wh}International Format :{Cy} {formatted_number}")
        print(f" {Wh}National Dial E.164  :{Cy} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
        
        clean_national = parsed_number.national_number
        print(f" {Wh}Public Intel Pivot   :{Cy} https://scannumber.org/lookup?number={clean_national}")

        if number_type == phonenumbers.PhoneNumberType.MOBILE:
            print(f" {Wh}Infrastructure Type  :{Cy} Assigned to standard Mobile Core Network")
        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            print(f" {Wh}Infrastructure Type  :{Cy} Assigned to Landline Infrastructure (Fixed)")
        else:
            print(f" {Wh}Infrastructure Type  :{Cy} VOIP/Virtual or Restricted Infrastructure")
            
    except KeyboardInterrupt:
        print(f" {Wh}[{Ye}!{Wh}] {Ye}PROCESS TERMINATED...")
    except Exception as e:
        print(f" {Re}[!] Input data corruption or formatting invalid: {str(e)}")
