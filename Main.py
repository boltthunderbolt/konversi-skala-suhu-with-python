from libs import temperatureConverter
from libs import temperatureUnit

## Temperature Converter
#* Sumber : Wikipedia
'''
  - Kelvin     - Fahrenheit     - Celcius      - Reamur
  - Rankine    - Delisle        - Newton       - Romer
'''

def main():
  temperatureUnit.show_list_of_units()
  temperatureConverter.user_input()
  temperatureConverter.show_results()

if __name__ == '__main__':
  main()