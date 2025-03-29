import re

class IBAN_Checker:
    config = {
        "countries":[
            {
                "country":"Albania",
                "length":28,
                "code":"AL",
                "format":"AL,2n,8n,16c"
            },
            {
                "country":"Andorra",
                "length":24,
                "code":"AD",
                "format":"AD,2n,8n,12c"
            },
            {
                "country":"Austria",
                "length":20,
                "code":"AT",
                "format":"AT,2n,16n"
            },
            {
                "country":"Azerbaijan",
                "length":28,
                "code":"AZ",
                "format":"AZ,2n,4a,20c"
            },
            {
                "country":"Bahrain",
                "length":22,
                "code":"BH",
                "format":"BH,2n,4a,14c"
            },
            {
                "country":"Belarus",
                "length":28,
                "code":"BY",
                "format":"BY,2n,4c,4n,16c"
            },
            {
                "country":"Belgium",
                "length":16,
                "code":"BE",
                "format":"BE,2n,12n"
            },
            {
                "country":"Bosnia and Herzegovina",
                "length":20,
                "code":"BA",
                "format":"BA,2n,16n"
            },
            {
                "country":"Brazil",
                "length":29,
                "code":"BR",
                "format":"BR,2n,23n,1a,1c"
            },
            {
                "country":"British Virgin Islands",
                "length":24,
                "code":"VG",
                "format":"VG,2n,4a,16n"
            },
            {
                "country":"Bulgaria",
                "length":22,
                "code":"BG",
                "format":"BG,2n,4a,6n,8c"
            },
            {
                "country":"Costa Rica",
                "length":22,
                "code":"CR",
                "format":"CR,2n,18n"
            },
            {
                "country":"Croatia",
                "length":21,
                "code":"HR",
                "format":"HR,2n,17n"
            },
            {
                "country":"Cyprus",
                "length":28,
                "code":"CY",
                "format":"CY,2n,8n,16c"
            },
            {
                "country":"Czech Republic",
                "length":24,
                "code":"CZ",
                "format":"CZ,2n,20n"
            },
            {
                "country":"Denmark",
                "length":18,
                "code":"DK",
                "format":"DK,2n,14n"
            },
            {
                "country":"Dominican Republic",
                "length":28,
                "code":"DO",
                "format":"DO,2n,4c,20n"
            },
            {
                "country":"Egypt",
                "length":29,
                "code":"EG",
                "format":"EG,2n,25n"
            },
            {
                "country":"El Salvador",
                "length":28,
                "code":"SV",
                "format":"SV,2n,4a,20n"
            },
            {
                "country":"Estonia",
                "length":20,
                "code":"EE",
                "format":"EE,2n,16n"
            },
            {
                "country":"Faroe Islands",
                "length":18,
                "code":"FO",
                "format":"FO,2n,14n"
            },
            {
                "country":"Finland",
                "length":18,
                "code":"FI",
                "format":"FI,2n,14n"
            },
            {
                "country":"France",
                "length":27,
                "code":"FR",
                "format":"FR,2n,10n,11c,2n"
            },
            {
                "country":"French Guiana",
                "length":27,
                "code":"GF",
                "format":"GF,2n,10n,11c,2n"
            },
            {
                "country":"French Polynesia",
                "length":27,
                "code":"PF",
                "format":"PF,2n,10n,11c,2n"
            },
            {
                "country":"French Southern Territories",
                "length":27,
                "code":"TF",
                "format":"TF,2n,10n,11c,2n"
            },
            {
                "country":"Georgia",
                "length":22,
                "code":"GE",
                "format":"GE,2n,2a,16n"
            },
            {
                "country":"Germany",
                "length":22,
                "code":"DE",
                "format":"DE,2n,18n"
            },
            {
                "country":"Gibraltar",
                "length":23,
                "code":"GI",
                "format":"GI,2n,4a,15c"
            },
            {
                "country":"Greece",
                "length":27,
                "code":"GR",
                "format":"GR,2n,7n,16c"
            },
            {
                "country":"Greenland",
                "length":18,
                "code":"GL",
                "format":"GL,2n,14n"
            },
            {
                "country":"Guadelope",
                "length":27,
                "code":"GP",
                "format":"GP,2n,10n,11c,2n"
            },
            {
                "country":"Guatemala",
                "length":28,
                "code":"GT",
                "format":"GT,2n,4c,20c"
            },
            {
                "country":"Hungary",
                "length":28,
                "code":"HU",
                "format":"HU,2n,24n"
            },
            {
                "country":"Iceland",
                "length":26,
                "code":"IS",
                "format":"IS,2n,22n"
            },
            {
                "country":"Ireland",
                "length":22,
                "code":"IE",
                "format":"IE,2n,4a,6n,8n"
            },
            {
                "country":"Israel",
                "length":23,
                "code":"IL",
                "format":"IL,2n,19n"
            },
            {
                "country":"Italy",
                "length":27,
                "code":"IT",
                "format":"IT,2n,1a,10n,12c"
            },
            {
                "country":"Jordan",
                "length":30,
                "code":"JO",
                "format":"JO,2n,4a,4n,18c"
            },
            {
                "country":"Kazakhstan",
                "length":20,
                "code":"KZ",
                "format":"KZ,2n,3n,13c"
            },
            {
                "country":"Kosovo",
                "length":20,
                "code":"XK",
                "format":"XK,2n,4n,10n,2n"
            },
            {
                "country":"Kuwait",
                "length":30,
                "code":"KW",
                "format":"KW,2n,4a,22c"
            },
            {
                "country":"Latvia",
                "length":21,
                "code":"LV",
                "format":"LV,2n,4a,13c"
            },
            {
                "country":"Lebanon",
                "length":28,
                "code":"LB",
                "format":"LB,2n,4n,20c"
            },
            {
                "country":"Liechtenstein",
                "length":21,
                "code":"LI",
                "format":"LI,2n,5n,12c"
            },
            {
                "country":"Lithuania",
                "length":20,
                "code":"LT",
                "format":"LT,2n,16n"
            },
            {
                "country":"Luxembourg",
                "length":20,
                "code":"LU",
                "format":"LU,2n,3n,13c"
            },
            {
                "country":"Macedonia",
                "length":19,
                "code":"MK",
                "format":"MK,2n,3n,10c,2n"
            },
            {
                "country":"Malta",
                "length":31,
                "code":"MT",
                "format":"MT,2n,4a,5n,18c"
            },
            {
                "country":"Martinique",
                "length":27,
                "code":"MQ",
                "format":"MQ,2n,10n,11c,2n"
            },
            {
                "country":"Mauritania",
                "length":27,
                "code":"MR",
                "format":"MR,2n,10n,11c,2n"
            },
            {
                "country":"Mauritius",
                "length":30,
                "code":"MU",
                "format":"MU,2n,4a,19n,3a"
            },
            {
                "country":"Mayotte",
                "length":27,
                "code":"YT",
                "format":"YT,2n,10n,11c,2n"
            },
            {
                "country":"Moldova",
                "length":24,
                "code":"MD",
                "format":"MD,2n,2c,18c"
            },
            {
                "country":"Monaco",
                "length":27,
                "code":"MC",
                "format":"MC,2n,10n,11c,2n"
            },
            {
                "country":"Montenegro",
                "length":22,
                "code":"ME",
                "format":"ME,2n,18n"
            },
            {
                "country":"Netherlands",
                "length":18,
                "code":"NL",
                "format":"NL,2n,4a,10n"
            },
            {
                "country":"New Caledonia",
                "length":27,
                "code":"NC",
                "format":"NC,2n,10n,11c,2n"
            },
            {
                "country":"Norway",
                "length":15,
                "code":"NO",
                "format":"NO,2n,11n"
            },
            {
                "country":"Pakistan",
                "length":24,
                "code":"PK",
                "format":"PK,2n,4a,16c"
            },
            {
                "country":"Palestine",
                "length":29,
                "code":"PS",
                "format":"PS,2n,4a,21c"
            },
            {
                "country":"Poland",
                "length":28,
                "code":"PL",
                "format":"PL,2n,24n"
            },
            {
                "country":"Portugal",
                "length":25,
                "code":"PT",
                "format":"PT,2n,21n"
            },
            {
                "country":"Qatar",
                "length":29,
                "code":"QA",
                "format":"QA,2n,4a,21c"
            },
            {
                "country":"Romania",
                "length":24,
                "code":"RO",
                "format":"RO,2n,4a,16c"
            },
            {
                "country":"Saint Barhelemy",
                "length":27,
                "code":"BL",
                "format":"BL,2n,10n,11c,2n"
            },
            {
                "country":"Saint Lucia",
                "length":32,
                "code":"LC",
                "format":"LC,2n,4a,24c"
            },
            {
                "country":"Saint Martin",
                "length":27,
                "code":"MF",
                "format":"MF,2n,10n,11c,2n"
            },
            {
                "country":"Saint Pierre et Miquelon",
                "length":27,
                "code":"PM",
                "format":"PM,2n,10n,11c,2n"
            },
            {
                "country":"San Marino",
                "length":27,
                "code":"SM",
                "format":"SM,2n,1a,10n,12c"
            },
            {
                "country":"Sao Tome And Principe",
                "length":25,
                "code":"ST",
                "format":"ST,2n,21n"
            },
            {
                "country":"Saudi Arabia",
                "length":24,
                "code":"SA",
                "format":"SA,2n,2n,18c"
            },
            {
                "country":"Serbia",
                "length":22,
                "code":"RS",
                "format":"RS,2n,18n"
            },
            {
                "country":"Seychelles",
                "length":31,
                "code":"SC",
                "format":"SC,2n,4a,20n,3a"
            },
            {
                "country":"Slovakia",
                "length":24,
                "code":"SK",
                "format":"SK,2n,20n"
            },
            {
                "country":"Slovenia",
                "length":19,
                "code":"SI",
                "format":"SI,2n,15n"
            },
            {
                "country":"Spain",
                "length":24,
                "code":"ES",
                "format":"ES,2n,20n"
            },
            {
                "country":"Sweden",
                "length":24,
                "code":"SE",
                "format":"SE,2n,20n"
            },
            {
                "country":"Switzerland",
                "length":21,
                "code":"CH",
                "format":"CH,2n,5n,12c"
            },
            {
                "country":"Timor-Leste",
                "length":23,
                "code":"TL",
                "format":"TL,2n,19n"
            },
            {
                "country":"Tunisia",
                "length":24,
                "code":"TN",
                "format":"TN,2n,20n"
            },
            {
                "country":"Turkey",
                "length":26,
                "code":"TR",
                "format":"TR,2n,5n,1n,16c"
            },
            {
                "country":"Ukraine",
                "length":29,
                "code":"UA",
                "format":"UA,2n,6n,19c"
            },
            {
                "country":"United Arab Emirates",
                "length":23,
                "code":"AE",
                "format":"AE,2n,3n,16n"
            },
            {
                "country":"United Kingdom",
                "length":22,
                "code":"GB",
                "format":"GB,2n,4a,14n"
            },
            {
                "country":"Vatican City State",
                "length":22,
                "code":"VA",
                "format":"VA,2n,3n,15n"
            },
            {
                "country":"Wallis and Futuna Islands",
                "length":27,
                "code":"WF",
                "format":"WF,2n,10n,11c,2n"
            }
        ]
    }

    def __init__(self):
        self.regex_string = self.generate_regexp()

    @classmethod
    def get_length(cls, code):
        for p in cls.config['countries']:
            if p['code'] == code:
                return p['length']

    # Let's get the IBAN formatted in blocks of 4 digits
    @classmethod
    def format_iban(cls, iban):
        iban = iban.replace(' ', '')
        return ' '.join(iban[i:i + 4] for i in range(0, len(iban), 4))

    # Generate regexp for all countries in the config
    @classmethod
    def generate_regexp(cls):
        regex_string = r'('
        for p in cls.config['countries']:
            regex_string += r'(?:' + f'{p["code"]}'
            for f in p['format'].split(',')[1:]:
                if f[-1] == 'a':
                    regex_string += r'(?:[\s\-]*[a-zA-Z]){' + f'{f[:-1]}' + r'}'
                elif f[-1] == 'n':
                    regex_string += r'(?:[\s\-]*[0-9]){' + f'{f[:-1]}' + r'}'
                elif f[-1] == 'c':
                    regex_string += r'(?:[\s\-]*[a-zA-Z0-9]){' + f'{f[:-1]}' + r'}'
            regex_string += r')|'
        regex_string = regex_string[:-1] + r')'
        return regex_string
    
    # Let's call the validator
    @classmethod
    def validate_iban(cls, iban):
        # let's eliminate the empty spaces
        iban = iban.replace(' ', '').replace('-', '')

        # let's control the input data type
        if not iban.isalnum():
            return False

        # (step 1) Check that the total IBAN length is correct
        code = (iban[0:2].upper())
        length = cls.get_length(code)

        if not code.isalpha():
            return False

        if len(iban) != int(length):
            return False

        # (step 2) Move the four initial characters to the end of the string (i.e., the country code and the check digits)
        iban_rearranged = (iban[4:] + iban[0:4]).upper()

        # (step 3) Replace each letter in the string with two digits, thereby expanding the string, where A = 10, B = 11 .. Z = 35;
        iban2 = ''
        for ch in iban_rearranged:
            if ch.isdigit():
                iban2 += ch
            else:
                iban2 += str(10 + ord(ch) - ord('A'))

        # (step 4) Interpret the string as a decimal integer and compute the remainder of that number on division by 97;
        # If the remainder is 1, the check digit test is passed and the IBAN might be valid.
        ibann = int(iban2)
        if ibann % 97 == 1:
            return True
        else:
            return False

    def find_iban(self, text, return_if_valid=True):
        iban_list = []
        for regex_result in re.findall(self.regex_string, text):
            if return_if_valid:
                if self.validate_iban(regex_result):
                    iban_list.append(regex_result)
            else:
                iban_list.append(regex_result)            
        return iban_list