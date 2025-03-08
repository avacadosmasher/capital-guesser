#!/usr/bin/env python3

import random

# List of capitals and their count
capital_list=[["Afghanistan" , "Kabul"],["Albania" , "Tirana"],["Algeria" , "Algiers"],["Andorra" , "Andorra la Vella"],["Angola" , "Luanda"],["Antigua and Barbuda" , "Saint Johns"],["Argentina" , "Buenos Aires"],["Armenia" , "Yerevan"],["Australia" , "Canberra"],["Austria" , "Vienna"],["Azerbaijan" , "Baku"],["The Bahamas" , "Nassau"],["Bahrain" , "Manama"],["Bangladesh" , "Dhaka"],["Barbados" , "Bridgetown"],["Belarus" , "Minsk"],["Belgium" , "Brussels"],["Belize" , "Belmopan"],["Benin" , "Porto-Novo"],["Bhutan" , "Thimphu"],["Bolivia" , "La Paz"],["Bosnia and Herzegovina" , "Sarajevo"],["Botswana" , "Gaborone"],["Brazil" , "Brasilia"],["Brunei" , "Bandar Seri Begawan"],["Bulgaria" , "Sofia"],["Burkina Faso" , "Ouagadougou"],["Burundi" , "Bujumbura"],["Cambodia" , "Phnom Penh"],["Cameroon" , "Yaounde"],["Canada" , "Ottawa"],["Cape Verde" , "Praia"],["Central African Republic" , "Bangui"],["Chad" , "NDjamena"],["Chile" , "Santiago"],["China" , "Beijing"],["Colombia" , "Bogota"],["Comoros" , "Moroni"],["Republic of the Congo", "Brazzaville"],["Democratic Republic of the Congo" , "Kinshasa"],["Costa Rica" , "San Jose"],["Cote dIvoire" , "Yamoussoukro"],["Croatia" , "Zagreb"],["Cuba" , "Havana"],["Cyprus" , "Nicosia"],["Czech Republic" , "Prague"],["Denmark" , "Copenhagen"],["Djibouti" , "Djibouti"],["Dominica" , "Roseau"],["Dominican Republic" , "Santo Domingo"],["East Timor" , "Dili"],["Ecuador" , "Quito"],["Egypt" , "Cairo"],["El Salvador" , "San Salvador"],["Equatorial Guinea" , "Malabo"],["Eritrea" , "Asmara"],["Estonia" , "Tallinn"],["Ethiopia" , "Addis Ababa"],["Fiji" , "Suva"],["Finland" , "Helsinki"],["France" , "Paris"],["Gabon" , "Libreville"],["The Gambia" , "Banjul"],["Georgia" , "Tbilisi"],["Germany" , "Berlin"],["Ghana" , "Accra"],["Greece" , "Athens"],["Grenada" , "Saint George’s"],["Guatemala" , "Guatemala City"],["Guinea" , "Conakry"],["Guinea-Bissau" , "Bissau"],["Guyana" , "Georgetown"],["Haiti" , "Port-au-Prince"],["Honduras" , "Tegucigalpa"],["Hungary" , "Budapest"],["Iceland" , "Reykjavik"],["India" , "New Delhi"],["Indonesia" , "Jakarta"],["Iran" , "Tehran"],["Iraq" , "Baghdad"],["Ireland" , "Dublin"],["Israel" , "Jerusalem"],["Italy" , "Rome"],["Jamaica" , "Kingston"],["Japan" , "Tokyo"],["Jordan" , "Amman"],["Kazakhstan" , "Astana"],["Kenya" , "Nairobi"],["Kiribati" , "Tarawa Atoll"],["North Korea" , "Pyongyang"],["South Korea" , "Seoul"],["Kosovo" , "Pristina"],["Kuwait" , "Kuwait City"],["Kyrgyzstan" , "Bishkek"],["Laos" , "Vientiane"],["Latvia" , "Riga"],["Lebanon" , "Beirut"],["Lesotho" , "Maseru"],["Liberia" , "Monrovia"],["Libya" , "Tripoli"],["Liechtenstein" , "Vaduz"],["Lithuania" , "Vilnius"],["Luxembourg" , "Luxembourg"],["Macedonia" , "Skopje"],["Madagascar" , "Antananarivo"],["Malawi" , "Lilongwe"],["Malaysia" , "Kuala Lumpur"],["Maldives" , "Male"],["Mali" , "Bamako"],["Malta" , "Valletta"],["Marshall Islands" , "Majuro"],["Mauritania" , "Nouakchott"],["Mauritius" , "Port Louis"],["Mexico" , "Mexico City"],["Federated States of Micronesia" , "Palikir"],["Moldova" , "Chisinau"],["Monaco" , "Monaco"],["Mongolia" , "Ulaanbaatar"],["Montenegro" , "Podgorica"],["Morocco" , "Rabat"],["Mozambique" , "Maputo"],["Myanmar" , "Naypyidaw"],["Namibia" , "Windhoek"],["Nauru" , "Yaren District"],["Nepal" , "Kathmandu"],["Netherlands" , "Amsterdam"],["New Zealand" , "Wellington"],["Nicaragua" , "Managua"],["Niger" , "Niamey"],["Nigeria" , "Abuja"],["Norway" , "Oslo"],["Oman" , "Muscat"],["Pakistan" , "Islamabad"],["Palau" , "Melekeok"],["Panama" , "Panama City"],["Papua New Guinea" , "Port Moresby"],["Paraguay" , "Asuncion"],["Peru" , "Lima"],["Philippines" , "Manila"],["Poland" , "Warsaw"],["Portugal" , "Lisbon"],["Qatar" , "Doha"],["Romania" , "Bucharest"],["Russia" , "Moscow"],["Rwanda" , "Kigali"],["Saint Kitts and Nevis" , "Basseterre"],["Saint Lucia" , "Castries"],["Saint Vincent and the Grenadines" , "Kingstown"],["Samoa" , "Apia"],["San Marino" , "San Marino"],["Sao Tome and Principe" , "Sao Tome"],["Saudi Arabia" , "Riyadh"],["Senegal" , "Dakar"],["Serbia" , "Belgrade"],["Seychelles" , "Victoria"],["Sierra Leone" , "Freetown"],["Singapore" , "Singapore"],["Slovakia" , "Bratislava"],["Slovenia" , "Ljubljana"],["Solomon Islands" , "Honiara"],["Somalia" , "Mogadishu"],["South Africa" , "Cape Town"],["South Sudan" , "Juba"],["Spain" , "Madrid"],["Sri Lanka" , "Colombo"],["Sudan" , "Khartoum"],["Suriname" , "Paramaribo"],["Swaziland" , "Mbabane"],["Sweden" , "Stockholm"],["Switzerland" , "Bern"],["Syria" , "Damascus"],["Taiwan" , "Taipei"],["Tajikistan" , "Dushanbe"],["Tanzania" , "Dodoma"],["Thailand" , "Bangkok"],["Togo" , "Lome"],["Tonga" , "Nuku’alofa"],["Trinidad and Tobago" , "Port-of-Spain"],["Tunisia" , "Tunis"],["Turkey" , "Ankara"],["Turkmenistan" , "Ashgabat"],["Tuvalu" , "Funafuti"],["Uganda" , "Kampala"],["Ukraine" , "Kyiv"],["United Arab Emirates" , "Abu Dhabi"],["United Kingdom" , "London"],["United States of America" , "Washington D.C."],["Uruguay" , "Montevideo"],["Uzbekistan" , "Tashkent"],["Vanuatu" , "Port-Vila"],["Vatican City" , "Vatican City"],["Venezuela" , "Caracas"],["Vietnam" , "Hanoi"],["Yemen" , "Sanaa"],["Zambia" , "Lusaka"],["Zimbabwe" , "Harare"]]
capital_count=len(capital_list)

score=0
guess="start"

print("Have fun, press q to quit! ")

while guess != 'q':

    random_number=random.randint(0,capital_count)

    country,capital=capital_list[random_number]

    guess=input("what is the capital of %s? " % country)

    if guess.lower() == capital.lower():
        print("Great job!")
        score = score + 1
    elif guess == "q":
        print ("bye")
    else:
        print("Whoops, thats not right")
    
print("Well done, your score is",score)
