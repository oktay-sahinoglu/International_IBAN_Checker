# International_IBAN_Checker
Extract IBAN numbers from text, validate IBAN numbers found. Config based international coverage.

## Installation
Just add `src/iban_checker.py` file to your project.

## Config
```
config = {
    "countries":[
        {
            "country":"Turkey",
            "length":26,
            "code":"TR",
            "format":"TR,2n,5n,1n,16c"
        },
        {
            "country":"United Kingdom",
            "length":22,
            "code":"GB",
            "format":"GB,2n,4a,14n"
        }
    ]
}
```
Above is a fragment of the config. The config inside the code contains configurations for 87 different countries. New countries can be added to the config.
```
format: code, iban blocks

a: alphabets (letters only), c: characters (letters & numbers), n: numbers (numbers only)

E.g.: XX,2n,4a,16c means country code(XX) then 2 numbers then 4 letters then 16 characters 
```

## Usage
Assuming it is run from the path contains `iban_checker.py`.

```
>>> from iban_checker import IBAN_Checker
>>> iban_checker = IBAN_Checker()

>>> iban_checker.find_iban("I want to check the balance of my account with GB 29 NWBK 601613 31926819 iban number.")
['GB 29 NWBK 601613 31926819']
```
Let's change one digit in the IBAN and try again.
```
>>> iban_checker.find_iban("I want to check the balance of my account with GB 28 NWBK 601613 31926819 iban number.")
[]
```
It returned empty list because IBAN is not valid. You can control validation check with `return_if_valid` parameter, which is `True` by default.
```
>>> iban_checker.find_iban("I want to check the balance of my account with GB 28 NWBK 601613 31926819 iban number.", return_if_valid=False)
['GB 28 NWBK 601613 31926819']
```

Spaces and space positions among IBAN blocks does not affect the functionality.

```
>>> iban_checker.find_iban("I want to check the balance of my account with GB29 NWBK 6016 1331 9268 19 iban number.")
['GB29 NWBK 6016 1331 9268 19']

>>> iban_checker.find_iban("I want to check the balance of my account with GB29NWBK60161331926819 iban number.")
['GB29NWBK60161331926819']
```

You can perform validation check with or without creating an instance.
```
>>> iban_checker.validate_iban("GB29 NWBK 6016 1331 9268 19")
True

>>> IBAN_Checker.validate_iban("GB29 NWBK 6016 1331 9268 19")
True
```
Let's change one digit in the IBAN again.
```
>>> iban_checker.validate_iban("GB28 NWBK 6016 1331 9268 19")
False

>>> IBAN_Checker.validate_iban("GB28 NWBK 6016 1331 9268 19")
False
```
