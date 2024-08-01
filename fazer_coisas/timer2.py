import time as relogio

agr = relogio.gmtime()
formatando = relogio.strftime('%DD%MM%AA',agr)

print(formatando)