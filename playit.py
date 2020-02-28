from track import *
# from short import *

# the package that does the key input reading
import pygame as pg

## correspondence of the keys to the audio files
# my sounds
soundfolder = 'sounds/'
# techno folder from MusicRadar
tfolder = 'musicradar-techno-120bpm/'
# sounds played at press
SOUNDS = {
    pg.K_a: 'kurz_crop.wav', pg.K_s:'kurz1.wav', pg.K_d: 'meeewKurz.wav', pg.K_f:'ewew.wav',
    pg.K_g:'meeeew.wav', pg.K_h: 'mozart.wav', pg.K_j: 'mewmew.wav',
    pg.K_k:'yeah.wav', pg.K_l: 'woof.wav',  pg.K_p:'whaaat.wav',

    pg.K_m: 'Drum_Hits_C_a/TechDHitCa-02_louder.wav',
    pg.K_n: 'Drum_Hits_C_a/TechDHitCa-06_louder.wav'
}

# sounds played continuously and stopped/started as key is pressed
LOOP_SOUNDS = {
    pg.K_z: 'Beats_C_a/TechBeatC120a-01.wav',
    pg.K_x: 'Bassline_R/TechBassR120E-01.wav',
    # pg.K_z: 'Bassline_U/TechBassU120G-03.wav',

    pg.K_c: 'Synths/TechSynthM120E-01.wav',
    # pg.K_x: 'Synths/TechSynthN120C-01.wav',
}
LOOP_MEMORY = {}

# how is there no built in method for the key to tell its string name???
# explanatory initial message
KEYS = {
'Short (NO NO cat)': ['a', 's', 'd', 'f', 'g', 'h', 'j'],
'Short (other)': ['k', 'l', 'p'],
'Short (techno)': ['m', 'n'],
'Continuous (techno)': ['z', 'x']
}

######################################3


# main function
def piano():
    '''
    Awesome docstring
    '''
    # initial message
    print('\nAvailable keys:\n')
    for key in KEYS:
        print(key + ' : ' + ', '.join(KEYS[key]))
    print('\nTo quit press q\n')

    # this creates a window (necessary)
    # that will respond to the keys and do everything
    pg.init()

    # image not to have a boring black window
    img = pg.image.load('nononocatSmall.jpg')
    white = (255, 64, 64)
    screen = pg.display.set_mode((200, 200))
    screen.fill((white))

    # technical trick for later
    # playing silence first to create this "pl" object
    pl = play_wav(soundfolder + 'silence.wav')

    # it keeps running with some sort of 25 frames per second rate or sth
    running = True
    while running:

        # put the image to the screen
        screen.blit(img,(0,0))
        pg.display.flip()

        # check if anything is happening all the time
        for event in pg.event.get():
            # if key is pressed
            if event.type == pg.KEYDOWN:
                # if a key corresponds to a sound to play once
                if event.key in SOUNDS:
                    # print random cat message
#                    print(random.choice(NO))
                    # stop the previous sound
                    pl.stop()
                    # play the sound
                    folder = tfolder if '/' in  SOUNDS[event.key] else soundfolder
                    pl = play_wav(folder + SOUNDS[event.key])

                # if a key corresponds to a loop sound
                elif event.key in LOOP_SOUNDS:
                    # if it's the first time the key is pressed, add the sound
                    if not event.key in LOOP_MEMORY:
                        LOOP_MEMORY[event.key] = Track(tfolder + LOOP_SOUNDS[event.key])
                        LOOP_MEMORY[event.key].start()
                    else:
                        LOOP_MEMORY[event.key].stop()
                        del LOOP_MEMORY[event.key]


                # quit button
                elif event.key == pg.K_q:
                    print('Quitting...')
                    running = False

    for ob in LOOP_MEMORY:
        LOOP_MEMORY[ob].stop()

    pg.quit()


if __name__ == '__main__':
    piano()
