import pygame

folder = 'imgs/'
folder = 'imgs/piano_03/'
porcent = 0.40
version= '03'

piano = pygame.image.load( folder + 'piano_base_03.png').convert_alpha()
piano_0 = pygame.transform.rotozoom( piano, 0, porcent )

cifras_img = ['C', 'CS', 'D', 'DS', 'E', 'F', 'FS', 'G', 'GS', 'A', 'AS', 'B' ]
pianos = []
for n in range( 3 ):
    count = 0
    for cif in cifras_img :

        if n == 2 and count > 2 : break # ultima oitava até D2

        file_aux = 'piano_' + cif + str(n) + "_" + version + '.png'
        print( "[Visual] Add images:", file_aux )
        piano_cifra_ = pygame.image.load( folder + file_aux ).convert_alpha()
        piano_cifra  = pygame.transform.rotozoom( piano_cifra_, 0, porcent )
        pianos.append( piano_cifra )
        count += 1

touchs = []
for n in range(1,5):
    file_aux = 'piano_touch_'+ str(n).zfill(2)+'.png'
    print( "[Visual] Add touch buttons:", file_aux )
    touch_bt_ = pygame.image.load( folder + file_aux ).convert_alpha()
    touch_bt  = pygame.transform.rotozoom( touch_bt_ , 0, porcent )
    touchs.append( touch_bt )

oct_up_ = pygame.image.load( folder + 'piano_oct_up.png' ).convert_alpha()
oct_up  = pygame.transform.rotozoom( oct_up_, 0, porcent )
oct_down_ = pygame.image.load( folder + 'piano_oct_down.png' ).convert_alpha()
oct_down  = pygame.transform.rotozoom( oct_down_, 0, porcent )
change_octave = [ oct_down, oct_up ]

#piano_c0_ = pygame.image.load( folder + 'piano_C0_03.png' ).convert_alpha()
#piano_C0 = pygame.transform.rotozoom( piano_c0_, 0, porcent )
#piano_C0.set_alpha(200)

#piano_cs0_ = pygame.image.load( folder + 'piano_CS0_03.png' ).convert_alpha()
#piano_CS0 = pygame.transform.rotozoom( piano_cs0_, 0, porcent )

#piano_d0_ = pygame.image.load( folder + 'piano_D0_03.png' ).convert_alpha()
#piano_D0 = pygame.transform.rotozoom( piano_d0_, 0, porcent )

#piano_ds0_ = pygame.image.load( folder + 'piano_DS0_03.png' ).convert_alpha()
#piano_DS0 = pygame.transform.rotozoom( piano_ds0_, 0, porcent )

#piano_e0_ = pygame.image.load( folder + 'piano_E0_03.png' ).convert_alpha()
#piano_E0 = pygame.transform.rotozoom( piano_e0_, 0, porcent )

#piano_f0_ = pygame.image.load( folder + 'piano_F0_03.png' ).convert_alpha()
#piano_F0 = pygame.transform.rotozoom( piano_f0_, 0, porcent )

#piano_fs0_ = pygame.image.load( folder + 'piano_FS0_03.png' ).convert_alpha()
#piano_FS0 = pygame.transform.rotozoom( piano_fs0_, 0, porcent )

#piano_g0_ = pygame.image.load( folder + 'piano_G0_03.png' ).convert_alpha()
#piano_G0 = pygame.transform.rotozoom( piano_g0_, 0, porcent )

#piano_gs0_ = pygame.image.load( folder + 'piano_GS0_03.png' ).convert_alpha()
#piano_GS0 = pygame.transform.rotozoom( piano_gs0_, 0, porcent )

#piano_a0_ = pygame.image.load( folder + 'piano_A0_03.png' ).convert_alpha()
#piano_A0 = pygame.transform.rotozoom( piano_a0_, 0, porcent )

#piano_as0_ = pygame.image.load( folder + 'piano_AS0_03.png' ).convert_alpha()
#piano_AS0 = pygame.transform.rotozoom( piano_as0_, 0, porcent )

#piano_b0_ = pygame.image.load( folder + 'piano_B0_03.png' ).convert_alpha()
#piano_B0 = pygame.transform.rotozoom( piano_b0_, 0, porcent )

#piano_c1_ = pygame.image.load( folder + 'piano_C1_03.png' ).convert_alpha()
#piano_C1 = pygame.transform.rotozoom( piano_c1_, 0, porcent )

#pianos = [ piano_C0, piano_CS0, piano_D0, piano_DS0, piano_E0, piano_F0, piano_FS0, piano_G0, piano_GS0, piano_A0, piano_AS0, piano_B0, piano_C1 ]

#touch_01_ = pygame.image.load( folder + 'piano_touch_01.png' ).convert_alpha()
#touch_01 = pygame.transform.rotozoom( touch_01_, 0, porcent )
#touch_02_ = pygame.image.load( folder + 'piano_touch_02.png' ).convert_alpha()
#touch_02 = pygame.transform.rotozoom( touch_02_, 0, porcent )
#touch_03_ = pygame.image.load( folder + 'piano_touch_03.png' ).convert_alpha()
#touch_03 = pygame.transform.rotozoom( touch_03_, 0, porcent )
#touch_04_ = pygame.image.load( folder + 'piano_touch_04.png' ).convert_alpha()
#touch_04 = pygame.transform.rotozoom( touch_04_, 0, porcent )
#touchs = [ touch_01, touch_02, touch_03, touch_04 ]
