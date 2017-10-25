# Torso Ninja - scrolling shooter video game
# Copyright (C) 2015-2017 Erik Letson <hmagellan@tutamail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame, os, math, ConfigParser

pygame.init()

######################
## GLOBAL VARIABLES ##
######################
INITIAL_SCROLLER_Y = -600#for scrollers
SCROLLER_LIMIT_Y = 600

#######################
## ENVIRONMENT CALLS ##
#######################

#########################
## SHEETS & ANIMATIONS ##
#########################

#sheets is in the form:
#   SHEETS = {
#       'image_filename':[(spritewidth, spriteheight), num_sprites],
#       ...
#   }
SHEETS = {
    'tn.png':[(16, 24), 8],
    'woodstest1.png':[(800, 600), 1],
    'woodstest2.png':[(800, 600), 1],
    'grass1.png':[(800, 600), 1],
    'tatami1.png':[(800, 600), 1],
    'bul.png':[(12, 12), 1],
    'shuriken1.png':[(18, 18), 6],
    'life_thumbnail.png':[(12, 12), 2],
    'bomb_thumbnail.png':[(12, 12), 2],
    'ninja_particle.png':[(8, 8), 1],
    'smoke.png':[(64, 64), 4],
    'start.png':[(180, 80), 2],
    'menu.png':[(160, 80), 2],
    'instructions.png':[(380, 80), 2],
    'sasuke.png':[(16, 24), 4],
    'goemon_closed.png':[(16, 24), 4],
    'goemon_open.png':[(16, 24), 4],
    'goemon_armless_closed.png':[(16, 24), 4],
    'goemon_armless_open.png':[(16, 24), 4],
    'arm.png':[(27, 27), 6],
    'bomb.png':[(24, 24), 1],
    '1up.png':[(16, 16), 1],
    '1times_score.png':[(16, 16), 1],
    '3times_score.png':[(16, 16), 1],
    'finish.png':[(800, 100), 1],
    'ingame_logo.png':[(600, 264), 1],
    'instructions_screen.png':[(800, 600), 1]
}

#Animations is in the form:
#   ANIMATIONS = {
#       'image_filename':{
#           anim_name:([(sprite1x, sprite1y), (sprite2x, sprite2y), ...], delay)
#           ...
#       }
#       ...
#   }
#NOTE: the animation name 'PLACEHOLDER' is featured in any image that doesn't
#need to be animated. It makes an image simply hold still.
ANIMATIONS = {
    'tn.png':{
        'PLACEHOLDER':([(0, 0)], 1),
        'run':([(0, 0), (1, 0), (2, 0), (3, 0)], 8),
        'die':([(0, 1), (1, 1), (2, 1), (3, 1)], 2),
        'materialize':([(3, 1), (2, 1), (1, 1), (0, 1)], 1),
        'blink':([(0, 0), (3, 1)], 6)
    },
    'woodstest1.png':{
        'PLACEHOLDER':([(0, 0)], 1)
    },
    'woodstest2.png':{
        'PLACEHOLDER':([(0, 0)], 1)
    },
    'grass1.png':{
        'PLACEHOLDER':([(0, 0)], 1)
    },
    'tatami1.png':{
        'PLACEHOLDER':([(0, 0)], 1)
    },
    'bul.png':{
        'PLACEHOLDER':([(0, 0)], 1)
    },
    'shuriken1.png':{
        'PLACEHOLDER':([(0, 0)], 1),
        'spin':([(0, 0), (1, 0), (2, 0), (0, 1)], 3)
    },
    'life_thumbnail.png':{
        'PLACEHOLDER':([(0, 0)], 1),
        'blink':([(0, 0), (1, 0)], 1)
    },
    'bomb_thumbnail.png':{
        'PLACEHOLDER':([(0, 0)], 1),
        'blink':([(0, 0), (1, 0)], 1)
    },
    'ninja_particle.png':{
        'PLACEHOLDER':([(0, 0)], 1)
    },
    'smoke.png':{
        'PLACEHOLDER':([(0, 0)], 1),
        'dissipate':([(0, 0), (1, 0), (0, 1), (1, 1)], 6)
    },
    'start.png':{
        'PLACEHOLDER':([(0, 0)], 1)
    },
    'menu.png':{
        'PLACEHOLDER':([(0, 0)], 1)
    },
    'instructions.png':{
        'PLACEHOLDER':([(0, 0)], 1)
    },
    'sasuke.png':{
        'PLACEHOLDER':([(0, 0)], 1),
        'run':([(0, 0), (1, 0), (2, 0), (3, 0)], 8)
    },
    'goemon_open.png':{
        'PLACEHOLDER':([(0, 0)], 1),
        'run':([(0, 0), (1, 0), (2, 0), (3, 0)], 8)
    },
    'goemon_closed.png':{
        'PLACEHOLDER':([(0, 0)], 1),
        'run':([(0, 0), (1, 0), (2, 0), (3, 0)], 8)
    },
    'goemon_armless_open.png':{
        'PLACEHOLDER':([(0, 0)], 1),
        'run':([(0, 0), (1, 0), (2, 0), (3, 0)], 8)
    },
    'goemon_armless_closed.png':{
        'PLACEHOLDER':([(0, 0)], 1),
        'run':([(0, 0), (1, 0), (2, 0), (3, 0)], 8)
    },
    'arm.png':{
        'PLACEHOLDER':([(0, 0)], 1),
        'spin':([(0, 0), (1, 0), (2, 0), (0, 1)], 3)
    },
    'bomb.png':{
        'PLACEHOLDER':([(0, 0)], 1)
    },
    '1up.png':{
        'PLACEHOLDER':([(0, 0)], 1)
    },
    '1times_score.png':{
        'PLACEHOLDER':([(0, 0)], 1)
    },
    '3times_score.png':{
        'PLACEHOLDER':([(0, 0)], 1)
    },
    'finish.png':{
        'PLACEHOLDER':([(0, 0)], 1)
    },
    'ingame_logo.png':{
        'PLACEHOLDER':([(0, 0)], 1)
    },
    'instructions_screen.png':{
        'PLACEHOLDER':([(0, 0)], 1)
    }
}

SOUNDS = ('Here_I_Am.wav', 'Hyacinth.wav', 'Meaner.wav', 'Four-Fourths_Ninja.wav', 'hit.wav',
          'transition.wav', 'pickup1.wav', 'pickup2.wav', 'pickup3.wav', 'bomb.wav', 'shoot.wav')#tulpe of string file-names

####################################################################################################

class Game(object):
    """
    Class for the main game controller. Responsible
    for managing the game logic.
    """

    def __init__(self, framerate, screen_width, screen_height):

        ##################
        ## NAMED VALUES ##
        ##################
        
        self.framerate = framerate
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.on = True
        self.mode = 'OPEN'
        self.sheets = {}
        self.animations = ANIMATIONS#don't need to be loaded
        self.sounds = {}
        self.level_timer = 0
        self.finish_point = 0
        self.finish_line = None
        self.finish_timer = 110
        self.finished = False

        self.end_text = 'GAME OVER'# this is what is drawn on the game over screen. it can also say YOU WIN

        self.worldspeed = 4

        self.font = pygame.font.Font(os.path.join('data', 'font', 'Berenika.ttf'), 11)
        self.font2 = pygame.font.Font(os.path.join('data', 'font', 'Berenika.ttf'), 48)

        self.levels = []
        self.level_index = 0

        self.open_timer = 110

        self.started = False
        self.start_counter = 50

        self.instructioned = False
        self.instruction_timer = 20

        self.between_timer = 51

        self.fade_in = False

        self.old_highscore = 0
        self.score_life_counter = 1
        
        #data dicts. Stores only raw data (strings and numbers)
        self.enemies = {}
        self.enemy_phases = {}
        self.shot_lists = {}
        self.patterns = {}
        self.bullet_phases = {}

        self.pickups = {}

        #visible game values
        try:
            f = open(os.path.join('data', 'scr', 'highscore.dat'), 'r')

            self.highscore = int(f.readline())
            
            f.close()

        except Exception:
            f = open(os.path.join('data', 'scr', 'highscore.dat'), 'w')

            f.write('0')

            f.close()
        
        self.score = 0
        self.multiplier = 1
        self.bombs = 3
        self.max_bombs = 3
        self.lives = 99
        self.bomb_color = (255, 255, 0)#yellow = full, white = not full

        self.muted = False
        self.music_playing = False
        self.music_stopped = False

        self.music_channel = pygame.mixer.Channel(0)
        self.sfx_channel = pygame.mixer.Channel(1)
        self.sfx_channel2 = pygame.mixer.Channel(2)

        self.left_mouse_pressed = False

        ########################
        ## CONTROLLER OBJECTS ##
        ########################

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.frameclock = pygame.time.Clock()

        #################
        ## SETUP CALLS ##
        #################
        
        self.load_sheets()
        self.load_sounds()
        pygame.display.set_caption('Torso Ninja II')
        
        ##################
        ## GAME OBJECTS ##
        ##################

        self.transition_surface = pygame.Surface((screen_width, screen_height))
        self.transition_surface_rect = self.transition_surface.get_rect()
        self.transition_surface_rect.topleft = (0, 0)
        self.transition_surface.fill((255, 255, 255))
        self.transition_alpha = 255
        self.transition_surface.set_alpha(self.transition_alpha)

        self.logo = Entity(self, self.sheets['ingame_logo.png'], (0, 0),
                                 ANIMATIONS['ingame_logo.png'], (110, 70))

        self.start_button = Button(self, self.sheets['start.png'], (0, 0), ANIMATIONS['start.png'], (310, 400),
                                   (0, 1))

        self.menu_button = Button(self, self.sheets['menu.png'], (0, 0), ANIMATIONS['menu.png'], (320, 500),
                                   (0, 1))
        
        self.instructions_button = Button(self, self.sheets['instructions.png'], (0, 0),
                                          ANIMATIONS['instructions.png'], (210, 500), (0, 1))
        self.instructions_screen = Entity(self, self.sheets['instructions_screen.png'], (0, 0),
                                          ANIMATIONS['instructions_screen.png'], (0, 0))
        
        self.player = Torso_Ninja(self, self.sheets['tn.png'], (0, 0), ANIMATIONS['tn.png'], (0, 0))
        self.player.set_animation('run')

        self.scroll1 = None
        self.scroll2 = None
        self.music = 'Four-Fourths_Ninja.wav'

        self.lives_icon = Entity(self, self.sheets['life_thumbnail.png'], (0, 0),
                                 ANIMATIONS['life_thumbnail.png'], (732, 16))
        self.bombs_icon = Entity(self, self.sheets['bomb_thumbnail.png'], (0, 0),
                                 ANIMATIONS['bomb_thumbnail.png'], (732, 48))

        ###################
        ## SPRITE GROUPS ##
        ###################

        #main menu objs only
        self.main_menu_draw_group = pygame.sprite.LayeredUpdates()
        self.main_menu_draw_group.add(self.logo, self.start_button, self.instructions_button, layer = 1)

        self.over_draw_group = pygame.sprite.LayeredUpdates()
        self.over_draw_group.add(self.menu_button, layer = 1)

        #instructions objects only
        self.instructions_menu_draw_group = pygame.sprite.LayeredUpdates()
        self.instructions_menu_draw_group.add(self.menu_button, self.instructions_screen, layer = 1)

        #draw_group handles all drawn objects
        self.draw_group = pygame.sprite.LayeredUpdates()
        self.draw_group.add(self.player, self.lives_icon, self.bombs_icon, layer = 1)

        #collision group for torso ninja to iterate through
        self.collision_group = pygame.sprite.Group()

        self.pickup_group = pygame.sprite.Group()

        self.enumerate_levels("level_config.ini")#TMP - should happen when a level is started

    def enumerate_levels(self, configfile):

        config = ConfigParser.ConfigParser()

        config.read(os.path.join('data', 'lvl', configfile))

        for section in config.sections():

            if section[0:2] == "DF":

                for option in config.options(section):

                    self.levels.append(config.get(section, option).lower())
        
    def load_sheets(self, sheets = SHEETS):
        """
        Load all sheets given, either from the SHEETS constant,
        or from a supplied dict of the proper form.
        """

        #enumerate and step through the provided dict
        for sh in sheets:

            #create a sheet object for every specified sheet, and bind it to the sheet list
            self.sheets[sh] = Sheet(self, sh, sheets[sh][0], sheets[sh][1])

    def load_sounds(self):

        for s in SOUNDS:

            self.sounds[s] = pygame.mixer.Sound(os.path.join('data', 'snd', s))

    def play_sound(self, sound, loops = 0, channel = 1):

        if channel == 1:

            self.sfx_channel.play(self.sounds[sound], loops)

        elif channel == 0:

            self.music_channel.play(self.sounds[sound], loops)

        elif channel == 2:#for powerups

            self.sfx_channel2.play(self.sounds[sound], loops)

    def stop_sound(self, sound):

        if sound != None:

            self.sounds[sound].stop()

    def load_level(self, levelfile):
        """
        Create a level from a markup levelfile. Creates scrollers,
        enemy spawns, and other such things.
        """

        config = ConfigParser.ConfigParser()

        config.read(os.path.join('data', 'lvl', levelfile))

        for section in config.sections():

            if section[0:2] == "LV":

                self.scroll1 = Scroller(self, self.sheets[config.get(section, "scroller1")], (0, 0),
                                ANIMATIONS[config.get(section, "scroller1")], (0, 0))
                self.scroll2 = Scroller(self, self.sheets[config.get(section, "scroller2")], (0, 0),
                                ANIMATIONS[config.get(section, "scroller2")], (0, -600))

                self.draw_group.add(self.scroll1, self.scroll2, layer = 0)

                self.finish_point = config.getint(section, "finish")

                if config.get(section, "music") in SOUNDS:

                    self.music = config.get(section, "music")

            elif section[0:2] == "PI":

                self.pickups[section] = {
                    "type":config.get(section, "type"),
                    "sheet":config.get(section, "sheet"),
                    "sprite":(config.getint(section, "spritex"), config.getint(section, "spritey")),
                    "animations":config.get(section, "animations"),
                    "position":(config.getint(section, "positionx"), config.getint(section, "positiony")),
                    "spawn":config.getint(section, "spawn")
                    }

            elif section[0:2] == "EN":

                self.enemies[section] = {
                    "sheet":config.get(section, "sheet"),
                    "sprite":(config.getint(section, "spritex"), config.getint(section, "spritey")),
                    "animations":config.get(section, "animations"),
                    "active_anim":config.get(section, "activeanimation"),
                    "position":(config.getint(section, "positionx"), config.getint(section, "positiony")),
                    "spawn":config.getint(section, "spawn"),#the timer number at which this enemy should appear
                    "phases":[],
                    "patterns":[]
                    }

                for option in config.options(section):

                    if option[0:5].upper() == "PHASE":

                        self.enemies[section]["phases"].append(config.get(section, option).upper())

                    elif option[0:7].upper() == "PATTERN":

                        self.enemies[section]["patterns"].append(config.get(section, option).upper())

            elif section[0:2] == "EP":

                self.enemy_phases[section] = {
                    "angle":config.getfloat(section, "angle"),
                    "speed":config.getfloat(section, "speed"),
                    "phase_timer":config.getint(section, "phasetimer")}

            elif section[0:2] == "SL":

                self.shot_lists[section] = {
                    "sheet":config.get(section, "sheet"),
                    "sprite":(config.getint(section, "spritex"), config.getint(section, "spritey")),
                    "animations":config.get(section, "animations"),
                    "active_anim":config.get(section, "activeanimation"),
                    "phases":[]}

                for option in config.options(section):

                    if option[0:5].upper() == "PHASE":

                        self.shot_lists[section]["phases"].append(config.get(section, option).upper())

            elif section[0:2] == "PT":

                self.patterns[section] = {
                    "shot_lists":[],
                    "timer":config.getint(section, "timer")}

                for option in config.options(section):

                    if option[0:8].upper() == "SHOTLIST":

                        self.patterns[section]["shot_lists"].append(config.get(section, option).upper())

            elif section[0:2] == "BP":

                if config.get(section, "angle") == 'OLD':

                    ang = 'OLD'

                else:

                    ang = config.getfloat(section, "angle")

                self.bullet_phases[section] = {
                    "angle":ang,
                    "speed":config.getfloat(section, "speed"),
                    "rotation":config.getfloat(section, "rotation"),
                    "phase_timer":config.getint(section, "phasetimer")
                    }

    def tally_score(self):

        if self.player.alive == True and self.finished == False:

            self.score += self.multiplier

        if self.score >= self.score_life_counter * 100000:

            self.score_life_counter += 1
            self.lives += 1

            if self.muted == False:
                self.play_sound('pickup2.wav', 0, 2)

    def check_highscore(self, score):

        if score > self.highscore:

            self.highscore = score

            f = open(os.path.join('data', 'scr', 'highscore.dat'), 'w')

            f.write(str(score))

            f.close()

    def print_text(self):

        bx = self.font.render('X', False, (0, 0, 0))
        bx_rect = bx.get_rect()
        bx_rect.topleft = (747, 45)

        b = self.font.render(str(self.bombs), False, self.bomb_color)
        b_rect = b.get_rect()
        b_rect.topleft = (762, 44)

        lx = self.font.render('X', False, (0, 0, 0))
        lx_rect = bx.get_rect()
        lx_rect.topleft = (747, 13)

        l = self.font.render(str(self.lives), False, (0, 0, 0))
        l_rect = b.get_rect()
        l_rect.topleft = (762, 12)

        sh = self.font.render('SCORE', False, (255, 0, 0))
        sh_rect = sh.get_rect()
        sh_rect.topleft = (8, 12)

        s = self.font.render(str(self.score), False, (255, 0, 0))
        s_rect = s.get_rect()
        s_rect.topleft = (75, 12)

        mh = self.font.render('MULTIPLIER    X', False, (0, 0, 0))
        mh_rect = mh.get_rect()
        mh_rect.topleft = (8, 44)

        m = self.font.render(str(self.multiplier), False, (200, 0, 200))
        m_rect = m.get_rect()
        m_rect.topleft = (84, 44)

        self.screen.blit(bx, bx_rect)
        self.screen.blit(b, b_rect)

        self.screen.blit(lx, lx_rect)
        self.screen.blit(l, l_rect)

        self.screen.blit(sh, sh_rect)
        self.screen.blit(s, s_rect)

        self.screen.blit(mh, mh_rect)
        self.screen.blit(m, m_rect)

    def spawn(self):

        if self.level_timer == self.finish_point:

            self.finish_line = Finish_Line(self, self.sheets['finish.png'], (0, 0), ANIMATIONS['finish.png'],
                                           (0, -120))

            self.draw_group.add(self.finish_line, layer = 0)

        for p in self.pickups:

            if self.pickups[p]["spawn"] == self.level_timer:

                new_pickup = Pickup(self, self.sheets[self.pickups[p]["sheet"]], self.pickups[p]["sprite"],
                                    ANIMATIONS[self.pickups[p]["animations"]], self.pickups[p]["position"],
                                    self.pickups[p]["type"])

                self.pickup_group.add(new_pickup)
                self.draw_group.add(new_pickup, layer = 2)

        for e in self.enemies:

            if self.enemies[e]["spawn"] == self.level_timer:

                phases = []

                for ph in self.enemies[e]["phases"]:

                    phases.append((self.enemy_phases[ph]["angle"], self.enemy_phases[ph]["speed"],
                                   self.enemy_phases[ph]["phase_timer"]))

                patterns = []

                for pt in self.enemies[e]["patterns"]:

                    shols = []

                    for sl in self.patterns[pt]["shot_lists"]:

                        bphases = []

                        for bp in self.shot_lists[sl]["phases"]:

                            bphases.append((self.bullet_phases[bp]["angle"],
                                           self.bullet_phases[bp]["speed"],
                                           self.bullet_phases[bp]["rotation"],
                                           self.bullet_phases[bp]["phase_timer"]))

                        shols.append((self.sheets[self.shot_lists[sl]["sheet"]],
                                      self.shot_lists[sl]["sprite"],
                                      ANIMATIONS[self.shot_lists[sl]["animations"]],
                                      self.shot_lists[sl]["active_anim"],
                                      bphases))

                    patterns.append((shols, self.patterns[pt]["timer"]))

                new_e = Enemy(self, self.sheets[self.enemies[e]["sheet"]], self.enemies[e]["sprite"],
                              ANIMATIONS[self.enemies[e]["animations"]], self.enemies[e]["position"],
                              phases, patterns)

                self.draw_group.add(new_e, layer=1)
                self.collision_group.add(new_e)

    def switch_to_instructions(self):

        if self.instruction_timer > 0:

            self.instruction_timer -= 1

        else:

            self.mode = 'INSTRUCTION'

    def start_game(self):

        if self.start_counter > 0:
            self.start_counter -= 1

            self.transition_surface_rect.topleft = (self.transition_surface_rect.topleft[0] - 16,
                                                    self.transition_surface_rect.topleft[1])

        else:

            self.score = 0
            self.bombs = 3
            self.lives = 3

            self.level_index = 0

            self.mode = 'BETWEEN'

            self.clear_level()

            self.load_level(self.levels[self.level_index])#LOAD LEVEL IN SEPERATE PLACE

    def clear_level(self):

        self.draw_group.empty()

        self.draw_group.add(self.player, self.lives_icon, self.bombs_icon, layer = 1)

        self.collision_group.empty()
        self.pickup_group.empty()

        self.level_timer = 0
        self.music_playing = False
        self.music_stopped = True
        self.stop_sound(self.music)
        self.music = None

        self.between_timer = 110

        self.fade_in = False

        self.worldspeed = 4

        self.finish_point = 0
        self.finish_line = None
        self.finish_timer = 110
        self.finished = False

        self.enemies = {}
        self.enemy_phases = {}
        self.shot_lists = {}
        self.patterns = {}
        self.bullet_phases = {}

        self.pickups = {}

    def finish_stage(self):

        if self.finish_timer > 0:

            self.finish_timer -= 1

            if self.finish_timer <= 50:

                self.transition_surface_rect.topleft = (self.transition_surface_rect.topleft[0] - 16,
                                                        self.transition_surface_rect.topleft[1])

            elif self.finish_timer == 40:

                if self.muted == False:
                    self.play_sound('transition.wav')

        else:

            self.mode = 'BETWEEN'

            self.clear_level()

            if self.level_index <= len(self.levels) -1:

                self.load_level(self.levels[self.level_index])#LOAD LEVEL IN SEPERATE PLACE

            else:

                self.end_text = 'YOU WIN'

                self.old_highscore = self.highscore

                self.check_highscore(self.score)

                self.left_mouse_pressed = False
                self.started = False
                self.transition_surface_rect.topleft = (800, 0)
                self.music = 'Four-Fourths_Ninja.wav'
                self.music_playing = False
                self.music_stopped = False

                pygame.mouse.set_visible(True)

                self.mode = 'OVER'

    def end_game(self):

        self.clear_level()

        self.level_index = 0

        self.end_text = 'GAME OVER'

        self.old_highscore = self.highscore

        self.check_highscore(self.score)

        self.left_mouse_pressed = False
        self.started = False
        self.transition_surface_rect.topleft = (800, 0)
        self.music = 'Four-Fourths_Ninja.wav'
        self.music_playing = False
        self.music_stopped = False

        pygame.mouse.set_visible(True)

        self.mode = 'OVER'

    def shift_frames(self):
        """
        Shift to the next frame of animation.
        MUST ALWAYS BE THE FIRST CALLED METHOD
        IN THE GAME LOOP!
        """

        self.frameclock.tick(self.framerate)

    def handle_events(self):
        """
        Handle all events in the event.get list.
        """

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                self.on = False

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1 and self.mode == 'GAME':

                    self.left_mouse_pressed = True

                elif event.button == 1 and self.mode == 'MENU':

                    if self.start_button.rect.collidepoint(pygame.mouse.get_pos()):

                        self.started = True
                        self.transition_alpha = 255
                        self.transition_surface.set_alpha(self.transition_alpha)
                        self.transition_surface.fill((0, 0, 0))

                        if self.muted == False:
                            self.play_sound('transition.wav')

                    elif self.instructions_button.rect.collidepoint(pygame.mouse.get_pos()):

                        self.instructioned = True

                elif event.button == 1 and (self.mode == 'OVER' or self.mode == 'INSTRUCTION'):

                    if self.menu_button.rect.collidepoint(pygame.mouse.get_pos()):

                        self.mode = 'MENU'

                        self.instructioned = False
                        self.instruction_timer = 20

            elif event.type == pygame.MOUSEBUTTONUP:

                if event.button == 1:

                    self.left_mouse_pressed = False

    def update_game(self):
        """
        Updates game objects and values and draws the
        game objects to the screen. Mode-controlled.
        """

        if self.mode == 'OPEN':

            self.screen.fill((0, 249, 255))

            if self.open_timer > 0:
                self.open_timer -= 1

                if self.open_timer <= 51:

                    self.transition_alpha -= 5

                if self.transition_alpha >= 0:

                    self.transition_surface.set_alpha(self.transition_alpha)

                else:

                    self.transition_surface.set_alpha(0)

            else:

                self.mode = 'MENU'
                self.transition_surface_rect.topleft = (800, 0)

            self.screen.blit(self.transition_surface, self.transition_surface_rect)

        elif self.mode == 'MENU':

            if self.music_playing == False and self.muted == False and self.music_stopped == False:
                self.music_playing = True
                self.play_sound(self.music, 1, 0)

            #blank the screen first
            self.screen.fill((0, 249, 255))

            if self.started:
                self.start_game()

            if self.instructioned:
                self.switch_to_instructions()

            self.main_menu_draw_group.update(self.screen)

            h = self.font.render('High Score: ' + str(self.highscore), False, (255, 0, 0))
            hr = h.get_rect()
            hr.topleft = (660, 540)

            self.screen.blit(h, hr)

            self.screen.blit(self.transition_surface, self.transition_surface_rect)

        elif self.mode == 'INSTRUCTION':

            if self.music_playing == False and self.muted == False and self.music_stopped == False:
                self.music_playing = True
                self.play_sound(self.music, 1, 0)

            self.screen.fill((0, 249, 255))

            self.instructions_menu_draw_group.update(self.screen)

        elif self.mode == 'BETWEEN':

            self.screen.fill((0, 0, 0))

            sh = self.font2.render('SCORE:', False, (0, 255, 255))
            sh_rect = sh.get_rect()
            sh_rect.topleft = (230, 120)

            s = self.font2.render(str(self.score), False, (0, 255, 255))
            s_rect = s.get_rect()
            s_rect.topleft = (460, 120)

            ready = self.font2.render('GET READY', False, (255, 255, 255))
            ready_rect = ready.get_rect()
            ready_rect.topleft = (230, 300)

            self.screen.blit(sh, sh_rect)
            self.screen.blit(s, s_rect)
            self.screen.blit(ready, ready_rect)

            if self.between_timer > 0:

                self.between_timer -= 1

            else:

                self.mode = 'GAME'
                self.transition_surface_rect.topleft = (0, 0)

                self.music_stopped = False

                pygame.mouse.set_visible(False)

        #if mode is 'GAME' we are playing the main game and should update
        #the payer position, scroll the world, spawn enemies/bullets, and
        #keep score, just for starters
        elif self.mode == 'GAME':

            if self.transition_alpha >= 0 and self.fade_in == False:

                self.transition_alpha -= 5

                self.transition_surface.set_alpha(self.transition_alpha)

            elif self.fade_in == False:

                self.transition_surface.set_alpha(0)
                self.fade_in = True

            if self.music_playing == False and self.muted == False and self.music_stopped == False:
                self.music_playing = True
                self.play_sound(self.music, 1, 0)

            self.level_timer += 1

            if self.bombs == 3:
                self.bomb_color = (255, 255, 0)
            else:
                self.bomb_color = (0, 0, 0)

            self.spawn()

            self.tally_score()

            self.draw_group.update(self.screen)#draw everything

            if self.transition_alpha <= 0:

                self.print_text()

            else:

                self.screen.blit(self.transition_surface, self.transition_surface_rect)

            if self.finished:
                self.finish_stage()

        elif self.mode == 'OVER':

            self.screen.fill((0, 0, 0))

            e = self.font2.render(self.end_text, False, (0, 255, 255))
            e_rect = e.get_rect()#hue hue hue
            e_rect.topleft = (280, 120)

            ys = self.font2.render("Your Score: " + str(self.score), False, (0, 255, 255))
            ys_rect = ys.get_rect()
            ys_rect.topleft = (160, 220)

            hs = self.font2.render("High Score: " + str(self.old_highscore), False, (0, 255, 0))
            hs_rect = hs.get_rect()
            hs_rect.topleft = (160, 300)

            if self.score > self.old_highscore:

                n = self.font2.render('NEW HIGH SCORE!', False, (0, 255, 255))
                n_rect = n.get_rect()
                n_rect.topleft = (220, 380)

                self.screen.blit(n, n_rect)

            self.screen.blit(e, e_rect)
            self.screen.blit(ys, ys_rect)
            self.screen.blit(hs, hs_rect)

            self.over_draw_group.update(self.screen)

        #Call to update screen
        pygame.display.update()

    def mainloop(self):

        while self.on:

            self.shift_frames()
            self.handle_events()
            self.update_game()

        pygame.quit()

####################################################################################################

class Sheet(object):
    """
    Class for the spritesheets that entity images are loaded
    from. Supports regularized spritesheets only (all sprites
    feature the same dimensions).
    """

    def __init__(self, game, name, sprite_size, total_sprites):

        self.game = game

        #try and load all sprites on the sheet
        success = self.load_sheet(name, sprite_size, total_sprites)

        if success == 1:#failure, cleanup vals
            
            self.sprites = {}
            print "Failed to load sheet: " + name#error message

    def load_sheet(self, name, sprite_size, total_sprites):
        """
        Load a sheet and divide it into subsurfaces for
        use as images by sprite entities.
        """

        #remember important variables
        self.name = name
        self.sprite_size = sprite_size
        self.total_sprites = total_sprites

        #Step 1: attempt to load the appropriate image file
        try:

            self.sheet = pygame.image.load(os.path.join("data", "img", name))

        #catch a missing file error and stop, set up graceful failure
        except:

            self.sheet = None

        #Step 2: if sheet exists, divide it into sprites
        if self.sheet != None:

            self.sprites = {}#empty dict to hold our loaded images

            #vals to track our progress thru the sheet
            x = 0
            y = 0

            #while we still have more sprites to load, load them
            while len(self.sprites) < total_sprites:

                #get a rect that can be used to make a subsurface of the sheet
                new_rect = pygame.Rect((x * sprite_size[0], y * sprite_size[1]),
                                            sprite_size)

                #load image, store it in our dict, set its colorkey
                self.sprites[(x, y)] = self.sheet.subsurface(new_rect).convert()
                self.sprites[(x, y)].set_colorkey((255, 0, 255))

                x += 1#scoot over to the right

                #if we're hanging off the right side, scoot down and start over
                #again from the far left
                if x * sprite_size[0] >= self.sheet.get_width():

                    x = 0
                    y += 1

            return 0#SUCCESS!!

        #No sheet exists
        else:

            return 1# failure :C

####################################################################################################

class Entity(pygame.sprite.Sprite):
    """
    Visible game object parent class. Allows for drawing, moving,
    animating, and more. Basically expands on pygame.sprite.Sprite.
    """

    def __init__(self, game, sheet, sprite, animations, position):

        pygame.sprite.Sprite.__init__(self)

        self.game = game
        
        #loads image and makes rect
        self.sheet = sheet
        self.image = self.sheet.sprites[sprite]#the specific sprite of the sheet
        self.rect = self.image.get_rect()
        self.rect.topleft = position

        #get center x-y position & previous coordinates
        self.x = self.rect.center[0]
        self.y = self.rect.center[1]
        self.prev_x = self.x
        self.prev_y = self.y

        #some trig values
        self.angle = None
        self.speed = None
        self.rotation = None

        #can be turned off if we don't want to be drawn
        self.visible = True

        #determines if we get redrawn
        self.dirty = 1

        #determines our layer
        self.layer = 1

        ########################
        #ANIMATIONS:           
        #Animations are a tuple of two values:
        #   (sprites, timer)
        #where 'sprites' is an ORDERED list of sheet positions values
        #and 'timer' is the amount of time that any one sprite will
        #be shown on the screen.
        #######################
        
        #Animation values. Remember:entity takes a whole dict of animations!
        self.animations = {}#dict which stores all animations
        self.current_animation = None
        self.current_sprite = sprite
        self.animation_timer = -1#-1 = off. this val is used for a countdown

        #setup all animations available to this entity's spritesheet
        if animations != None:
            
            for an in animations:

                self.setup_animation(an, animations[an][0], animations[an][1])

    def center(self, new_x, new_y):
        """
        Updates x-y position and prev_x-prev_y position, by the
        center of the rect.
        """

        self.prev_x = self.x
        self.prev_y = self.y

        self.x = new_x
        self.y = new_y

    def offset_move(self, offset):
        """
        Move rect by the provided offset, from the topleft.
        """

        self.rect.topleft = (self.rect.topleft[0] + offset[0], self.rect.topleft[1] + offset[1])

    def rotate(self, rotation = None):
        """
        Shift the angle by the given rotation.
        """

        self.angle += rotation

    def trigonometric_move(self):
        """
        Move using vector math.
        """

        self.prev_x = self.x
        self.prev_y = self.y

        self.x += math.cos(self.angle) * self.speed
        self.y -= math.sin(self.angle) * self.speed

        self.rect.center = (self.x, self.y)

    def setup_animation(self, name, sprites, timer = 2):
        """
        Sets up an animation given a unique name, a list
        of sprite origin positions on the entity's sheet,
        and a timer. Sprites must be in an ordered list.
        """

        self.animations[name] = (sprites, timer)

    def set_animation(self, name):
        """
        Set the chosen animation as the current (active)
        animation, provided it is already in the animations
        list.
        """

        #check through the animations for the chosen animation
        if name in self.animations.keys():

            #setup all animation values for the new animation
            self.current_animation = self.animations[name]
            self.animation_timer = self.current_animation[1]
            self.current_sprite = self.current_animation[0][0]
            self.image = self.sheet.sprites[self.current_sprite]

        #handles errors if the animation is not found
        else:

            print "ERROR: Animation '" + name + "' not found."

    def animate(self):
        """
        Countdown each frame from the maximum (the animation
        timer number) and shift frames when 0 is reached.
        """

        if self.animation_timer != -1:#animations are not off

            #if we are not at zero, countdown 1
            if self.animation_timer > 0:

                self.animation_timer -= 1

            #if we are, shift frames in the animation and reset the timer.
            else:

                self.shift_animation()
                self.animation_timer = self.current_animation[1]

    def shift_animation(self):
        """
        Shifts to the next sprite (frame) in the animation.
        """

        if self.current_animation != None:#make sure we actually have one

            sprites = self.current_animation[0]#'sprites' name for convenience

            #if the iterated sprite value is not out of range
            #NOTE: the same sprite loaction on the sheet cannot be repeated
            #in an animation because of the .index method. A sheet must
            #have a unique sprite for each location used in an animation
            if sprites.index(self.current_sprite) + 1 <= (len(sprites) - 1):

                newsp = sprites[sprites.index(self.current_sprite) + 1]

                self.current_sprite = newsp
                self.image = self.sheet.sprites[newsp]

            #else if the value is out of range, restart animation
            else:

                #shift to the first sprite in the list
                self.current_sprite = sprites[0]
                self.image = self.sheet.sprites[sprites[0]]

    def act(self, surface = None, *args):
        """
        Method to be overwritten with update data unique to subclasses. Can
        handle any arguments passed via update().
        """

        pass

    def update(self, surface = None, *args):

        self.act(surface, args)#method to be overwritten with unique update data

        #play an animation, if one is set
        if self.current_animation != None:

            self.animate()

        #finally, draw this entity if we can (surface exists and we're onscreen)
        r = surface.get_rect()
        
        if surface != None and self.rect.colliderect(r) and self.visible:

            surface.blit(self.image, self.rect)

####################################################################################################

class Button(Entity):
    """
    Class for clickable menu objects.
    """

    def __init__(self, game, sheet, sprite, animations, position, highlight_sprite):

        Entity.__init__(self, game, sheet, sprite, animations, position)

        self.highlight_sprite = highlight_sprite
        self.original_sprite = sprite

    def act(self, surface = None, *args):

        if self.rect.collidepoint(pygame.mouse.get_pos()):

            self.current_sprite = self.highlight_sprite

            self.image = self.sheet.sprites[self.current_sprite]

        else:

            self.current_sprite = self.original_sprite

            self.image = self.sheet.sprites[self.current_sprite]

####################################################################################################

class Torso_Ninja(Entity):
    """
    Class for the player character
    """

    def __init__(self, game, sheet, sprite, animations, position):

        Entity.__init__(self, game, sheet, sprite, animations, position)

        self.alive = True
        self.death_counter = 90
        self.invincible = False
        self.blinking = False
        self.blink_counter = 0

        self.hitbox = pygame.Rect(0, 0, 8, 12)
        self.hitbox.center = self.rect.center

    def lock_to_mouse(self):

        self.rect.center = pygame.mouse.get_pos()
        self.hitbox.center = self.rect.center

    def check_collisions(self):

        #check collisions with bullets and/or enemies first
        for sprite in self.game.collision_group:

            if self.hitbox.colliderect(sprite.rect) and self.alive and self.invincible == False:

                if self.game.muted == False:
                    self.game.play_sound('hit.wav')

                self.die()

        #check pickups
        for p in self.game.pickup_group:

            if self.rect.colliderect(p.rect) and self.alive:#go by rect rather than hitbox

                self.get_pickup(p)

    def get_pickup(self, pickup):

        if pickup.pickup_type == 'LIFE':

            if self.game.muted == False:
                self.game.play_sound('pickup2.wav', 0, 2)

            self.game.lives += 1

        elif pickup.pickup_type == '1XMP':

            if self.game.muted == False:
                self.game.play_sound('pickup1.wav', 0, 2)

            self.game.multiplier += 1

        elif pickup.pickup_type == '3XMP':

            if self.game.muted == False:
                self.game.play_sound('pickup1.wav', 0, 2)

            self.game.multiplier += 3

        elif pickup.pickup_type == 'BOMB':

            if self.game.muted == False:
                self.game.play_sound('pickup3.wav', 0, 2)

            if self.game.bombs < self.game.max_bombs:

                self.game.bombs += 1

            else:

                self.game.score += 500

        pickup.kill()

    def die(self):

        self.death_counter = 90
        self.alive = False
        self.visible = False

        self.game.lives -= 1
        self.game.multiplier = 1

        #create flying particles
        nw = Bullet(self.game, self.game.sheets['ninja_particle.png'], (0, 0),
                    ANIMATIONS['ninja_particle.png'], self.rect.center,
                    [((3 * math.pi)/4, 7, 0, -1)])
        ne = Bullet(self.game, self.game.sheets['ninja_particle.png'], (0, 0),
                    ANIMATIONS['ninja_particle.png'], self.rect.center,
                    [(math.pi/4, 7, 0, -1)])
        sw = Bullet(self.game, self.game.sheets['ninja_particle.png'], (0, 0),
                    ANIMATIONS['ninja_particle.png'], self.rect.center,
                    [((5 * math.pi)/4, 7, 0, -1)])
        se = Bullet(self.game, self.game.sheets['ninja_particle.png'], (0, 0),
                    ANIMATIONS['ninja_particle.png'], self.rect.center,
                    [((7 * math.pi)/4, 7, 0, -1)])

        self.game.draw_group.add(nw, ne, sw, se)

    def respawn(self):

        if self.death_counter > 0:
            self.death_counter -= 1

        elif self.game.lives > 0:

            self.lock_to_mouse()

            self.blink_counter = 120
            self.visible = True
            self.set_animation('blink')
            self.blinking = True
            self.invincible = True
            self.alive = True
            
        else:

            self.game.end_game()

    def blink(self):

        if self.blink_counter > 0:
            self.blink_counter -= 1

            self.invincible = True

        else:

            self.invincible = False
            self.set_animation('run')
            self.blinking = False

    def bomb(self):

        if self.game.left_mouse_pressed == True and self.game.bombs > 0 and self.blink_counter == 0:

            if self.game.muted == False:
                self.game.play_sound('bomb.wav')

            b = Smoke(self.game, self.game.sheets['smoke.png'], (0, 0), ANIMATIONS['smoke.png'],
                      (self.rect.topleft[0] - 24, self.rect.topleft[1] - 16))

            self.game.draw_group.add(b, layer = 2)

            self.blink_counter = 120
            self.set_animation('blink')
            self.blinking = True

            self.game.bombs -= 1

    def act(self, screen = None, *args):

        if self.alive:

            self.lock_to_mouse()

            self.bomb()

            if self.invincible == False:

                self.check_collisions()

            if self.blinking:

                self.blink()

        else:

            self.respawn()

####################################################################################################

class Scroller(Entity):
    """
    Class for the scrolling backgrounds.
    """

    def __init__(self, game, sheet, sprite, animations, position):

        Entity.__init__(self, game, sheet, sprite, animations, position)

        self.scrolling = True
        self.layer = 0#scrollers are always on the background layer

    def scroll(self, speed):
        """
        Scrolls at the rate of 'speed' and resets
        to the initial y-position if we are too far.
        """

        self.offset_move((0, speed))

        if self.rect.topleft[1] >= SCROLLER_LIMIT_Y:

            self.rect.topleft = (self.rect.topleft[0], INITIAL_SCROLLER_Y)

    def act(self, screen = None, *args):

        if self.scrolling:

            self.scroll(self.game.worldspeed)

####################################################################################################

class Finish_Line(Entity):

    def __init__(self, game, sheet, sprite, animations, position):

        Entity.__init__(self, game, sheet, sprite, animations, position)

        self.collided = False

    def be_collided(self):

        if self.game.player.rect.colliderect(self.rect) and self.collided == False:

            self.game.finished = True

            self.game.transition_surface_rect.topleft = (800, 0)
            self.game.transition_surface.fill((0, 0, 0))

            self.game.transition_alpha = 255
            self.game.transition_surface.set_alpha(255)

            self.game.worldspeed = 0
            self.game.level_index += 1

            self.collided = True

    def act(self, surface = None, *args):

        self.be_collided()

        self.offset_move((0, self.game.worldspeed))

####################################################################################################

class Smoke(Entity):
    """
    Class for the image that displays when the smoke bomb is used.
    """

    def __init__(self, game, sheet, sprite, animations, position):

        Entity.__init__(self, game, sheet, sprite, animations, position)

        self.set_animation('dissipate')
        self.timer = 24

    def act(self, surface = None, *args):

        if self.timer > 0:
            self.timer -= 1
        else:
            self.kill()

####################################################################################################

class Pickup(Entity):

    def __init__(self, game, sheet, sprite, animations, position, pickup_type):

        Entity.__init__(self, game, sheet, sprite, animations, position)

        self.speed = self.game.worldspeed / 2

        self.pickup_type = pickup_type

    def act(self, surface = None, *args):

        self.offset_move((0, self.speed))

        if self.rect.topleft[1] > 600:
            self.kill()

####################################################################################################

class Enemy(Entity):

    def __init__(self, game, sheet, sprite, animations, position, phases = None, patterns = None):

        Entity.__init__(self, game, sheet, sprite, animations, position)

        #phases = [(angle, speed, phase_timer), ...]
        self.phases = phases

        self.current_phase = self.phases[0]
        self.phase_index = 0

        self.angle = self.phases[0][0]
        self.speed = self.phases[0][1]
        self.phase_timer = self.phases[0][2]

        #Paterns = [(shot_spawns_and_phases, shot_timer), ...]
        #shot_lists = [((sheet, sprite, anims, anim, [(angle, speed, rotation, phase_timer), ...]), ...)]
        self.patterns = patterns

        self.shot_lists = self.patterns[0][0]
        self.shot_timer = self.patterns[0][1]
        self.pattern_index = 0

        self.entrance_flag = False

        self.set_animation('run')

    def shift_phases(self):

        if self.phase_timer == -1:

            return

        elif self.phase_timer > 0:

            self.phase_timer -= 1

        else:

            self.phase_index += 1
            self.current_phase = self.phases[self.phase_index]
            self.speed = self.phases[self.phase_index][1]
            self.phase_timer = self.phases[self.phase_index][2]

            if self.phases[self.phase_index][0] != "OLD":

                self.angle = self.phases[self.phase_index][0]

    def shoot(self):

        if self.shot_timer > 0:

            self.shot_timer -= 1

        elif self.shot_timer == 0:

            if self.game.muted == False:
                self.game.play_sound('shoot.wav')

            for i in self.shot_lists:

                    b = Bullet(self.game, i[0], i[1], i[2], self.rect.center, i[4])
                    b.set_animation(i[3])
                    b.rect.center = self.rect.center
                    self.game.draw_group.add(b, layer = 1)
                    self.game.collision_group.add(b)

            if len(self.patterns) > self.pattern_index + 1:

                self.pattern_index += 1

                self.shot_lists = self.patterns[self.pattern_index][0]
                self.shot_timer = self.patterns[self.pattern_index][1]

            else:

                self.shot_timer = -1

        else:

            return

    def check_escape(self, surface = None):
        """
        Kill this entity if it is off screen.
        """

        r = surface.get_rect()

        if not self.rect.colliderect(r):

            if self.entrance_flag == True:

                self.kill()

        else:

            self.entrance_flag = True

    def act(self, surface = None, *args):

        self.shift_phases()

        self.trigonometric_move()

        self.shoot()

        self.check_escape(surface)

####################################################################################################
            
class Bullet(Entity):

    def __init__(self, game, sheet, sprite, animations, position, phases = None):

        Entity.__init__(self, game, sheet, sprite, animations, position)

        if phases != None:

            self.phases = phases

        else:

            self.phases = [(0, 1, 0, -1)]
            #####phases = [(angle, speed, rotation, phase_timer), ...]

        self.current_phase = self.phases[0]
        self.phase_index = 0

        self.angle = self.phases[0][0]
        self.speed = self.phases[0][1]
        self.rotation = self.phases[0][2]
        self.phase_timer = self.phases[0][3]

    def shift_phases(self):

        if self.phase_timer == -1:

            return

        elif self.phase_timer > 0:

            self.phase_timer -= 1

        else:

            self.phase_index += 1
            self.current_phase = self.phases[self.phase_index]
            self.speed = self.phases[self.phase_index][1]
            self.rotation = self.phases[self.phase_index][2]
            self.phase_timer = self.phases[self.phase_index][3]

            if self.phases[self.phase_index][0] != "OLD":

                self.angle = self.phases[self.phase_index][0]

    def check_escape(self, surface = None):
        """
        Kill this entity if it is off screen.
        """

        r = surface.get_rect()

        if not self.rect.colliderect(r):

            self.kill()

    def act(self, surface = None, *args):

        self.shift_phases()

        self.rotate(self.rotation)

        self.trigonometric_move()

        self.check_escape(surface)
