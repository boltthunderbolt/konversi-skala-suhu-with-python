from libs import temperatureConverter
from libs import temperatureUnit

## Temperature Converter
#* Resource : Wikipedia
'''
  - Kelvin     - Fahrenheit     - Celcius      - Reamur
  - Rankine    - Delisle        - Newton       - Romer
'''

def main():
  print()
  temperatureUnit.show_list_of_units()
  temperatureConverter.user_input()
  temperatureConverter.show_results()
  menu()

def menu():
  while True:
    menu_program = input("Convert again? [y / n]")
    match menu_program:
      case "y" | "yes" | "Y" | "Yes" | "YES": return main()
      case "n" | "no" | "N" | "No" | "NO": break
      case _: return

if __name__ == '__main__':
  main()