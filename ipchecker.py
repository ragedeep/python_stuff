#validate ip
firstoct = input('Firstoctet: ')
secondoct = input('Secondoctet: ')
thirdoct = input('thirdoctet: ')
fourthoct = input('fourthoctet: ')
ipaddress = firstoct + "." + secondoct + "." + thirdoct + "." + fourthoct
if firstoct != (10) or (172) or (192):
    print( 'invalid ip address')
    if firstoct == (10):
        print ('valid class A ip address')
    if firstoct == (172):
        print( 'valid class b network')
    if firstoct == (192):
        print ('valid class c network')

