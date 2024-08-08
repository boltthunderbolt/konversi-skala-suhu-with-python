from libs import temperatureUnit

def user_input():
  global first_unit_selected, second_unit_selected, values
  first_unit_selected = int(input("Select the first unit temperature: "));
  first_unit_selected = first_unit_selected - 1;
  print(f'{temperatureUnit.temperature_units[first_unit_selected]} selected');
  
  values = int(input("Input the value here\n-> "))

  second_unit_selected = int(input("Convert to: "));
  second_unit_selected = second_unit_selected - 1;
  print(f'{temperatureUnit.temperature_units[second_unit_selected]} selected');

def show_results():
  results = temperatureUnit.temperature_converter_list(temperatureUnit.temperature_units[first_unit_selected], temperatureUnit.temperature_units[second_unit_selected], values)
  print(f"\nThe result of {values} {temperatureUnit.temperature_units[first_unit_selected].capitalize()} to {temperatureUnit.temperature_units[second_unit_selected].capitalize()} is {results}\n\n\n");


if __name__ == '__main__':
  user_input()
  show_results()
