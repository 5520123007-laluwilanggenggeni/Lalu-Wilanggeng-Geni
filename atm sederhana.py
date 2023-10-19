while True:
    print('==================================')
    print('SELAMAT DATANG DI ATM BRI SYARIAH')
    print('==================================')
    pin = int(input('masukkan PIN anda:'))
    if pin == 123:
        saldo = 500000
        sisa = saldo
        while True:
                print('================MENU==============')
                print('1.Tarik tunai')
                print('2.Cek saldo')
                print('3.Stor tunai')
                print('4.Exit')
                print('==================================')
                menu = input('pilih menu yang anda inginkan:')
                print('==================================')
                if menu == '1':
                    print('anda memilih menu tarik tunai')
                    jumlah_penarikan = int(input('masukkan jumlah penarikan: '))
                    sisa = saldo - jumlah_penarikan
                    if saldo >= 50000 and sisa >= 50000:
                        saldo = sisa
                        print('jumlah_penarikan: ',jumlah_penarikan)
                        print('sisa saldo: ', sisa)
                    elif sisa <= 50000:
                        print('maaf penarikan tidak bisa dilakukan')
                    else:
                        print('maaf saldo anda kurang untuk melakukan penarikan')
                elif menu == '2':
                    print('anda memilih menu cek saldo')
                    print('saldo:', saldo)
                elif menu == '3':
                    stor = int(input('masukkan jumlah yang ingin di stor:'))
                    saldo = saldo + stor
                    print('saldo:', saldo)
                elif menu == '4':
                    print('terima kasih telah berlangganan bersama kami')
                    break
    else:
        print('mohon maaf PIN anda salah')
        idf = 'apakah anda ingin coba lagi y/n:'
        if idf == 'y':
            continue
        elif idf == 'n':
            break