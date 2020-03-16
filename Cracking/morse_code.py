
def alphabets(keys):
    #dict alphas
    alphas = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.',
              'G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..',
              'M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.',
              'S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
              'Y':'-.--','Z':'--..',' ':'*'}
    return alphas[keys] 
def codes():
    alphas = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.',
              'G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..',
              'M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.',
              'S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
              'Y':'-.--','Z':'--..'}
    return alphas
def Encrypt(sentences):
    SENTS = sentences.upper()
    words = SENTS.split(' ')
    for word in words:
        for w in word:
            alphas = alphabets(w)
            print(alphas,end=' ')

def Decrypt(gibberish):
    w = []
    gib = gibberish.split(' ')
    for g in gib:
        for k,v in codes().items():
            if(g == v):
                w.append(k)
    print(''.join([ele for ele in w]))
            

entry = input('Do you want to Encrypt press 0 or to Decrypt press 1 : \n')
if(entry == '0'):
    rerun = 'y'
    while(rerun=='y'):
        message = input('Enter the message: ')
        Encrypt(message)
        rerun = input('Do you want to continue? [y/n] ')
elif(entry == '1'):
    rerun = 'y'
    while(rerun=='y'):
        message = input('Enter your giberish: ')
        Decrypt(message)
        rerun = input('Do you want to continue? [y/n] ')
else:
    print('Please enter a valid key')
    exit()
