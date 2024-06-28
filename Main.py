# Python
## Konversi segala jenis skala suhu
#* Sumber : Wikipedia
'''
  - Kelvin     - Fahrenheit     - Celcius      - Reamur
  - Rankine    - Delisle        - Newton       - Romer
'''


# Input user melalu terminal
skala_yang_dipilih = input("Masukkan skala awal (kelvin/fahrenheit/celcius/reamur/rankine/delisle/newton/romer):   ->   ").lower();
nilai_suhu = float(input("Masukkan nilainya   ->   "));
skala_yang_ingin_dikonversi = input("Masukkan skala yang ingin dikonversi (kelvin/fahrenheit/celcius/reamur/rankine/delisle/newton/romer):   ->   ").lower();



# Function konversi skala suhu
def konversi_skala_suhu(skala_yang_dipilih, nilai_suhu, skala_yang_ingin_dikonversi):
  # * Mencari nilai konversi dari satuan Kelvin
  if skala_yang_dipilih == 'kelvin':
    if skala_yang_ingin_dikonversi == 'kelvin':
      return nilai_suhu;
    elif skala_yang_ingin_dikonversi == 'fahrenheit':
      return nilai_suhu * 9/5 - 459.67;
    elif skala_yang_ingin_dikonversi == 'celcius':
      return nilai_suhu - 273.15;
    elif skala_yang_ingin_dikonversi == 'reamur':
      return (nilai_suhu - 273.15) * 4/5;
    elif skala_yang_ingin_dikonversi == 'rankine':
      return nilai_suhu * 9/5;
    elif skala_yang_ingin_dikonversi == 'delisle':
      return (373.15 - nilai_suhu) * 3/2;
    elif skala_yang_ingin_dikonversi == 'newton':
      return (nilai_suhu - 273.15) * 33/100;
    elif skala_yang_ingin_dikonversi == 'romer':
      return (nilai_suhu - 273.15) * 21/40 + 7.5;
    else:
      #! Jika salah memasukkan satuan skala suhu
      raise ValueError('Masukkan satuan sesuai dengan yang sudah tertera!');

  # * Mencari nilai konversi dari satuan Fahrenheit
  elif skala_yang_dipilih == 'fahrenheit':
    if skala_yang_ingin_dikonversi == 'kelvin':
      return (nilai_suhu + 459.67) * 5/9;
    elif skala_yang_ingin_dikonversi == 'fahrenheit':
      return nilai_suhu;
    elif skala_yang_ingin_dikonversi == 'celcius':
      return (nilai_suhu - 32) * 5/9;
    elif skala_yang_ingin_dikonversi == 'reamur':
      return (nilai_suhu - 32) * 4/9;
    elif skala_yang_ingin_dikonversi == 'rankine':
      return nilai_suhu + 459.67;
    elif skala_yang_ingin_dikonversi == 'delisle':
      return (212 - nilai_suhu) * 5/6;
    elif skala_yang_ingin_dikonversi == 'newton':
      return (nilai_suhu - 32) * 11/80;
    elif skala_yang_ingin_dikonversi == 'romer':
      return (nilai_suhu - 32) * 7/24 + 7.5;
    else:
      #! Jika salah memasukkan satuan skala suhu
      raise ValueError('Masukkan satuan sesuai dengan yang sudah tertera!');

  # * Mencari nilai konversi dari satuan Celcius
  elif skala_yang_dipilih == 'celcius':
    if skala_yang_ingin_dikonversi == 'kelvin':
      return nilai_suhu + 273.15;
    elif skala_yang_ingin_dikonversi == 'fahrenheit':
      return nilai_suhu * 9/5 + 32;
    elif skala_yang_ingin_dikonversi == 'celcius':
      return nilai_suhu;
    elif skala_yang_ingin_dikonversi == 'reamur':
      return nilai_suhu * 4/5;
    elif skala_yang_ingin_dikonversi == 'rankine':
      return (nilai_suhu + 273.15) * 9/5;
    elif skala_yang_ingin_dikonversi == 'delisle':
      return (100 - nilai_suhu) * 3/2;
    elif skala_yang_ingin_dikonversi == 'newton':
      return nilai_suhu * 33/100;
    elif skala_yang_ingin_dikonversi == 'romer':
      return nilai_suhu * 21/40 + 7.5;
    else:
      #! Jika salah memasukkan satuan skala suhu
      raise ValueError('Masukkan satuan sesuai dengan yang sudah tertera!');

  # * Mencari nilai konversi dari satuan Reamur
  elif skala_yang_dipilih == 'reamur':
    if skala_yang_ingin_dikonversi == 'kelvin':
      return nilai_suhu * 5/4 + 273.15;
    elif skala_yang_ingin_dikonversi == 'fahrenheit':
      return nilai_suhu * 9/4 + 32;
    elif skala_yang_ingin_dikonversi == 'celcius':
      return nilai_suhu * 5/4;
    elif skala_yang_ingin_dikonversi == 'reamur':
      return nilai_suhu;
    elif skala_yang_ingin_dikonversi == 'rankine':
      return nilai_suhu * 9/4 + 491.67;
    elif skala_yang_ingin_dikonversi == 'delisle':
      return (80 - nilai_suhu) * 15/8;
    elif skala_yang_ingin_dikonversi == 'newton':
      return nilai_suhu * 33/80;
    elif skala_yang_ingin_dikonversi == 'romer':
      return nilai_suhu * 21/32 + 7.5;
    else:
      #! Jika salah memasukkan satuan skala suhu
      raise ValueError('Masukkan satuan sesuai dengan yang sudah tertera!');
      
  # * Mencari nilai konversi dari satuan Rankine
  elif skala_yang_dipilih == 'rankine':
    if skala_yang_ingin_dikonversi == 'kelvin':
      return nilai_suhu * 5/9;
    elif skala_yang_ingin_dikonversi == 'fahrenheit':
      return nilai_suhu - 459.67;
    elif skala_yang_ingin_dikonversi == 'celcius':
      return (nilai_suhu - 491.67) * 5/9;
    elif skala_yang_ingin_dikonversi == 'reamur':
      return (nilai_suhu - 491.67) * 4/9;
    elif skala_yang_ingin_dikonversi == 'rankine':
      return nilai_suhu;
    elif skala_yang_ingin_dikonversi == 'delisle':
      return (671.67 - nilai_suhu) * 5/6;
    elif skala_yang_ingin_dikonversi == 'newton':
      return (nilai_suhu - 491.67) * 11/80;
    elif skala_yang_ingin_dikonversi == 'romer':
      return (nilai_suhu - 491.67) * 7/24 + 7.5;
    else:
      #! Jika salah memasukkan satuan skala suhu
      raise ValueError('Masukkan satuan sesuai dengan yang sudah tertera!');
  
  # * Mencari nilai konversi dari satuan Delisle
  elif skala_yang_dipilih == 'delisle':
    if skala_yang_ingin_dikonversi == 'kelvin':
      return 373.15 - nilai_suhu * 2/3;
    elif skala_yang_ingin_dikonversi == 'fahrenheit':
      return 212 - nilai_suhu * 6/5;
    elif skala_yang_ingin_dikonversi == 'celcius':
      return 100 - nilai_suhu * 2/3;
    elif skala_yang_ingin_dikonversi == 'reamur':
      return 80 - nilai_suhu * 8/15;
    elif skala_yang_ingin_dikonversi == 'rankine':
      return 671.67 - nilai_suhu * 6/5;
    elif skala_yang_ingin_dikonversi == 'delisle':
      return nilai_suhu;
    elif skala_yang_ingin_dikonversi == 'newton':
      return 33 - nilai_suhu * 11/50;
    elif skala_yang_ingin_dikonversi == 'romer':
      return 60 - nilai_suhu * 7/20;
    else:
      #! Jika salah memasukkan satuan skala suhu
      raise ValueError('Masukkan satuan sesuai dengan yang sudah tertera!');

  # * Mencari nilai konversi dari satuan Newton
  elif skala_yang_dipilih == 'newton':
    if skala_yang_ingin_dikonversi == 'kelvin':
      return nilai_suhu * 100/33 + 273.15;
    elif skala_yang_ingin_dikonversi == 'fahrenheit':
      return nilai_suhu * 60/11 + 32;
    elif skala_yang_ingin_dikonversi == 'celcius':
      return nilai_suhu * 100/33;
    elif skala_yang_ingin_dikonversi == 'reamur':
      return nilai_suhu * 80/33;
    elif skala_yang_ingin_dikonversi == 'rankine':
      return nilai_suhu * 60/11 + 491.67;
    elif skala_yang_ingin_dikonversi == 'delisle':
      return (33 - nilai_suhu) * 50/11;
    elif skala_yang_ingin_dikonversi == 'newton':
      return nilai_suhu;
    elif skala_yang_ingin_dikonversi == 'romer':
      return nilai_suhu * 35/22 + 7.5;
    else:
      #! Jika salah memasukkan satuan skala suhu
      raise ValueError('Masukkan satuan sesuai dengan yang sudah tertera!');

# * Mencari nilai konversi dari satuan Romer
  elif skala_yang_dipilih == 'romer':
    if skala_yang_ingin_dikonversi == 'kelvin':
      return (nilai_suhu - 7.5) * 40/21 + 273.15;
    elif skala_yang_ingin_dikonversi == 'fahrenheit':
      return (nilai_suhu - 7.5) * 24/7 + 32;
    elif skala_yang_ingin_dikonversi == 'celcius':
      return (nilai_suhu - 7.5) * 40/21;
    elif skala_yang_ingin_dikonversi == 'reamur':
      return (nilai_suhu - 7.5) * 32/21;
    elif skala_yang_ingin_dikonversi == 'rankine':
      return (nilai_suhu - 7.5) * 24/7 + 491.67;
    elif skala_yang_ingin_dikonversi == 'delisle':
      return (60 - nilai_suhu) * 20/7;
    elif skala_yang_ingin_dikonversi == 'newton':
      return (nilai_suhu - 7.5) * 22/35;
    elif skala_yang_ingin_dikonversi == 'romer':
      return nilai_suhu;
    else:
      #! Jika salah memasukkan satuan skala suhu
      raise ValueError('Masukkan satuan sesuai dengan yang sudah tertera!');

# Hasil Konversi di proses kedalam variabel hasil_konversi
hasil_konversi = konversi_skala_suhu(skala_yang_dipilih, nilai_suhu, skala_yang_ingin_dikonversi);

# Menampilkan hasil
print(f"Hasil konversi dari {nilai_suhu} {skala_yang_dipilih} ke {skala_yang_ingin_dikonversi} adalah {hasil_konversi}");