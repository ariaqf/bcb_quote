# BCB Quote
Program to obtain the smallest exchange rate between USD and other currencies from the BCB (Brazilian Central Bank). If it doesn't manage to find a quote it will print x in the terminal, if other errors raise it will print an error message in the terminal

## Setup
This program depends on two libraries which you can install from the deps.txt file or using the commands:
```
pip install pycountry
pip install requests
```

## Usage
the program is pretty straightforward in which it receives a date as a parameter and downloads the relevant data from the BCB.
Afterwards it tries to use the pycountry library to fetch data, if it fails it uses a fallback dict that was extracted from wikipedia.

```
$ python main.py "20100104"
S/., Ecuador, 0.00004000
```

Or yet, if you want to get the currency code:

```
$ python main.py "20100104" 1
ECS, S/., Ecuador, 0.00004000
```

## Considerations
I would have prefered to use the iso tables or only libraries to get both the symbol and country name, but the iso table gives the countries using the currency and not the issuer. Also, the symbol is pretty hard to guess and all of the libraries, webservices and files in the internet miss some of those currencies, in special the VES and ECS weren't both in any of those resources.

Also i got a bit sidetracked in extracting the data from wikipedia and lost a lot of the allotted time.