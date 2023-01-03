

def tambah_aktivitas(name,datum,ktgr):
    global activity
    
    if name.lower() in [name_a.lower() for name_a in activity]:
        return 'Kegiatan sudah pernah diinput. Tidak boleh double claim!'
    else:
        activity[name] = [datum,ktgr,daftar_poin_kegiatan[ktgr]]
        return 'Kegiatan berhasil ditambahkan.'

activity = {}

daftar_poin_kegiatan = {
    'Prestasi':30,
    'Organisasi':10,
    'Kepanitiaan':5,
    'Rekognisi':2
}

belum_keluar = True

while belum_keluar:
    print('******* Kredit Keaktifan Mahasiswa ******\n(Student Activities Credit)')

    cho = ['Menambahkan Kegiatan', 'Menampilkan Jumlah Poin', 'Keluar']

    for i, choice in enumerate(cho,start=1):
        print(f'{i}. {choice}')

    print('-'*30)


    pil = cho[int(input('Silahkan Masukan Pilihan Anda: '))-1]

    if pil == cho[0]:
        nama_aktivitas = input('Nama Kegiatan: ')
        tanggal_aktivitas = input('Tanggal Kegiatan: ')
        print('Pilihan Kategori Kegiatan:')
        for poin in daftar_poin_kegiatan:
            print(f' - {poin}')
        kategori_kegiatan = input('Masukan Kategori Kegiatan: ').title()
        print('')
        print(tambah_aktivitas(nama_aktivitas,tanggal_aktivitas,kategori_kegiatan))
        print('')
    elif pil == cho[1]:
        print('')
        print('-'*30,end='')
        print('Nama Kegiatan\tTanggal\tKategori\tPoin')
        total_poin = 0
        for i, kegiatan_terdaftar in enumerate(activity,start=1):
            print(f'{i}. {kegiatan_terdaftar}',end='\t')
            print(*activity[kegiatan_terdaftar],sep='\t')
            total_poin += activity[kegiatan_terdaftar][-1]
        print(f'JUMLAH TOTAL POIN\t: {total_poin}')
        print('')
    else:
        print('Sistem Berhenti...')
        belum_keluar = False