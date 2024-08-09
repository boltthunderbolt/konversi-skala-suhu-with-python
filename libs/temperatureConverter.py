from libs import temperatureUnit
from time import sleep

temperature_unit_lists = temperatureUnit.temperature_units
def user_input():
  global first_unit_selected, second_unit_selected, values
  while True:
    first_unit_selected = int(input("\nSelect the first unit temperature: "))
    first_unit_selected -= 1
    print(f'{temperature_unit_lists[first_unit_selected]} selected')
    
    values = int(input("Input the value here: "))

    second_unit_selected = int(input("Convert to: "))
    second_unit_selected -= 1
    print(f'{temperature_unit_lists[second_unit_selected]} selected\n')

    if first_unit_selected == second_unit_selected :
      print(f"Cannot converted with the same unit {temperature_unit_lists[first_unit_selected]} & {temperature_unit_lists[second_unit_selected]}. Try Again!\n")
      sleep(2)
    else: break

def show_results():
  results = temperatureUnit.temperature_converter_list(temperatureUnit.temperature_units[first_unit_selected], temperatureUnit.temperature_units[second_unit_selected], values)
  print(f"\nThe result of {values} {temperatureUnit.temperature_units[first_unit_selected].capitalize()} to {temperatureUnit.temperature_units[second_unit_selected].capitalize()} is {results}")

if __name__ == '__main__':
  user_input()
  show_results()