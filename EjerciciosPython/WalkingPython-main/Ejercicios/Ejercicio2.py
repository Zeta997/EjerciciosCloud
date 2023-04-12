#Version 3.11

# Crea un programa que le pregunte al usuario su zona horaria y le muestre la hora actual en esa zona. 
from pytz import timezone
import pytz
from datetime import datetime

europe=['Amsterdam', 'Andorra', 'Astrakhan', 'Athens', 'Belfast', 'Belgrade', 'Berlin', 'Bratislava', 'Brussels', 'Bucharest', 'Budapest', 'Busingen', 'Chisinau', 'Copenhagen', 'Dublin', 'Gibraltar', 'Guernsey', 'Helsinki', 'Isle_of_Man', 'Istanbul', 'Jersey', 'Kaliningrad', 'Kiev', 'Kirov', 'Kyiv', 'Lisbon', 'Ljubljana', 'London', 'Luxembourg', 'Madrid', 'Malta', 'Mariehamn', 'Minsk', 'Monaco', 'Moscow', 'Nicosia', 'Oslo', 'Paris', 'Podgorica', 'Prague', 'Riga', 'RSamara', 'San_Marino', 'Sarajevo', 'Saratov', 'Simferopol', 'Skopje', 'Sofia', 'Stockholm', 'Tallinn', 'Tirane', 'Tiraspol', 'Ulyanovsk', 'Uzhgorod', 'Vaduz', 'Vatican', 'Vienna', 'Vilnius', 'Volgograd', 'Warsaw', 'Zagreb', 'Zaporozhye', 'Zurich']
india=['Antananarivo', 'Chagos', 'Christmas', 'Cocos', 'Comoro', 'Kerguelen', 'Mahe', 'Maldives', 'Mauritius', 'Mayotte', 'Reunion']
asia=['Aden', 'Almaty', 'Amman', 'Anadyr', 'Aqtau', 'Aqtobe', 'Ashgabat', 'Ashkhabad', 'Atyrau', 'Baghdad', 'Bahrain', 'Baku', 'Bangkok', 'Barnaul', 'Beirut', 'Bishkek', 'Brunei', 'Calcutta', 'Chita', 'Choibalsan', 'Chongqing', 'Chungking', 'Colombo', 'Dacca', 'Damascus', 'Dhaka', 'Dili', 'Dubai', 'Dushanbe', 'Famagusta', 'Gaza', 'Harbin', 'Hebron', 'Ho_Chi_Minh', 'Hong_Kong', 'Hovd', 'Irkutsk', 'Istanbul', 'Jakarta', 'Jayapura', 'Jerusalem', 'Kabul', 'Kamchatka', 'Karachi', 'Kashgar', 'Kathmandu', 'Katmandu', 'Khandyga', 'Kolkata', 'Krasnoyarsk', 'Kuala_Lumpur', 'Kuching', 'Kuwait', 'Macao', 'Macau', 'Magadan', 'Makassar', 'Manila', 'Muscat', 'Nicosia', 'Novokuznetsk', 'Novosibirsk', 'Omsk', 'Oral', 'Phnom_Penh', 'Pontianak', 'Pyongyang', 'Qatar', 'Qostanay', 'Qyzylorda', 'Rangoon', 'Riyadh', 'Saigon', 'Sakhalin', 'Samarkand', 'Seoul', 'Shanghai', 'Singapore', 'Srednekolymsk', 'Taipei', 'Tashkent', 'Tbilisi', 'Tehran', 'Tel_Aviv', 'Thimbu', 'Thimphu', 'Tokyo', 'Tomsk', 'Ujung_Pandang', 'Ulaanbaatar', 'Ulan_Bator', 'Urumqi', 'Ust-Nera', 'Vientiane', 'Vladivostok', 'Yakutsk', 'Yangon', 'Yekaterinburg', 'Yerevan']
africa=['Abidjan', 'Accra', 'Addis_Ababa', 'Algiers', 'Asmara', 'Asmera', 'Bamako', 'Bangui', 'Banjul', 'Bissau', 'Blantyre', 'Brazzaville', 'Bujumbura', 'Cairo', 'Casablanca', 'Ceuta', 'Conakry', 'Dakar', 'Dar_es_Salaam', 'Djibouti', 'Douala', 'El_Aaiun', 'Freetown', 'Gaborone', 'Harare', 'Johannesburg', 'Juba', 'Kampala', 'Khartoum', 'Kigali', 'Kinshasa', 'Lagos', 'Libreville', 'Lome', 'Luanda', 'Lubumbashi', 'Lusaka', 'Malabo', 'Maputo', 'Maseru', 'Mbabane', 'Mogadishu', 'Monrovia', 'Nairobi', 'Ndjamena', 'Niamey', 'Nouakchott', 'Ouagadougou', 'Porto-Novo', 'Sao_Tome', 'Timbuktu', 'Tripoli', 'Tunis', 'Windhoek']
america=['Adak', 'Anchorage', 'Anguilla', 'Antigua', 'Araguaina', 'Argentina/Buenos_Aires', 'Argentina/Catamarca', 'Argentina/ComodRivadavia', 'Argentina/Cordoba', 'Argentina/Jujuy', 'Argentina/La_Rioja', 'Argentina/Mendoza', 'Argentina/Rio_Gallegos', 'Argentina/Salta', 'Argentina/San_Juan', 'Argentina/San_Luis', 'Argentina/Tucuman', 'Argentina/Ushuaia', 'Aruba', 'Asuncion', 'Atikokan', 'Atka', 'Bahia', 'Bahia_Banderas', 'Barbados', 'Belem', 'Belize', 'Blanc-Sablon', 'Boa_Vista', 'Bogota', 'Boise', 'Buenos_Aires', 'Cambridge_Bay', 'Campo_Grande', 'Cancun', 'Caracas', 'Catamarca', 'Cayenne', 'Cayman', 'Chicago', 'Chihuahua', 'Ciudad_Juarez', 'Coral_Harbour', 'Cordoba', 'Costa_Rica', 'Creston', 'Cuiaba', 'Curacao', 'Danmarkshavn', 'Dawson', 'Dawson_Creek', 'Denver', 'Detroit', 'Dominica', 'Edmonton', 'Eirunepe', 'El_Salvador', 'Ensenada', 'Fort_Nelson', 'Fort_Wayne', 'Fortaleza', 'Glace_Bay', 'Godthab', 'Goose_Bay', 'Grand_Turk', 'Grenada', 'Guadeloupe', 'Guatemala', 'Guayaquil', 'Guyana', 'Halifax', 'Havana', 'Hermosillo', 'Indiana/Indianapolis', 'Indiana/Knox', 'Indiana/Marengo', 'Indiana/Petersburg', 'Indiana/Tell_City', 'Indiana/Vevay', 'Indiana/Vincennes', 'Indiana/Winamac', 'Indianapolis', 'Inuvik', 'Iqaluit', 'Jamaica', 'Jujuy', 'Juneau', 'Kentucky/Louisville', 'Kentucky/Monticello', 'Knox_IN', 'Kralendijk', 'La_Paz', 'Lima', 'Los_Angeles', 'Louisville', 'Lower_Princes', 'Maceio', 'Managua', 'Manaus', 'Marigot', 'Martinique', 'Matamoros', 'Mazatlan', 'Mendoza', 'Menominee', 'Merida', 'Metlakatla', 'Mexico_City', 'Miquelon', 'Moncton', 'Monterrey', 'Montevideo', 'Montreal', 'Montserrat', 'Nassau', 'New_York', 'Nipigon', 'Nome', 'Noronha', 'North_Dakota/Beulah', 'North_Dakota/Center', 'North_Dakota/New_Salem', 'Nuuk', 'Ojinaga', 'Panama', 'Pangnirtung', 'Paramaribo', 'Phoenix', 'Port-au-Prince', 'Port_of_Spain', 'Porto_Acre', 'Porto_Velho', 'Puerto_Rico', 'Punta_Arenas', 'Rainy_River', 'Rankin_Inlet', 'Recife', 'Regina', 'Resolute', 'Rio_Branco', 'Rosario', 'Santa_Isabel', 'Santarem', 'Santiago', 'Santo_Domingo', 'Sao_Paulo', 'Scoresbysund', 'Shiprock', 'Sitka', 'St_Barthelemy', 'St_Johns', 'St_Kitts', 'St_Lucia', 'St_Thomas', 'St_Vincent', 'Swift_Current', 'Tegucigalpa', 'Thule', 'Thunder_Bay', 'Tijuana', 'Toronto', 'Tortola', 'Vancouver', 'Virgin', 'Whitehorse', 'Winnipeg', 'Yakutat', 'Yellowknife']
atlantico=['Azores', 'Bermuda', 'Canary', 'Cape_Verde', 'Faeroe', 'Faroe', 'Jan_Mayen', 'Madeira', 'Reykjavik', 'South_Georgia', 'St_Helena', 'Stanley']
australia=['ACT', 'Adelaide', 'Brisbane', 'Broken_Hill', 'Canberra', 'Currie', 'Darwin', 'Eucla', 'Hobart', 'LHI', 'Lindeman', 'Lord_Howe', 'Melbourne', 'NSW', 'North', 'Perth', 'Queensland', 'South', 'Sydney', 'Tasmania', 'Victoria', 'West', 'Yancowinna']
brasil=['Acre', 'DeNoronha', 'East', 'West']
canada=['Atlantic', 'Central', 'Canada/Eastern', 'Canada/Mountain', 'Newfoundland', 'Pacific', 'Saskatchewan', 'Yukon']
us=['Alaska', 'Aleutian', 'Arizona', 'Central', 'East-Indiana', 'Eastern', 'Hawaii', 'Indiana-Starke', 'Michigan', 'Mountain', 'Pacific', 'Samoa']
pacifico= ['Apia', 'Auckland', 'Bougainville', 'Chatham', 'Chuuk', 'Easter', 'Efate', 'Enderbury', 'Fakaofo', 'Fiji', 'Funafuti', 'Galapagos', 'Gambier', 'Guadalcanal', 'Guam', 'Honolulu', 'Johnston', 'Kanton', 'Kiritimati', 'Kosrae', 'Kwajalein', 'Majuro', 'Marquesas', 'Midway', 'Nauru', 'Niue', 'Norfolk', 'Noumea', 'Pago_Pago', 'Palau', 'Pitcairn', 'Pohnpei', 'Ponape', 'Port_Moresby', 'Rarotonga', 'Saipan', 'Samoa', 'Tahiti', 'Tarawa', 'Tongatapu', 'Truk', 'Wake', 'Wallis', 'Yap']
mexico=['BajaNorte', 'BajaSur', 'General']
chile=['Continental', 'EasterIsland']

_zonaUsuario=""
_location=""
_esValidaZona=""


def GetCountry():
    global _zonaUsuario, _location
    while _zonaUsuario=="" or _esValidaZona==False:

        _zonaUsuario=input("Introduce tu país: ")
        CompareCountry(_zonaUsuario, _esValidaZona)
        
def CompareCountry(_country, _zonaCorrecta):

    for i in europe:
        if _country==i:
            _location=datetime.now(timezone(f'Europe/{i}'))
            _getHourSpecificLocation= _location.strftime("%H:%M:%S")
            print(_getHourSpecificLocation)
            return _zonaCorrecta==True
            break
    for i in india:
        if _country==i:
            _location=datetime.now(timezone(f'Indian/{i}'))
            _getHourSpecificLocation= _location.strftime("%H:%M:%S")
            print(_getHourSpecificLocation)
            return _zonaCorrecta==True
            break
    for i in asia:
        if _country==i:
            _location=datetime.now(timezone(f'Asia/{i}'))
            _getHourSpecificLocation= _location.strftime("%H:%M:%S")
            print(_getHourSpecificLocation)
            return _zonaCorrecta==True
            break
    for i in america:
    
        if _country==i:
            _location=datetime.now(timezone(f'America/{i}'))
            _getHourSpecificLocation= _location.strftime("%H:%M:%S")
            print(_getHourSpecificLocation)
            return _zonaCorrecta==True
            break
        elif f"Argentina/{_country}"==i:
            _location=datetime.now(timezone(f'America/{i}'))
            _getHourSpecificLocation= _location.strftime("%H:%M:%S")
            print(_getHourSpecificLocation)
            return _zonaCorrecta==True
            break
        elif f"Indiana/{_country}"==i:
            _location=datetime.now(timezone(f'America/{i}'))
            _getHourSpecificLocation= _location.strftime("%H:%M:%S")
            print(_getHourSpecificLocation)
            return _zonaCorrecta==True
            break
        elif f"Kentucky/{_country}"==i:
            _location=datetime.now(timezone(f'America/{i}'))
            _getHourSpecificLocation= _location.strftime("%H:%M:%S")
            print(_getHourSpecificLocation)
            return _zonaCorrecta==True
            break
        elif f"North_Dakota/{_country}"==i:
            _location=datetime.now(timezone(f'America/{i}'))
            _getHourSpecificLocation= _location.strftime("%H:%M:%S")
            print(_getHourSpecificLocation)
            return _zonaCorrecta==True
            break
    for i in africa:
        if _country==i:
            _location=datetime.now(timezone(f'Africa/{i}'))
            _getHourSpecificLocation= _location.strftime("%H:%M:%S")
            print(_getHourSpecificLocation)
            return _zonaCorrecta==True
            break
    for i in atlantico:
        if _country==i:
            _location=datetime.now(timezone(f'Atlantic/{i}'))
            _getHourSpecificLocation= _location.strftime("%H:%M:%S")
            print(_getHourSpecificLocation)
            return _zonaCorrecta==True
            break
    for i in australia:
        if _country==i:
            _location=datetime.now(timezone(f'Australia/{i}'))
            _getHourSpecificLocation= _location.strftime("%H:%M:%S")
            print(_getHourSpecificLocation)
            return _zonaCorrecta==True
            break
    for i in brasil:
        if _country==i:
            _location=datetime.now(timezone(f'Brazil/{i}'))
            _getHourSpecificLocation= _location.strftime("%H:%M:%S")
            print(_getHourSpecificLocation)
            return _zonaCorrecta==True
            break
    for i in canada:
        if _country==i:
            _location=datetime.now(timezone(f'Canada/{i}'))
            _getHourSpecificLocation= _location.strftime("%H:%M:%S")
            print(_getHourSpecificLocation)
            return _zonaCorrecta==True
            break
    for i in us:
        if _country==i:
            _location=datetime.now(timezone(f'US/{i}'))
            _getHourSpecificLocation= _location.strftime("%H:%M:%S")
            print(_getHourSpecificLocation)
            return _zonaCorrecta==True
            break
    for i in pacifico:
        if _country==i:
            _location=datetime.now(timezone(f'Pacific/{i}'))
            _getHourSpecificLocation= _location.strftime("%H:%M:%S")
            print(_getHourSpecificLocation)
            return _zonaCorrecta==True
            break
    for i in mexico:
        if _country==i:
            _location=datetime.now(timezone(f'Mexico/{i}'))
            _getHourSpecificLocation= _location.strftime("%H:%M:%S")
            print(_getHourSpecificLocation)
            return _zonaCorrecta==True
            break
    for i in chile:
        if _country==i:
            _location=datetime.now(timezone(f'Chile/{i}'))
            _getHourSpecificLocation= _location.strftime("%H:%M:%S")
            print(_getHourSpecificLocation)
            return _zonaCorrecta==True
            break
    print("La zona introducida no es correcta.")
    return _zonaCorrecta==False
            
            


GetCountry()
