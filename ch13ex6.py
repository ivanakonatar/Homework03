def cifre_broja_na_engleskom(x):

    sve_cifre = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']

    if x < 10:          # ako je unijet jednocifren broj vratice tu cifru rijecima odmah
        return sve_cifre[x]

    else:
        return cifre_broja_na_engleskom(x//10) + " " + sve_cifre[x % 10]

x = abs(int(input("Unesi cijeli broj: ")))
print("Cifre datog broja na engleskom su: ", cifre_broja_na_engleskom(x))


