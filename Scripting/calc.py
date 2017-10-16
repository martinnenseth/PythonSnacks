kalkulator = int(input('Ønsker du å se om du kan låne en bestemt sum? tast "1",\
Ønsker du å se hvor mye du kan låne tast  "2":'))

if kalkulator == 1:  # input for kalkulator 1
    print('Du har nå kommet til kalkulator 1')
    print('-------------------------------------------')
    print()
    Bolig_pris = int(input('Hvor mye ønsker du å låne? :'))
    EK = int(input('Hva er din egenkapital? :'))
    Barn = 0
    laanefaktor = 0  # laanefaktor og barn får en verdi

    EK_betingelse = (EK / Bolig_pris) * 100  # beregner om EK er bra nok

    if EK_betingelse >= 15:  # Før koden går videre på denne IFen, så sjekkes det med betingelsen om egenkapitalen er høy nok for et lån.
        forhold = int(input('Er du singel? tast "2",har du Samboer tast "1": '))
        brutto = int(input('Hvor mye tjener du/dere Brutto? :'))
        antall_barn = int(input('Hvor mange barn har du/dere vis ingen skriv 0'))

        if forhold == 1:
            Barn = 365000
            if brutto < 450000:
                print('dere fyller desverre ikke kravet om 450.000kr i brutto')
            else:
                if brutto >= 450000 and brutto < 650000:
                    laanefaktor = 3.0
                elif brutto >= 650000 and brutto < 900000:
                    laanefaktor = 4.25
                elif brutto >= 900000 and brutto < 1000000:
                    laanefaktor = 5.0
                elif brutto >= 1000000 and brutto < 1200000:
                    laanefaktor = 5.5
                else:
                    laanefaktor = 5.75

        faktor_barn = Barn * antall_barn
        Okonomi = (brutto * laanefaktor) - faktor_barn

        if Okonomi >= Bolig_pris:
            print('Du får invilget lån for din bolig for kjøp av din bolig')
            print('Din brutto"', brutto, 'kr" og din egenkapital"', EK, 'kr" er nok for', Bolig_pris, 'kr')
        elif Okonomi < Bolig_pris:
            print('Din Brutto er desverre ikke tilstrekkelig for lån på:', Bolig_pris, 'kr')
            print('Grunnlaget for det er regnet ut ifra antall barn"', Barn, '"brutto', brutto, 'kr')