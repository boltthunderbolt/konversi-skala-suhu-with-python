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


# # Validasi input
# if skala_yang_dipilih < 0 or skala_yang_dipilih >= len(list_satuan_skala) or skala_yang_ingin_dikonversi < 0 or skala_yang_ingin_dikonversi >= len(list_satuan_skala):
#   #! Jika skala_yang_dipilih dan skala_yang_dikonversi tidak ada dalam daftar list_satuan_skala maka error ditampilkan
#   raise ValueError('Satuan skala yang dimasukkan tidak valid. Harap masukkan dengan benar');

# # Function konversi skala suhu

# #* Hasil Konversi di proses kedalam variabel hasil_konversi
# hasil_konversi = konversi_skala_suhu(list_satuan_skala[skala_yang_dipilih], nilai_suhu, list_satuan_skala[skala_yang_ingin_dikonversi]);

# # Menampilkan hasil
# #! Akan memvalidasi, jika input nama skala bernilai sama
# if skala_yang_dipilih == skala_yang_ingin_dikonversi :
#   raise ValueError("Konversi tidak akan berlaku jika kedua nama skala suhu sama");
# else:
#   print(f"\nHasil konversi dari {nilai_suhu} {list_satuan_skala[skala_yang_dipilih]} ke {list_satuan_skala[skala_yang_ingin_dikonversi]} adalah {hasil_konversi}\n\n\n");

if __name__ == '__main__':
  main()