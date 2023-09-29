import subprocess


dosya_yolu = "c:\\baffle.z3"  # Açmak istediğiniz dosyanın yolu

try:
    subprocess.Popen(["D:\Program Files\ZWSOFT\ZW3D 2023\zw3d.exe", dosya_yolu])
except FileNotFoundError:
    print(f"{dosya_yolu} dosyası bulunamadı.")
except Exception as e:
    print(f"Dosya açılırken bir hata oluştu: {str(e)}")
