# @brief:
# Piano visual:
# Program to manipulate notes and chords sound and MIDI in realtime
# @author: claudiorogerio 22.04.22
#
# TODO:
#       - Change timbre
#       - Chords Sound
#       - ADSR
#       - Midi file export
# MAKED:
#       - Chords midi
#       - Chords visual
#       - Midi
#       - Realtime Sound
#       - Touch button 1 - Sound
#       - Touch button 2 - Midi
#       - Touch button 3
#       - Touch button 4
#       - Visual informations
#       - Individual notes
#       - Octave changes
#       - Octave sounds
# HOTKEYS:
#       < 1 > On/Off Sound
#       < 2 > On/Off Midi
#       < 3 > On/Off Record midi
#       < 4 > On/Off Record sound
#       < 5 > On/Off Metronomo


import pygame, sys
import time
from colorama import Fore
import mido

debug = True
play_sound = False
play_midi = False

# Inicializacao pygame
pygame.mixer.pre_init( size=-16, channels=1, buffer=512 )
volume = 5000

pygame.init()
pygame.display.set_caption( "Visual piano")
icon = pygame.image.load( 'imgs/piano_icon.png' )
pygame.display.set_icon( icon )
# setup da superficie
display =[200, 500]
surface = pygame.display.set_mode( (display ) )
clock = pygame.time.Clock()

from visual import *
from sound import *

print( piano_0.get_width(), piano_0.get_height() )
delta = [30, 30]
pos_piano = int( delta[0]/2 ), int( delta[1]/2 ) # + 22
display_x = piano_0.get_width() + delta[0]
display_y = piano_0.get_height() + delta[1]

color1 = [0,0,0]
surface = pygame.display.set_mode( (display_x, display_y ) )
surface.fill( color1 )    # cor de fundo

font = pygame.font.get_default_font()
font_layer = pygame.font.Font( font, 12 )

font2 = pygame.font.SysFont('./fonts/joystix monospace.ttf', 20 )
font2 = pygame.font.SysFont('./fonts/monospace.medium.ttf', 20 )
#font_layer2 = pygame.font.Font( font, 12 )

text0 = ''
cifra = ''
notas = [ 'Dó', 'Dó sustenido', 'Ré', 'Ré sustenido', 'Mi', 'Fá', 'Fá sustenido', 'Sol', 'Sol sustenido', 'Lá', 'Lá sustenido', 'Si' ]
cifras = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
text_midi = 'OFF'
text_sound = 'OFF'
octave = 4      # midi 60
oct_idx = -1

count_color = 0     # contador visual
#press = [ -1, -1, -1, -1, -1 ]           # vetor de notas pressionadas
press = 0
pressed = [ -1, -1, -1, -1, -1, -1 ]
n_notes = -1

midi = 0
midis= []
sound = pygame.mixer.Sound( np.arange(1000) )

port = mido.open_output( 'Midi Through:Midi Through Port-0 14:0' )

touch_idx = [False, False, False, False, False, False]

running = 1
while running:

   # eventos de saida
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit(); sys.exit();
            running = 0
        elif event.type == pygame.KEYDOWN :
            if debug:
                print( Fore.BLUE + '[KEYDOWN] ', event.key, Fore.RESET )
            if event.key == pygame.K_ESCAPE :
                running = 0
            if event.key == pygame.K_1:
                touch_idx[0] = not touch_idx[0]
                play_sound = touch_idx[0]
                if play_sound:
                    text_sound = 'ON'
                else: text_sound = 'OFF'
                if debug: print( '1', touch_idx[0] )

            if event.key == pygame.K_2:
                touch_idx[1] = not touch_idx[1]
                play_midi = touch_idx[1]
                if play_midi:
                    text_midi = 'ON'
                else: text_midi = 'OFF'
                if debug: print( '2', touch_idx[1] )

            if event.key == pygame.K_3:
                touch_idx[2] = not touch_idx[2]
                if debug: print( '3', touch_idx[2] )

            if event.key == pygame.K_4:
                touch_idx[3] = not touch_idx[3]
                if debug: print( '4', touch_idx[3] )
            if event.key == pygame.K_DOWN:
                oct_idx = 0
                if debug: print( 'Octave', oct_idx )
            if event.key == pygame.K_UP:
                oct_idx = 1
                if debug: print( 'Octave', oct_idx )



    keys = pygame.key.get_pressed()

#        if event.type == pygame.KEYDOWN:
# NAO UTILIZADO
    if keys[pygame.K_LEFT]:
        x_change = -5
    elif keys[pygame.K_RIGHT]:
        x_change = 5
    elif keys[pygame.K_UP]:
        y_change = -5
    elif keys[pygame.K_DOWN]:
        y_change = 20



    if keys[ pygame.K_a ]:
        press = 0
        pressed = add_notes( pressed, press )
        text0 = cifras[ press%len(cifras) ] + str( octave )
        cifra = cifras[ press ]
        midi = press + (octave*12)
        midis.append( midi )
#        if debug:
 #           print( Fore.GREEN + cifra + Fore.BLACK )
    if keys[ pygame.K_w ]:
        press = 1
        pressed = add_notes( pressed, press )
        text0 = cifras[ press%len(cifras) ] + str( octave )
        cifra = cifras[ press ]
        midi = press + (octave*12)
        midis.append( midi )

    if keys[ pygame.K_s ]:
        press = 2
        pressed = add_notes( pressed, press )
        text0 = cifras[ press%len(cifras) ] + str( octave )
        cifra = cifras[ press ]
        midi = press + (octave*12)
        midis.append( midi )

    elif keys[ pygame.K_e ]:
        press = 3
        pressed = add_notes( pressed, press )
        text0 = cifras[ press%len(cifras) ] + str( octave )
        cifra = cifras[press]
        midi = press + (octave*12)
        midis.append( midi )

    elif keys[ pygame.K_d ]:
        #n_notes += 1
        press = 4
        pressed = add_notes( pressed, press )
        text0 = cifras[ press%len(cifras) ] + str( octave )
        cifra = cifras[press]
        midi = press + (octave*12)
        midis.append( midi )

    elif keys[ pygame.K_f ]:
        press = 5
        pressed = add_notes( pressed, press )
        text0 = cifras[ press%len(cifras) ] + str( octave )
        cifra = cifras[press]
        midi = press + (octave*12)
        midis.append( midi )

    elif keys[pygame.K_t]:
        press = 6
        pressed = add_notes( pressed, press )
        text0 = cifras[ press%len(cifras) ] + str( octave )
        cifra = cifras[press]
        midi = press + (octave*12)
        midis.append( midi )

    elif keys[pygame.K_g]:
        press = 7
        pressed = add_notes( pressed, press )
        text0 = cifras[ press%len(cifras) ] + str( octave )
        cifra = cifras[press]
        midi = press + (octave*12)
        midis.append( midi )
    elif keys[pygame.K_y]:
        press = 8
        pressed = add_notes( pressed, press )
        text0 = cifras[ press%len(cifras) ] + str( octave )
        cifra = cifras[press]
        midi = press + (octave*12)
        midis.append( midi )
    elif keys[pygame.K_h]:
        press = 9
        pressed = add_notes( pressed, press )
        text0 = cifras[ press%len(cifras) ] + str( octave )
        cifra = cifras[press]
        midi = press + (octave*12)
        midis.append( midi )
    elif keys[pygame.K_u]:
        press = 10
        pressed = add_notes( pressed, press )
        text0 = cifras[ press%len(cifras) ] + str( octave )
        cifra = cifras[press]
        midi = press + (octave*12)
        midis.append( midi )
    elif keys[pygame.K_j]:
        press = 11
        pressed = add_notes( pressed, press )
        text0 = cifras[ press%len(cifras) ] + str( octave )
        cifra = cifras[press]
        midi = press + (octave*12)
        midis.append( midi )
    elif keys[pygame.K_k]:
        press = 12
        pressed = add_notes( pressed, press )
        text0 = cifras[ press%len(cifras) ] + str( octave + 1 )
        cifra = cifras[ press%len(cifras) ]
        midi = press + (octave*12)
        midis.append( midi )
    elif keys[pygame.K_o]:
        press = 13
        pressed = add_notes( pressed, press )
        text0 = cifras[ press%len(cifras) ] + str( octave + 1 )
        cifra = cifras[ press%len(cifras) ]
        midi = press + (octave*12)
        midis.append( midi )
    elif keys[pygame.K_l]:
        press = 14
        pressed = add_notes( pressed, press )
        text0 = cifras[ press%len(cifras) ] + str( octave + 1 )
        cifra = cifras[ press%len(cifras) ]
        midi = press + (octave*12)
        midis.append( midi )
    elif keys[pygame.K_p]:
        press = 15
        pressed = add_notes( pressed, press )
        text0 = cifras[ press%len(cifras) ] + str( octave + 1 )
        cifra = cifras[ press%len(cifras) ]
        midi = press + (octave*12)
        midis.append( midi )
    elif keys[231]:
        press = 16
        pressed = add_notes( pressed, press )
        text0 = cifras[ press%len(cifras) ] + str( octave + 1 )
        cifra = cifras[ press%len(cifras) ]
        midi = press + (octave*12)
        midis.append( midi )

    if debug:
        if any( keys ):
            print( Fore.GREEN + 'Note touched:'+cifra + Fore.RESET )

    # special keyboard
    aux = 0
    for n in keys:
        if n and aux == 52:
            print( '[PRESSED]', n, aux )
            press = 17
            pressed = add_notes( pressed, press )
            text0 = cifras[ press%len(cifras) ] + str( octave + 1 )
            cifra = cifras[ press%len(cifras) ]
            midi = press + (octave*12)
            midis.append( midi )
        if n and aux == 47:
            print( '[PRESSED]', n, aux )
            press = 18
            pressed = add_notes( pressed, press )
            text0 = cifras[ press%len(cifras) ] + str( octave + 1 )
            cifra = cifras[ press%len(cifras) ]
            midi = press + (octave*12)
            midis.append( midi )
        if n and aux == 49:
            print( '[PRESSED]', n, aux )
            press = 19
            pressed = add_notes( pressed, press )
            text0 = cifras[ press%len(cifras) ] + str( octave + 1 )
            cifra = cifras[ press%len(cifras) ]
            midi = press + (octave*12)
            midis.append( midi )
        if n and aux == 48:
            print( '[PRESSED]', n, aux )
            press = 20
            pressed = add_notes( pressed, press )
            text0 = cifras[ press%len(cifras) ] + str( octave + 1 )
            cifra = cifras[ press%len(cifras) ]
            midi = press + (octave*12)
            midis.append( midi )
        #if n:
        #    print( aux, '...')
        aux += 1

    ## nao pressionando teclas
    if not any( keys ):
        text0 = ''
        count_color -= 10
        n_notes -= 1    # retirando uma nota por vez
        if count_color <=0:
            n_notes = -1
            if play_midi and midi > 0 :
                for md in midis:
                    print( "[MIDI OFF]", md )
                    msg = mido.Message( 'note_off', note= md, velocity = count_color%128 )
                    port.send( msg )
            count_color = 0
            press = 0
            midi = 0
            midis= []
            pressed = [-1, -1, -1, -1, -1, -1]
    else:
        count_color += 3
        if count_color >= 255 : count_color = 255

    # cor de fundo
    surface.fill( [ (press*30%255), count_color, (press*50%255) ] )

    surface.blit( piano_0, ( pos_piano ) )

    if midi > 0 :
#        surface.fill( [ press*20, count_color, press*20] )
        #surface.blit( pianos[ press+1 ], ( pos_piano ) )
        print( Fore.RED + "Pressionada:", press, cifra, Fore.RESET )
        #surface.blit( pianos[ press ], ( pos_piano ) )     # anterior

        for n in pressed:
            if n != -1:
                print( "Notas", n )
                surface.blit( pianos[ n ], ( pos_piano ) )

        if play_sound:
            amostra = timbre_nota( timbre= 'sawtooth', midi=midi, sr= 44100, volume= volume )
            sound = pygame.sndarray.make_sound( amostra )
            sound.play()
            if debug: print( '[Sound]', midi )

        if play_midi:
            for md in midis:
                msg = mido.Message( 'note_on', note= md, velocity = count_color%128 , time= 1 )
                port.send( msg )
                pygame.time.delay( 5 ) # delay necessary to send data
                if debug: print( '[MIDI ON] ', midi, 120 )

    else:
        pygame.mixer.Sound.stop( sound )


    # atualiza a nova posicao



#    if count_color >=1 :
 #       print( press, '.....')
  #      for n in range( n_notes+1 ):
   #         surface.blit( pianos[ press[n] ], ( pos_piano ) )


    font_surface = font_layer.render( 'Sound ' + text_sound, True, (90,90,90) )
    surface.blit( font_surface, ( 82, 45 ) ) # 45 55

    font_surface = font_layer.render( 'Midi ' + text_midi, True, (90,90,90) )
    surface.blit( font_surface, ( 82, 60 ) ) # 45 55

    if text0 != '':
        font_surface = font2.render( text0, True, (100,100,100) )
        surface.blit( font_surface, ( 82, 75 ) ) # 45 55

    # touch
    for i in range( len(touch_idx) ):
        if touch_idx[i]== True:
            surface.blit( touchs[i], ( pos_piano ) )

    # change octaves
    if oct_idx >= 0:
        surface.blit( change_octave[ oct_idx ], ( pos_piano ) )
        pygame.display.update()     # way to see button pressed
        pygame.time.delay( 300 )

        if oct_idx == 0 : octave -= 1
        else: octave += 1

        if octave >= 8 : octave = 8
        if octave <= 0 : octave = 0

        oct_idx = -1    # null value
        if debug: print( Fore.BLUE, 'Change octave:', octave, Fore.RESET )


    pygame.display.flip()
    pygame.display.update()

    clock.tick(20)
