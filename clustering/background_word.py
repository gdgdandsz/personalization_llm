import pandas as pd

data = pd.read_csv("/scratch/wd2148/data_1016.csv")

country_code = {  # cc3_cn - Three Letter ISO Country Code to Country Name
    'AFG': 'Afghanistan',
    'ALA': 'Aland Islands',
    'ALB': 'Albania',
    'DZA': 'Algeria',
    'ASM': 'American Samoa',
    'AND': 'Andorra',
    'AGO': 'Angola',
    'AIA': 'Anguilla',
    'ATA': 'Antarctica',
    'ATG': 'Antigua and Barbuda',
    'ARG': 'Argentina',
    'ARM': 'Armenia',
    'ABW': 'Aruba',
    'AUS': 'Australia',
    'AUT': 'Austria',
    'AZE': 'Azerbaijan',
    'BHS': 'Bahamas',
    'BHR': 'Bahrain',
    'BGD': 'Bangladesh',
    'BRB': 'Barbados',
    'BLR': 'Belarus',
    'BEL': 'Belgium',
    'BLZ': 'Belize',
    'BEN': 'Benin',
    'BMU': 'Bermuda',
    'BTN': 'Bhutan',
    'BOL': 'Bolivia',
    'BIH': 'Bosnia and Herzegovina',
    'BWA': 'Botswana',
    'BVT': 'Bouvet Island',
    'BRA': 'Brazil',
    'VGB': 'British Virgin Islands',
    'IOT': 'British Indian Ocean Territory',
    'BRN': 'Brunei Darussalam',
    'BGR': 'Bulgaria',
    'BFA': 'Burkina Faso',
    'BDI': 'Burundi',
    'KHM': 'Cambodia',
    'CMR': 'Cameroon',
    'CAN': 'Canada',
    'CPV': 'Cape Verde',
    'CYM': 'Cayman Islands',
    'CAF': 'Central African Republic',
    'TCD': 'Chad',
    'CHL': 'Chile',
    'CHN': 'China',
    'HKG': 'Hong Kong, Special Administrative Region of China',
    'MAC': 'Macao, Special Administrative Region of China',
    'CXR': 'Christmas Island',
    'CCK': 'Cocos (Keeling) Islands',
    'COL': 'Colombia',
    'COM': 'Comoros',
    'COG': 'Congo (Brazzaville)',
    'COD': 'Congo, Democratic Republic of the',
    'COK': 'Cook Islands',
    'CRI': 'Costa Rica',
    'CIV': 'Cote d\'Ivoire',
    'HRV': 'Croatia',
    'CUB': 'Cuba',
    'CYP': 'Cyprus',
    'CZE': 'Czech Republic',
    'DNK': 'Denmark',
    'DJI': 'Djibouti',
    'DMA': 'Dominica',
    'DOM': 'Dominican Republic',
    'ECU': 'Ecuador',
    'EGY': 'Egypt',
    'SLV': 'El Salvador',
    'GNQ': 'Equatorial Guinea',
    'ERI': 'Eritrea',
    'EST': 'Estonia',
    'ETH': 'Ethiopia',
    'FLK': 'Falkland Islands (Malvinas)',
    'FRO': 'Faroe Islands',
    'FJI': 'Fiji',
    'FIN': 'Finland',
    'FRA': 'France',
    'GUF': 'French Guiana',
    'PYF': 'French Polynesia',
    'ATF': 'French Southern Territories',
    'GAB': 'Gabon',
    'GMB': 'Gambia',
    'GEO': 'Georgia',
    'DEU': 'Germany',
    'GHA': 'Ghana',
    'GIB': 'Gibraltar',
    'GRC': 'Greece',
    'GRL': 'Greenland',
    'GRD': 'Grenada',
    'GLP': 'Guadeloupe',
    'GUM': 'Guam',
    'GTM': 'Guatemala',
    'GGY': 'Guernsey',
    'GIN': 'Guinea',
    'GNB': 'Guinea-Bissau',
    'GUY': 'Guyana',
    'HTI': 'Haiti',
    'HMD': 'Heard Island and Mcdonald Islands',
    'VAT': 'Holy See (Vatican City State)',
    'HND': 'Honduras',
    'HUN': 'Hungary',
    'ISL': 'Iceland',
    'IND': 'India',
    'IDN': 'Indonesia',
    'IRN': 'Iran, Islamic Republic of',
    'IRQ': 'Iraq',
    'IRL': 'Ireland',
    'IMN': 'Isle of Man',
    'ISR': 'Israel',
    'ITA': 'Italy',
    'JAM': 'Jamaica',
    'JPN': 'Japan',
    'JEY': 'Jersey',
    'JOR': 'Jordan',
    'KAZ': 'Kazakhstan',
    'KEN': 'Kenya',
    'KIR': 'Kiribati',
    'PRK': 'Korea, Democratic People\'s Republic of',
    'KOR': 'Korea, Republic of',
    'KWT': 'Kuwait',
    'KGZ': 'Kyrgyzstan',
    'LAO': 'Lao PDR',
    'LVA': 'Latvia',
    'LBN': 'Lebanon',
    'LSO': 'Lesotho',
    'LBR': 'Liberia',
    'LBY': 'Libya',
    'LIE': 'Liechtenstein',
    'LTU': 'Lithuania',
    'LUX': 'Luxembourg',
    'MKD': 'Macedonia, Republic of',
    'MDG': 'Madagascar',
    'MWI': 'Malawi',
    'MYS': 'Malaysia',
    'MDV': 'Maldives',
    'MLI': 'Mali',
    'MLT': 'Malta',
    'MHL': 'Marshall Islands',
    'MTQ': 'Martinique',
    'MRT': 'Mauritania',
    'MUS': 'Mauritius',
    'MYT': 'Mayotte',
    'MEX': 'Mexico',
    'FSM': 'Micronesia, Federated States of',
    'MDA': 'Moldova',
    'MCO': 'Monaco',
    'MNG': 'Mongolia',
    'MNE': 'Montenegro',
    'MSR': 'Montserrat',
    'MAR': 'Morocco',
    'MOZ': 'Mozambique',
    'MMR': 'Myanmar',
    'NAM': 'Namibia',
    'NRU': 'Nauru',
    'NPL': 'Nepal',
    'NLD': 'Netherlands',
    'ANT': 'Netherlands Antilles',
    'NCL': 'New Caledonia',
    'NZL': 'New Zealand',
    'NIC': 'Nicaragua',
    'NER': 'Niger',
    'NGA': 'Nigeria',
    'NIU': 'Niue',
    'NFK': 'Norfolk Island',
    'MNP': 'Northern Mariana Islands',
    'NOR': 'Norway',
    'OMN': 'Oman',
    'PAK': 'Pakistan',
    'PLW': 'Palau',
    'PSE': 'Palestinian Territory, Occupied',
    'PAN': 'Panama',
    'PNG': 'Papua New Guinea',
    'PRY': 'Paraguay',
    'PER': 'Peru',
    'PHL': 'Philippines',
    'PCN': 'Pitcairn',
    'POL': 'Poland',
    'PRT': 'Portugal',
    'PRI': 'Puerto Rico',
    'QAT': 'Qatar',
    'REU': 'Reunion',
    'ROU': 'Romania',
    'RUS': 'Russian Federation',
    'RWA': 'Rwanda',
    'BLM': 'Saint-Barthelemy',
    'SHN': 'Saint Helena',
    'KNA': 'Saint Kitts and Nevis',
    'LCA': 'Saint Lucia',
    'MAF': 'Saint-Martin (French part)',
    'SPM': 'Saint Pierre and Miquelon',
    'VCT': 'Saint Vincent and Grenadines',
    'WSM': 'Samoa',
    'SMR': 'San Marino',
    'STP': 'Sao Tome and Principe',
    'SAU': 'Saudi Arabia',
    'SEN': 'Senegal',
    'SRB': 'Serbia',
    'SYC': 'Seychelles',
    'SLE': 'Sierra Leone',
    'SGP': 'Singapore',
    'SVK': 'Slovakia',
    'SVN': 'Slovenia',
    'SLB': 'Solomon Islands',
    'SOM': 'Somalia',
    'ZAF': 'South Africa',
    'SGS': 'South Georgia and the South Sandwich Islands',
    'SSD': 'South Sudan',
    'ESP': 'Spain',
    'LKA': 'Sri Lanka',
    'SDN': 'Sudan',
    'SUR': 'Suriname',
    'SJM': 'Svalbard and Jan Mayen Islands',
    'SWZ': 'Swaziland',
    'SWE': 'Sweden',
    'CHE': 'Switzerland',
    'SYR': 'Syrian Arab Republic (Syria)',
    'TWN': 'Taiwan, Republic of China',
    'TJK': 'Tajikistan',
    'TZA': 'Tanzania, United Republic of',
    'THA': 'Thailand',
    'TLS': 'Timor-Leste',
    'TGO': 'Togo',
    'TKL': 'Tokelau',
    'TON': 'Tonga',
    'TTO': 'Trinidad and Tobago',
    'TUN': 'Tunisia',
    'TUR': 'Turkey',
    'TKM': 'Turkmenistan',
    'TCA': 'Turks and Caicos Islands',
    'TUV': 'Tuvalu',
    'UGA': 'Uganda',
    'UKR': 'Ukraine',
    'ARE': 'United Arab Emirates',
    'GBR': 'United Kingdom',
    'USA': 'United States of America',
    'UMI': 'United States Minor Outlying Islands',
    'URY': 'Uruguay',
    'UZB': 'Uzbekistan',
    'VUT': 'Vanuatu',
    'VEN': 'Venezuela (Bolivarian Republic of)',
    'VNM': 'Viet Nam',
    'VIR': 'Virgin Islands, US',
    'WLF': 'Wallis and Futuna Islands',
    'ESH': 'Western Sahara',
    'YEM': 'Yemen',
    'ZMB': 'Zambia',
    'ZWE': 'Zimbabwe'
}

country_code_num = {# m49_cn - ISO Numeric Code UN M49 Numerical Code
    4: 'Afghanistan',
    8: 'Albania',
    10: 'Antarctica',
    12: 'Algeria',
    16: 'American Samoa',
    20: 'Andorra',
    24: 'Angola',
    28: 'Antigua and Barbuda',
    31: 'Azerbaijan',
    32: 'Argentina',
    36: 'Australia',
    40: 'Austria',
    44: 'Bahamas',
    48: 'Bahrain',
    50: 'Bangladesh',
    51: 'Armenia',
    52: 'Barbados',
    56: 'Belgium',
    60: 'Bermuda',
    64: 'Bhutan',
    68: 'Bolivia',
    70: 'Bosnia and Herzegovina',
    72: 'Botswana',
    74: 'Bouvet Island',
    76: 'Brazil',
    84: 'Belize',
    86: 'British Indian Ocean Territory',
    90: 'Solomon Islands',
    92: 'British Virgin Islands',
    96: 'Brunei Darussalam',
    100: 'Bulgaria',
    104: 'Myanmar',
    108: 'Burundi',
    112: 'Belarus',
    116: 'Cambodia',
    120: 'Cameroon',
    124: 'Canada',
    132: 'Cape Verde',
    136: 'Cayman Islands',
    140: 'Central African Republic',
    144: 'Sri Lanka',
    148: 'Chad',
    152: 'Chile',
    156: 'China',
    158: 'Taiwan, Republic of China',
    162: 'Christmas Island',
    166: 'Cocos (Keeling) Islands',
    170: 'Colombia',
    174: 'Comoros',
    175: 'Mayotte',
    178: 'Congo (Brazzaville)',
    180: 'Congo, Democratic Republic of the',
    184: 'Cook Islands',
    188: 'Costa Rica',
    191: 'Croatia',
    192: 'Cuba',
    196: 'Cyprus',
    203: 'Czech Republic',
    204: 'Benin',
    208: 'Denmark',
    212: 'Dominica',
    214: 'Dominican Republic',
    218: 'Ecuador',
    222: 'El Salvador',
    226: 'Equatorial Guinea',
    231: 'Ethiopia',
    232: 'Eritrea',
    233: 'Estonia',
    234: 'Faroe Islands',
    238: 'Falkland Islands (Malvinas)',
    239: 'South Georgia and the South Sandwich Islands',
    242: 'Fiji',
    246: 'Finland',
    248: 'Aland Islands',
    250: 'France',
    254: 'French Guiana',
    258: 'French Polynesia',
    260: 'French Southern Territories',
    262: 'Djibouti',
    266: 'Gabon',
    268: 'Georgia',
    270: 'Gambia',
    275: 'Palestinian Territory, Occupied',
    276: 'Germany',
    288: 'Ghana',
    292: 'Gibraltar',
    296: 'Kiribati',
    300: 'Greece',
    304: 'Greenland',
    308: 'Grenada',
    312: 'Guadeloupe',
    316: 'Guam',
    320: 'Guatemala',
    324: 'Guinea',
    328: 'Guyana',
    332: 'Haiti',
    334: 'Heard Island and Mcdonald Islands',
    336: 'Holy See (Vatican City State)',
    340: 'Honduras',
    344: 'Hong Kong, Special Administrative Region of China',
    348: 'Hungary',
    352: 'Iceland',
    356: 'India',
    360: 'Indonesia',
    364: 'Iran, Islamic Republic of',
    368: 'Iraq',
    372: 'Ireland',
    376: 'Israel',
    380: 'Italy',
    384: 'Cote d\'Ivoire',
    388: 'Jamaica',
    392: 'Japan',
    398: 'Kazakhstan',
    400: 'Jordan',
    404: 'Kenya',
    408: 'Korea, Democratic People\'s Republic of',
    410: 'Korea, Republic of',
    414: 'Kuwait',
    417: 'Kyrgyzstan',
    418: 'Lao PDR',
    422: 'Lebanon',
    426: 'Lesotho',
    428: 'Latvia',
    430: 'Liberia',
    434: 'Libya',
    438: 'Liechtenstein',
    440: 'Lithuania',
    442: 'Luxembourg',
    446: 'Macao, Special Administrative Region of China',
    450: 'Madagascar',
    454: 'Malawi',
    458: 'Malaysia',
    462: 'Maldives',
    466: 'Mali',
    470: 'Malta',
    474: 'Martinique',
    478: 'Mauritania',
    480: 'Mauritius',
    484: 'Mexico',
    492: 'Monaco',
    496: 'Mongolia',
    498: 'Moldova',
    499: 'Montenegro',
    500: 'Montserrat',
    504: 'Morocco',
    508: 'Mozambique',
    512: 'Oman',
    516: 'Namibia',
    520: 'Nauru',
    524: 'Nepal',
    528: 'Netherlands',
    530: 'Netherlands Antilles',
    533: 'Aruba',
    540: 'New Caledonia',
    548: 'Vanuatu',
    554: 'New Zealand',
    558: 'Nicaragua',
    562: 'Niger',
    566: 'Nigeria',
    570: 'Niue',
    574: 'Norfolk Island',
    578: 'Norway',
    580: 'Northern Mariana Islands',
    581: 'United States Minor Outlying Islands',
    583: 'Micronesia, Federated States of',
    584: 'Marshall Islands',
    585: 'Palau',
    586: 'Pakistan',
    591: 'Panama',
    598: 'Papua New Guinea',
    600: 'Paraguay',
    604: 'Peru',
    608: 'Philippines',
    612: 'Pitcairn',
    616: 'Poland',
    620: 'Portugal',
    624: 'Guinea-Bissau',
    626: 'Timor-Leste',
    630: 'Puerto Rico',
    634: 'Qatar',
    638: 'Reunion',
    642: 'Romania',
    643: 'Russian Federation',
    646: 'Rwanda',
    652: 'Saint-Barthelemy',
    654: 'Saint Helena',
    659: 'Saint Kitts and Nevis',
    660: 'Anguilla',
    662: 'Saint Lucia',
    663: 'Saint-Martin (French part)',
    666: 'Saint Pierre and Miquelon',
    670: 'Saint Vincent and Grenadines',
    674: 'San Marino',
    678: 'Sao Tome and Principe',
    682: 'Saudi Arabia',
    686: 'Senegal',
    688: 'Serbia',
    690: 'Seychelles',
    694: 'Sierra Leone',
    702: 'Singapore',
    703: 'Slovakia',
    704: 'Viet Nam',
    705: 'Slovenia',
    706: 'Somalia',
    710: 'South Africa',
    716: 'Zimbabwe',
    724: 'Spain',
    728: 'South Sudan',
    732: 'Western Sahara',
    736: 'Sudan',
    740: 'Suriname',
    744: 'Svalbard and Jan Mayen Islands',
    748: 'Swaziland',
    752: 'Sweden',
    756: 'Switzerland',
    760: 'Syrian Arab Republic (Syria)',
    762: 'Tajikistan',
    764: 'Thailand',
    768: 'Togo',
    772: 'Tokelau',
    776: 'Tonga',
    780: 'Trinidad and Tobago',
    784: 'United Arab Emirates',
    788: 'Tunisia',
    792: 'Turkey',
    795: 'Turkmenistan',
    796: 'Turks and Caicos Islands',
    798: 'Tuvalu',
    800: 'Uganda',
    804: 'Ukraine',
    807: 'Macedonia, Republic of',
    818: 'Egypt',
    826: 'United Kingdom',
    831: 'Guernsey',
    832: 'Jersey',
    833: 'Isle of Man',
    834: 'Tanzania, United Republic of',
    840: 'United States of America',
    850: 'Virgin Islands, US',
    854: 'Burkina Faso',
    858: 'Uruguay',
    860: 'Uzbekistan',
    862: 'Venezuela (Bolivarian Republic of)',
    876: 'Wallis and Futuna Islands',
    882: 'Samoa',
    887: 'Yemen',
    894: 'Zambia',
}


race_dict = {
    # Andorra
    20001: "Andorra: Caucasian white",
    20002: "Andorra: Negro black",
    20003: "Andorra: South Asian (Indian, Pakistani, etc.)",
    20004: "Andorra: East Asian (Chinese, Japanese, etc.)",
    20005: "Andorra: Arabic, Central Asian",
    20999: "Andorra: Other",

    # Argentina
    32001: "Argentina: White",
    32002: "Argentina: Light brown",
    32003: "Argentina: Dark brown",
    32004: "Argentina: Black",
    32005: "Argentina: Indigenous",
    32999: "Argentina: Other",

    # Australia
    36001: "Australia: Australian (English speaking)",
    36002: "Australia: European",
    36003: "Australia: South Asian (Indian, Pakistani, etc.)",
    36004: "Australia: East Asian (Chinese, Japanese, etc.)",
    36005: "Australia: Arabic, Central Asian",
    36006: "Australia: Southeast Asian (Thai, Vietnamese, Malaysian, etc.)",
    36007: "Australia: Aboriginal or Torres Strait Islander",
    36999: "Australia: Other",

    # Bangladesh
    50006: "Bangladesh: Bengali",
    50007: "Bangladesh: Chakma",
    50008: "Bangladesh: Murong",

    # Armenia
    51001: "Armenia: Armenian",
    51005: "Armenia: Russian",
    51006: "Armenia: Yazidis",
    51007: "Armenia: Other",

    # Bolivia
    68001: "Bolivia: Not pertaining to Indigenous groups",
    68002: "Bolivia: Quechua",
    68003: "Bolivia: Aymara",
    68004: "Bolivia: Guaraní",
    68005: "Bolivia: Chiquitano",
    68006: "Bolivia: Mojeño",
    68007: "Bolivia: Afroboliviano",
    68008: "Bolivia: Indigenous with no further detail",
    68999: "Bolivia: Other",

    # Brazil
    76001: "Brazil: White",
    76002: "Brazil: Black",
    76003: "Brazil: Brown - Moreno ou pardo",
    76004: "Brazil: Oriental (Chinese, Japanese, etc.)",
    76005: "Brazil: Indigenous",

    # Myanmar
    104001: "Myanmar: Bamar",
    104002: "Myanmar: Kayin",
    104003: "Myanmar: Rakhine",
    104004: "Myanmar: Shan",
    104005: "Myanmar: Mon",
    104999: "Myanmar: Other",

    # Canada
    124001: "Canada: Caucasian (White)",
    124002: "Canada: Black (African, African-American, etc.)",
    124003: "Canada: West Asian (Iranian, Afghan, etc.)",
    124004: "Canada: Southeast Asian (Vietnamese, Cambodian, Malaysian, etc.)",
    124005: "Canada: Arabic (Central Asia)",
    124006: "Canada: South Asian (Indian, Bangladeshi, Pakistani, Sri Lankan)",
    124007: "Canada: Latin American / Hispanic",
    124008: "Canada: Aboriginal / First Nations",
    124009: "Canada: Chinese",
    124010: "Canada: Filipino",
    124011: "Canada: Korean",
    124012: "Canada: Japanese",
    124999: "Canada: Other",

    # Chile
    152001: "Chile: White, Caucasian",
    152002: "Chile: Black",
    152008: "Chile: Indigenous",
    152009: "Chile: Asiatic",
    152012: "Chile: Mestizo(a)",
    152013: "Chile: Mulatto(a)",
    152999: "Chile: Other",

    # China
    156001: "China: Chinese",

    # Taiwan ROC
    158001: "Taiwan ROC: Hakka from Taiwan",
    158002: "Taiwan ROC: Minnanese from Taiwan",
    158003: "Taiwan ROC: Mainlander/China",
    158004: "Taiwan ROC: Aboriginal",
    158999: "Taiwan ROC: Other",

    # Colombia
    170008: "Colombia: Afro-colombian",
    170009: "Colombia: Gypsie",
    170010: "Colombia: Indigenous",
    170011: "Colombia: White",
    170999: "Colombia: Other",

    # Cyprus
    196001: "Cyprus: Caucasian white",
    196003: "Cyprus: South Asian Indian, Pakistani, etc.",
    196005: "Cyprus: Arabic, Central Asian",

    # Czechia
    203004: "Czechia: Slovak",
    203005: "Czechia: Polish",
    203006: "Czechia: Ukrainian",
    203010: "Czechia: Other",

    # Ecuador
    218011: "Ecuador: Blanco",
    218012: "Ecuador: Mestizo",
    218013: "Ecuador: Negro",
    218014: "Ecuador: Indígena",
    218017: "Ecuador: Montubio",
    218018: "Ecuador: Mulato",

    # Ethiopia
    231001: "Ethiopia: Amhara",
    231002: "Ethiopia: Tigre",
    231003: "Ethiopia: Oromo",
    231004: "Ethiopia: Somali",
    231005: "Ethiopia: Afar",
    231006: "Ethiopia: Sidama",
    231007: "Ethiopia: Wolayta",
    231998: "Ethiopia: Other Africans/Negro Black",
    231999: "Ethiopia: Other",

    # Greece
    300001: "Greece: Caucasian white",
    300002: "Greece: Negro Black",
    300004: "Greece: East Asian (Chinese, Japanese, etc.)",
    300005: "Greece: Arabic, Central Asian",

    # Guatemala
    320001: "Guatemala: Ladino",
    320002: "Guatemala: Cross breed",
    320003: "Guatemala: Brown",
    320004: "Guatemala: Indigenous",
    320005: "Guatemala: White",
    320006: "Guatemala: Hispanic",

    # Hong Kong SAR PRC
    344001: "Hong Kong SAR PRC: Chinese",
    344002: "Hong Kong SAR PRC: Filipino",
    344003: "Hong Kong SAR PRC: Indonesian",
    344004: "Hong Kong SAR PRC: White",
    344005: "Hong Kong SAR PRC: Indian",
    344006: "Hong Kong SAR PRC: Nepalese",
    344007: "Hong Kong SAR PRC: Pakistani",
    344008: "Hong Kong SAR PRC: Thai",
    344998: "Hong Kong SAR PRC: Other Asian",
    344999: "Hong Kong SAR PRC: Other",
    
    # Additional entries for other countries...
}


def format_background(row, country_code, country_code_num, race_dict):
    background = []

    # 性别 (Q260)
    gender = (
    'Male' if row['Q260'] == 1 else 
    'Female' if row['Q260'] == 2 else 
    'no answer' if row['Q260'] == -2 else 
    'Unknown'
)

    background.append(f" {gender}")
    
    # 年龄 (Q262)
    background.append(f" {'No answer' if row['Q262'] == -2 else row['Q262']} years old")
    
    # 移民信息 (Q263, Q264, Q265)
    immigrant = (
        'An immigrant' if row['Q263'] == 2 else 
        'no answer about if itself is an immigrant or not' if row['Q263'] == -2 else
        'Do not know if itself is an immigrant or not' if row['Q263'] == -1 else 
        'A local person')
    background.append(f" {immigrant}")
    
    mother_immigrant = (
        'Mother is an Immigrant' if row['Q264'] == 2 else
        "no answer about if it's mother is an immigrant or not" if row['Q264'] == -2 else
        "Do not know if it's mother is an immigrant or not" if row['Q264'] == -1 else 
        'Mother is a local person')
    background.append(f"{mother_immigrant}")
    
    father_immigrant = ('Father is an Immigrant' if row['Q265'] == 2 else
                        "no answer about if it's father is an immigrant or not" if row['Q265'] == -2 else
                        "Do not know if it's father is an immigrant or not" if row['Q265'] == -1 else 
                        'Father is a local person')
    background.append(f"{father_immigrant}")
    
    #出生国家
    
    if row['Q266'] == -2:
        country_b = 'Respondent gives no answer about where themself is from'
    elif row['Q266'] == -1:
        country_b = "Respondent doesn't know where themself is from"
    else:
        country_b = country_code_num.get(row['Q266'], 'Unknown Country')

    background.append(f"{country_b}")

    
    # 国籍 (Q269)
    citizen = 'The respondent is a citizen of this country.' if row['Q269'] == 1 else 'No. the respondent is not a citizen of this country'
    background.append(f"{citizen}")
    
    # 家庭规模 (Q270)
    background.append(f"- There are {'No answer' if row['Q270'] == -2 else 'Do not know' if row['Q270'] == -1 else row['Q270']} member in the respondent's family")
    
    # 是否与父母同住 (Q271)
    live_with_parents = ('Live with own parent(s)' if row['Q271'] == 2 else
                        'No answer' if row['Q271'] == -2 else
                        'Do not know' if row['Q271'] == -1 else 
                        "No applicable" if row['Q271']==-4 else
                        'Live with parent(s) in law' if row['Q271'] == 3 else
                        'Live with both own parent(s) and parent(s) in law' if row['Q271'] == 4 else 
                        'does not live with parents')
    background.append(f"{live_with_parents}")
    
    # 婚姻状况 (Q273)
    marital_status_map = {1: 'Married', 2: 'Living together as married', 3: 'Divorced', 4: 'Separated', 5: 'Widowed', 6: 'Single', -1: 'Do not know', -2: 'No answer'}
    marital_status = marital_status_map.get(row['Q273'], 'Other')
    background.append(f" {marital_status}")
    
    # 子女数量 (Q274)
    quantity = ('No answer' if row['Q274'] == -2 else 
                'Do not know' if row['Q274'] == -1 else 
                row['Q274'])
    background.append(f"Has {quantity} children")
    
    # 受教育程度 (Q275)
    education_map = {0: 'no education', 1: 'Primary education', 2: 'Lower secondary education', 
                    3: 'Upper secondary education', 4: 'Post-secondary non-tertiary education', 
                    5: 'Short-cycle tertiary education', 6: 'Bachelor or equivalent', 7: 'Master or equivalent', 
                    8: 'Doctoral or equivalent', -1: 'Do not know', -2: 'No answer', -3:'No applicable/No spouse'}
    education = education_map.get(row['Q275'], 'Other Education')
    background.append(f"{education}")
    
    spouse_education = education_map.get(row['Q276'], 'Other Education')
    background.append(f"- Spouse is {spouse_education}")
    
    mother_education = education_map.get(row['Q277'], 'Other Education')
    background.append(f"- Mother is {mother_education}")
    
    father_education = education_map.get(row['Q278'], 'Other Education')
    background.append(f"- Father is {father_education}")
    
    
    # 就业状况 (Q279)
    employment_status_map = {1: 'Full-time', 2: 'Part-time', 3: 'Self-employed', 4: 'Retired', 5: 'Housewife not otherwise employed', 6: 'Student', 7: 'Unemployed', 8: 'Other', -1: 'Do not know', -2: 'No answer', -3:'No applicable/No spouse'}
    employment_status = employment_status_map.get(row['Q279'], 'Other')
    background.append(f"{employment_status} employment ")
    
    spouse_employment_status = employment_status_map.get(row['Q280'], 'Other')
    background.append(f"- Spouse is {spouse_employment_status} employment.")
    
    
    ###
    # Q281: Respondent's occupational group
    occupational_group_map = {
        0: "Never had a job",
        1: "Professional and technical (e.g., doctor, teacher, engineer, accountant, nurse)",
        2: "Higher administrative (e.g., banker, executive, union official)",
        3: "Clerical (e.g., secretary, clerk, civil servant)",
        4: "Sales (e.g., sales manager, shop assistant, insurance agent)",
        5: "Service (e.g., restaurant owner, police officer, barber)",
        6: "Skilled worker (e.g., foreman, electrician, printer)",
        7: "Semi-skilled worker (e.g., bricklayer, bus driver, carpenter)",
        8: "Unskilled worker (e.g., labourer, cleaner)",
        9: "Farm worker (e.g., farm labourer, tractor driver)",
        10: "Farm owner or manager",
        11: "Other",
        -1: "Don't know",
        -2: "No answer",
        -3:'No applicable/No spouse'
    }
    occupation = occupational_group_map.get(row['Q281'], 'Unknown')
    background.append(f"- Occupational group: {occupation}")

    # Q282: Respondent's spouse's occupational group
    spouse_occupation = occupational_group_map.get(row['Q282'], 'Unknown')
    background.append(f"- Spouse's group: {spouse_occupation}")

    # Q283: Respondent's father's occupational group when respondent was 14 years old
    father_occupation = occupational_group_map.get(row['Q283'], 'Unknown')
    background.append(f"- Father's group: {father_occupation}")

    # Q284: Sector of employment
    employment_sector_map = {
        1: "Government or public institution",
        2: "Private business or industry",
        3: "Private non-profit organization",
        -1: "Don't know",
        -2: "No answer",
        -3: "Not applicable; Never had a job"
    }
    employment_sector = employment_sector_map.get(row['Q284'], 'Unknown')
    background.append(f"- belongs to {employment_sector} sector")

    # Q285: Chief wage earner in the house
    chief_wage_earner_map = {
        1: "is",
        2: "Not",
        -1: "Don't know whether the respondent is",
        -2: "No answer about whether the respondent is"
    }
    chief_wage_earner = chief_wage_earner_map.get(row['Q285'], 'Unknown')
    background.append(f"- {chief_wage_earner} chief wage earner in the house.")

    # Q286: Family savings during the past year
    family_savings_map = {
        1: "Saved money",
        2: "Just got by",
        3: "Spent some savings and borrowed money",
        4: "Spent savings and borrowed money",
        -1: "Don't know",
        -2: "No answer"
    }
    family_savings = family_savings_map.get(row['Q286'], 'Unknown')
    background.append(f"{family_savings}")

        
    # 社会阶层 (Q287)
    social_class_map = {1: 'Upper class', 2: 'Upper middle class', 3: 'Lower middle class', 4: 'Working class', 5: 'Lower class',
        -1: "Don't know",
        -2: "No answer"}
    social_class = social_class_map.get(row['Q287'], 'Unknown')
    background.append(f"Social {social_class}")
    
    # 宗教信仰 (Q289)
    religion_map = {0: 'No religion', 1: 'Roman Catholic', 2: 'Protestant', 3: 'Orthodox', 5: 'Muslim', 6: 'Hindu', 7: 'Buddhist', 8: 'Other',
        -1: "Don't know",
        -2: "No answer"}
    religion = religion_map.get(row['Q289'], 'No Answer')
    background.append(f"{religion}")
    
    # 收入等级 (Q288)
    income_group_map = {
        1: "Lowest income group",
        2: "Low income group",
        3: "Low-medium income group",
        4: "Medium income group",
        5: "Medium-high income group",
        6: "High income group",
        7: "Very high income group",
        8: "Upper high income group",
        9: "Near highest income group",
        10: "Highest income group",
        -1: "Don't know",
        -2: "No answer"
    }
    income_group = income_group_map.get(row['Q288'], 'Unknown')
    background.append(f"{income_group}")
    
    # 种族/民族 (Q290)
    ethnic_group = race_dict.get(row['Q290'], 'Unknown')
    background.append(f"{ethnic_group} ethnic group")
    
    # 国家 (B_COUNTRY_ALPHA)
    country = country_code.get(row['B_COUNTRY_ALPHA'], 'Unknown Country')
    background.append(f"from {country}")
    
    return "\n".join(background)

data['Background_Prompt'] = data.apply(format_background, country_code=country_code, country_code_num=country_code_num, race_dict=race_dict,axis=1)

output_path = "/scratch/wd2148/word_prompt_data.csv"
data.to_csv(output_path, index=False)

# Optionally, view the first few rows of the new column
#print(data[['Background_Prompt']].head())
