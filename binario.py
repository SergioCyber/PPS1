def esBinario (strbinario):
    
    
    try:
        for dato in range(0, len(strbinario)):
            if strbinario[dato]!='1' and strbinario[dato]!='0':
                return False
        return True
    except TypeError:
        return False

    
def ext (bin):
    try:
        dec=0
        for dato in range(0, len(bin)):
            if bin[dato]=='1':
                dec=dec+pow(2, len(bin)-dato-1)
        return dec
    except TypeError:
        return False
    

pantalla=str(input("Escribe un número que sea binario:  "))


if esBinario(pantalla):
    print(f"{pantalla} es binario " + str(ext(pantalla)))
else:
    print(f"{pantalla} ¡No es un número binario!")
