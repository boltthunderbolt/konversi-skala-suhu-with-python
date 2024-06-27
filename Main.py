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



# Function konversi
def konversi_skala_suhu(skala_yang_dipilih, nilai_suhu, skala_yang_ingin_dikonversi):
  # * Mencari nilai konversi dari satuan Celcius
  if skala_yang_dipilih == 'celcius':
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
    elif skala_yang_ingin_dikonversi == 'romer':
      return nilai_suhu * 21/40 + 7.5;
    else:
      #! Jika salah memasukkan satuan skala suhu
      raise ValueError('Masukkan satuan sesuai dengan yang sudah tertera!');

# Hasil Konversi di proses kedalam variabel hasil_konversi
hasil_konversi = konversi_skala_suhu(skala_yang_dipilih, nilai_suhu, skala_yang_ingin_dikonversi);

# Menampilkan hasil
print(f"Hasil konversi dari {nilai_suhu} {skala_yang_dipilih} ke {skala_yang_ingin_dikonversi} adalah {hasil_konversi}");