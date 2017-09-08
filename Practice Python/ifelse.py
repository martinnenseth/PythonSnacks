antall_deltakere=float(input('skriv inn hvor mange dere skal være: '))
leie=2500
leie_per=420
if antall_deltakere > 10 and antall_deltakere < 20:
    print(antall_deltakere)
    print("hei på deg")
    leie_per=380

elif antall_deltakere >= 20:
        print("hei")
        leie_per=350

totalpris=(antall_deltakere*leie_per)+leie

print('din totalpris kommer på',format (totalpris, '.2f'))
