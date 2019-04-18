#!/usr/bin/env python3

# Copyright (c) 2017 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Control Cozmo's Cube lights

This script shows how you can control Cozmo's cube lights and set
them to different colors - to red, green and blue in this case.
'''

import time
import random
import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id

def changementCouleur(robot: cozmo.robot.Robot, nbCube, i):
    vert = cozmo.lights.Color(rgb=(46, 204, 113))
    bleu = cozmo.lights.Color(rgb=(52, 152, 219))
    violet = cozmo.lights.Color(rgb=(155, 89, 182))
    noir = cozmo.lights.Color(rgb=(52, 73, 94))
    jaune = cozmo.lights.Color(rgb=(241, 196, 15))
    rouge = cozmo.lights.Color(rgb=(231, 76, 60))
    blanc = cozmo.lights.Color(rgb=(255, 255, 255))
    Couleur = [vert, bleu, violet, noir, jaune, rouge, blanc]

    cube1 = robot.world.get_light_cube(LightCube1Id)  # looks like a paperclip
    cube2 = robot.world.get_light_cube(LightCube2Id)  # looks like a lamp / heart
    cube3 = robot.world.get_light_cube(LightCube3Id)  # looks like the letters 'ab' over 'T'

    if (nbCube==1):
        couleurcube1 = cozmo.lights.Light(on_color=(Couleur[i]))
        cube1.set_lights(couleurcube1)
    #endif
    elif (nbCube==2):
        couleurcube2 = cozmo.lights.Light(on_color=(Couleur[i]))
        cube2.set_lights(couleurcube2)
    #endif
    elif (nbCube==3):
        couleurcube3 = cozmo.lights.Light(on_color=(Couleur[i]))
        cube3.set_lights(couleurcube3)
    #endif
#enddef

def cozmo_program(robot: cozmo.robot.Robot):
    vert = cozmo.lights.Color(rgb=(46, 204, 113))
    bleu = cozmo.lights.Color(rgb=(52, 152, 219))
    violet = cozmo.lights.Color(rgb=(155, 89, 182))
    noir = cozmo.lights.Color(rgb=(52, 73, 94))
    jaune = cozmo.lights.Color(rgb=(241, 196, 15))
    rouge = cozmo.lights.Color(rgb=(231, 76, 60))
    blanc = cozmo.lights.Color(rgb=(255, 255, 255))
    Couleur = [vert, bleu, violet, noir, jaune, rouge, blanc]

    cube1 = robot.world.get_light_cube(LightCube1Id)  # looks like a paperclip
    cube2 = robot.world.get_light_cube(LightCube2Id)  # looks like a lamp / heart
    cube3 = robot.world.get_light_cube(LightCube3Id)  # looks like the letters 'ab' over 'T'

    a = True
    b = True
    c = True

    if cube1 is not None and cube2 is not None and cube3 is not None:
        for y in range (10):
            for i in range (7):
                if cube1.last_tapped_time:
                    cube1.last_tapped_time = ""
                    couleurcube1 = cozmo.lights.Light(on_color=(Couleur[i]))
                    cube1.set_lights(couleurcube1)
                    verif1 = i
                    a = False
                #endif
                if cube2.last_tapped_time:
                    cube2.last_tapped_time = ""
                    couleurcube2 = cozmo.lights.Light(on_color=(Couleur[i]))
                    cube2.set_lights(couleurcube2)
                    verif2 = i
                    b = False
                #endif
                if cube3.last_tapped_time:
                    cube3.last_tapped_time = ""
                    couleurcube3 = cozmo.lights.Light(on_color=(Couleur[i]))
                    cube3.set_lights(couleurcube3)
                    verif3 = i
                    c = False
                #endif
                if a == True:
                    changementCouleur(robot, 1, i)
                #endif
                time.sleep(0.1)
                if b == True:
                    changementCouleur(robot, 2, i)
                #endif
                time.sleep(0.1)
                if c == True:
                    changementCouleur(robot, 3, i)
                #endif
                time.sleep(0.1)

                if (a == False and b == False and c == False):
                    if (verif1 == verif2 and verif1 == verif3 and verif2 == verif3):
                        robot.say_text("Oui bien jouer").wait_for_completed()
                    else:
                        print('dommage')
                        #robot.say_text("tu es nul").wait_for_completed()
                    #endif
                #endif
            #endfor
        #endfor
    else:
        cozmo.logger.warning("Cube 1 pas connecté.")
        robot.say_text("Je ne trouve pas le premier cube").wait_for_completed()

cozmo.run_program(cozmo_program)
