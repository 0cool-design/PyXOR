import sys, os, time

if sys.version_info[0] < 3:
	print(
		"(!) Please run the tool using Python 3")
	sys.exit()

os.system("clear")
print ("""
                                                   `-.`
                                              `-/+syhhyo+:.`
                                         `-/+syhhdmmmmmddhhyo+:.`
                                     -/+syhhdmmmh       sdmmddhhyo+:.
                                    `yhdmmmmmm   sddhhdho ommmmmmddyo
                                    `ydmmmmmmd  dhy+:/oyhd mmmmmmmmyo
                                     shmmmmmm  dhy/ O  oydo mmmmmmmy/
                                     ohmmmmmm  odys:../yyO  mmmmmmmy:
                                     :ymmmmmmm  +dhyyyhdh- mmmmmmds`
                                      `sdmmmmmmm          mmmmmmmmh+
                                      /ymmmmmmmmmmmy mmmmmmmmmmmmds.
                                       ohmmmmmmmmmmy    mmmmmmmmdy:
      _____                            `sdmmmmmmmmmy mmmmmmmmmmmh+ ________________
     / / _ \ _ __ ___   __ _ _ __       .shmmmmmmmmy     mmmmmdh+ / ___|| ____/ ___|
    / / | | | '_ ` _ \ / _` | '_ \       `ohdmmmmmmy dmmmmmmmdy/  \___ \|  _|| |
   / /| |_| | | | | | | (_| | | | |        /ydmmmmmy   mmmmdhs-    ___) | |__| |___
(_)_/  \___/|_| |_| |_|\__,_|_| |_|        .+ydmmmdyyhmmdhy:      |____/|_____\____|
                                              .+yhdmmmmdhs:`
                                                `/shddyo-
                                                   -+/.

""")

time.sleep(2)
with open(sys.argv[1], 'rb') as f1, open(sys.argv[2], 'rb') as f2:
    one, two = f1.read(), f2.read()

if one.endswith(b'\n'):
    one = one[:-1]

print()

for i, val in enumerate(one):
    print(  repr(chr(one[i])) +'  = '+ format(one[i], '#010b') )
    print(  repr(chr(two[i])) +'  = '+ format(two[i], '#010b') )
    print('--------------------------')
    print( 'xor  = ' + format( (one[i] ^ two[i]), '#010b' ) + ' = ' + repr(chr( one[i] ^ two[i] )) +'\n')
