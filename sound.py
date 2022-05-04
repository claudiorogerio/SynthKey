import numpy as np

# add notes if not added before
def add_notes( list, value ):
    for n in list:
        if n == value:  # ja esta na lista
            break
    list.append( value )
    return list

# convert midi to frequency
def midi_to_freq( midi, base=440 ):
  return base * np.power( 2, (midi-69)/12 )

# generate a sound array
def timbre_nota( timbre, midi, volume, base= 440, sr= 44100, dur=0.07 ):

    freq = midi_to_freq( midi, base )

    ts = 1/sr     # período de amostragem
    n1 = np.arange( sr*dur ) # domínio do tempo discreto, array

    if timbre == 'sawtooth':
        amplitudes = { 1: 2/1, 2: 2/2, 3: 2/3, 4: 2/4, 5: 2/5, 6: 2/6, 7: 2/7 }
    if timbre == 'square':
        amplitudes = { 1: 4/(np.pi), 3: 4/(3*np.pi), 5: 4/(5*np.pi), 7: 4/(7*np.pi), 9: 4/(9*np.pi) }
    if timbre == 'triangle':
        amplitudes = { 1: 4/(np.pi), 3: 4/(9*np.pi), 5: 4/(25*np.pi), 7: 4/(49*np.pi), 9: 4/(81*np.pi), 11: 4/(121*np.pi), 13: 4/(169*np.pi) }
    if timbre == 'flute':
        amplitudes = { 1.0: 1, 2.0: 1.869, 3.0: 0.042, 4.0: 0.022, 5.0: 0.009 }
    if timbre == 'trompa':
        amplitudes = { 1.0: 1, 2.0: 1.380, 3.0: 0.874, 4.0: 0.684, 5.0: 0.219 }
    if timbre == 'sino':
        amplitudes = { 1: 2/1 }

    amostra = 0
    for amp in amplitudes:
        print( "[",timbre,"]", amp, '\t', amplitudes[amp] )
        amostra += (2**-4)*6*volume*amplitudes[amp] * np.sin( amp * 2 * np.pi * freq *n1 * ts )   # onda senoidal, tempo, frequencia, espaço
#        amostra[1] += amplitudes[amp] * np.sin( amp * 2 * np.pi * freq *n1 * ts )   #

#    amostra = amostra * (2**8)
#    return np.dstack( (amostra, amostra))[0]
#    print( 'Amostra', amostra.shape )
#    return np.array( np.dstack( (amostra, amostra))[0], dtype="int16" )
#    print( type(amostra))
#    return np.array( amostra, dtype='int16' )
    return amostra.astype( 'int32' )
