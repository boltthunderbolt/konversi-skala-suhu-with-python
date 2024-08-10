temperature_units = ['kelvin', 'fahrenheit', 'celcius', 'reamur', 'rankine', 'delisle', 'newton', 'romer'];

def show_list_of_units():
  for index, show_unit_temperature in enumerate(temperature_units, start=1): #* menggunakan syntax enumerate(); ke variabel index, dan dimulai dari nomer 1
    print(f"{index}. {show_unit_temperature.capitalize()}");

def temperature_converter_list(first_unit_selected, second_unit_selected, values):
  # Mencari nilai konversi dari satuan Kelvin
  if first_unit_selected == temperature_units[0]:
    if second_unit_selected == temperature_units[1]: return values * 9/5 - 459.67;
    elif second_unit_selected == temperature_units[2]: return values - 273.15;
    elif second_unit_selected == temperature_units[3]: return (values - 273.15) * 4/5;
    elif second_unit_selected == temperature_units[4]: return values * 9/5;
    elif second_unit_selected == temperature_units[5]: return (373.15 - values) * 3/2;
    elif second_unit_selected == temperature_units[6]: return (values - 273.15) * 33/100;
    elif second_unit_selected == temperature_units[7]: return (values - 273.15) * 21/40 + 7.5;
    else: return;

  # Mencari nilai konversi dari satuan Fahrenheit
  elif first_unit_selected == temperature_units[1]:
    if second_unit_selected == temperature_units[0]: return (values + 459.67) * 5/9;
    elif second_unit_selected == temperature_units[2]: return (values - 32) * 5/9;
    elif second_unit_selected == temperature_units[3]: return (values - 32) * 4/9;
    elif second_unit_selected == temperature_units[4]: return values + 459.67;
    elif second_unit_selected == temperature_units[5]: return (212 - values) * 5/6;
    elif second_unit_selected == temperature_units[6]: return (values - 32) * 11/80;
    elif second_unit_selected == temperature_units[7]: return (values - 32) * 7/24 + 7.5;
    else: return;

  # Mencari nilai konversi dari satuan Celcius
  elif first_unit_selected == temperature_units[2]:
    if second_unit_selected == temperature_units[0]: return values + 273.15;
    elif second_unit_selected == temperature_units[1]: return values * 9/5 + 32;
    elif second_unit_selected == temperature_units[3]: return values * 4/5;
    elif second_unit_selected == temperature_units[4]: return (values + 273.15) * 9/5;
    elif second_unit_selected == temperature_units[5]: return (100 - values) * 3/2;
    elif second_unit_selected == temperature_units[6]: return values * 33/100;
    elif second_unit_selected == temperature_units[7]: return values * 21/40 + 7.5;
    else: return;

  # Mencari nilai konversi dari satuan Reamur
  elif first_unit_selected == temperature_units[3]:
    if second_unit_selected == temperature_units[0]: return values * 5/4 + 273.15;
    elif second_unit_selected == temperature_units[1]: return values * 9/4 + 32;
    elif second_unit_selected == temperature_units[2]: return values * 5/4;
    elif second_unit_selected == temperature_units[4]: return values * 9/4 + 491.67;
    elif second_unit_selected == temperature_units[5]: return (80 - values) * 15/8;
    elif second_unit_selected == temperature_units[6]: return values * 33/80;
    elif second_unit_selected == temperature_units[7]: return values * 21/32 + 7.5;
    else: return;
      
  # Mencari nilai konversi dari satuan Rankine
  elif first_unit_selected == temperature_units[4]:
    if second_unit_selected == temperature_units[0]: return values * 5/9;
    elif second_unit_selected == temperature_units[1]: return values - 459.67;
    elif second_unit_selected == temperature_units[2]: return (values - 491.67) * 5/9;
    elif second_unit_selected == temperature_units[3]: return (values - 491.67) * 4/9;
    elif second_unit_selected == temperature_units[5]: return (671.67 - values) * 5/6;
    elif second_unit_selected == temperature_units[6]: return (values - 491.67) * 11/80;
    elif second_unit_selected == temperature_units[7]: return (values - 491.67) * 7/24 + 7.5;
    else: return;
  
  # Mencari nilai konversi dari satuan Delisle
  elif first_unit_selected == temperature_units[5]:
    if second_unit_selected == temperature_units[0]: return 373.15 - values * 2/3;
    elif second_unit_selected == temperature_units[1]: return 212 - values * 6/5;
    elif second_unit_selected == temperature_units[2]: return 100 - values * 2/3;
    elif second_unit_selected == temperature_units[3]: return 80 - values * 8/15;
    elif second_unit_selected == temperature_units[4]: return 671.67 - values * 6/5;
    elif second_unit_selected == temperature_units[6]: return 33 - values * 11/50;
    elif second_unit_selected == temperature_units[7]: return 60 - values * 7/20;
    else: return;

  # Mencari nilai konversi dari satuan Newton
  elif first_unit_selected == temperature_units[6]:
    if second_unit_selected == temperature_units[0]: return values * 100/33 + 273.15;
    elif second_unit_selected == temperature_units[1]: return values * 60/11 + 32;
    elif second_unit_selected == temperature_units[2]: return values * 100/33;
    elif second_unit_selected == temperature_units[3]: return values * 80/33;
    elif second_unit_selected == temperature_units[4]: return values * 60/11 + 491.67;
    elif second_unit_selected == temperature_units[5]: return (33 - values) * 50/11;
    elif second_unit_selected == temperature_units[7]: return values * 35/22 + 7.5;
    else: return;

# Mencari nilai konversi dari satuan Romer
  elif first_unit_selected == temperature_units[7]:
    if second_unit_selected == temperature_units[0]: return (values - 7.5) * 40/21 + 273.15;
    elif second_unit_selected == temperature_units[1]: return (values - 7.5) * 24/7 + 32;
    elif second_unit_selected == temperature_units[2]: return (values - 7.5) * 40/21;
    elif second_unit_selected == temperature_units[3]: return (values - 7.5) * 32/21;
    elif second_unit_selected == temperature_units[4]: return (values - 7.5) * 24/7 + 491.67;
    elif second_unit_selected == temperature_units[5]: return (60 - values) * 20/7;
    elif second_unit_selected == temperature_units[6]: return (values - 7.5) * 22/35;
    else: return;

if __name__ == '__main__':
  show_list_of_units()
  temperature_converter_list()