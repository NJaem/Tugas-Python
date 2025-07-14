def cetak_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")
        
cetak_info(nama="Dedes", umur=21, hobi="Membaca")