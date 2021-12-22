def give_name():
    name_local = input('Name your hero: ')
    return name_local


name = give_name()


def play_again():
    choice = input('Do you wish to play again? (type "yes" or "no")')
    if choice == 'yes':
        main()
    else:
        exit()


def start():
    print('You wake up in a dark room. You don\'t know where you are. \n Why are you here?')
    print('"Oh yes. My friend is in danger. I must find her!" you recall.')
    print('Suddenly, you feel chilly. The Darkness around you seems to \n leech the air that you breathe.')
    print('"I must get out of here or I\'m gonna be consumed" you think.')
    print('You stand up and look around. There are two doors - the left \n and the right one.')
    print('"Which one should I choose?" you wonder.')
    choice = int(input('Left (type "1") or right (type "2")?'))
    if choice == 1:
        stairs()
    elif choice == 2:
        monster_room()
    else:
        print('You couldn\'t choose where to go. It\'s getting harder to breathe...')
        reason = 'The Darkness consumed you.'
        game_over(reason)


def stairs():
    print('When you open the door you see a devastated stone stairs. \n They don\'t look very stable. '
          'Also, there are some cracked spaces \n on the way. However, maybe the stairs might withstand?...')
    choice = input('Use the stairs? (type "yes" or "no")')
    if choice == 'yes':
        print('The stairs suddenly collapse under your weight!')
        reason = 'You fell into abyss.'
        game_over(reason)
    elif choice == 'no':
        print('"There must be another way. Maybe I should look around." you think.')
        choice2 = input('Look around? (type "yes" or "no")')
        if choice2 == 'yes':
            print('You may try to jump over the cracks. On the other hand, you notice \n'
                  'a line hanging down next ro the stairs. It looks quite old and worn.')
            choice3 = int(input('Jump (type "1") or use the line (type "2")?'))
            if choice3 == 1:
                print('That was a bad decision.')
                reason = 'You fell into abyss'
                game_over(reason)
            elif choice3 == 2:
                print('You reach the bottom and find a door. You enter to the next room.')
                prison()
        elif choice2 == 'no':
            print('You go back to the dark room. The dark creature fortunately is not here.')
            print('Suddenly, you feel dizzy. Your sight gets hazy. You fell on the ground...')
            start()
        else:
            print('You couldn\'t decide what to do. It\'s getting harder to breathe...')
            reason = 'The Darkness consumed you.'
            game_over(reason)
    else:
        print('You couldn\'t decide what to do. It\'s getting harder to breathe...')
        reason = 'The Darkness consumed you.'
        game_over(reason)


def monster_room():
    print('You enter the room and see a huge monster at the center. It \n seems to be asleep.')
    print('"Maybe I should get rid of this monster while it\'s asleep? \n It may be problematic later '
          'when it wakes up" a though appeared \n in your head.')
    choice = int(input('Attack the monster (type "1") or try to quietly pass (type "2")?'))
    if choice == 1:
        print('You take a chance and attack the monster, inflicting a wound. \n The monster '
              'wakes up momentarily and quickly throwing off the \n surprise it charges towards '
              'you. It moves so fast that you \n have no time to guard.')
        reason = 'The monster ripped out your heart.'
        game_over(reason)
    elif choice == 2:
        print('"Nah, it\'s not worth it." you think. You quietly advance through \n the room. '
              'The monster seems to be still asleep as you reach \n the next door.')
        prison()
    else:
        print('You wondered so long that the monster wakes up. As soon as it \n notices you, '
              'it charges towards you. It moves so fast that you \n have no time to guard.')
        reason = 'The monster ripped out your heart.'
        game_over(reason)


def first_choice():
    bottle_local = False
    print('You enter a room with cells. "It looks like a prison" you think.')
    print('You wander a while in the corridors. Most of cells are empty, \n in some you notice human skeletons.')
    print('"What a horrible place to be in" you presume.')
    print('"Who\'s there?" you suddenly hear a faint voice. You quickly look \n'
          'around and see that there is a live prisoner in one of the cells. \n'
          'He looks miserable and weak now, but guessing from his physique it \n'
          'seems that he used to be a muscular man.')
    print('"Hey you. You\'re not a guard, are you? Please, get me out \n of here! I\'m innocent! '
          'Look, the key to the cell is right there" \n he points behind you back. The key is indeed '
          'hanging on a \n spike on the wall.')
    choice = str(input('Should you free the prisoner? (type "yes" or "no")'))
    if choice == 'yes':
        print('"Nobody should stay here." you think while taking the key to \n the cell. '
              'You open the door. The prisoner looks surprised and thankful.')
        print('"Thank you, kind sir. I\'m not gonna forget this! It may not be much,\n but '
              'please take this bottle. It\'s a potion that release you \n from poison. Maybe '
              'you\'ll find it useful. Farewell!" he says \n while bowing his head slightly.')
        print('The prisoner leaves quickly. You put the bottle into your pocket.')
        bottle_local = True
        return bottle_local
    elif choice == 'no':
        print('"Why should I free this man? He probably bluffs about his innocence. \n What '
              'if he\'s a dangerous inmate who will take advantage of my \n kindness? I can\'t '
              'waste time here. My friend needs my help!" \n you think and quickly go further '
              'into the labyrinth of cells. \n The prisoner seems depressed as you leave.')
        bottle_local = False
        return bottle_local
    else:
        print('You couldn\'t decide what to do. It\'s getting harder to breathe...')
        reason = 'The Darkness consumed you.'
        game_over(reason)
    return bottle_local


def second_choice():
    key_local = False
    print('You continue your journey through the prison. Suddenly, you run into a guard.')
    print('"Who are you?! Surrender!" he shouts.')
    choice = int(input('Should you fight (type "1") or try to escape (type "2")?'))
    if choice == 1:
        print('You notice a metal pipe lying nearby. You take a chance in \n a fight with the guard!')
        print('The guard doesn\'t seem to be very bright. You manage to get him down.')
        print('As soon as he is disarmed, the guard shouts "Have mercy! \n I have a wife '
              'and a child to feed. I don\'t want to be here either!"')
        choice2 = input('Should you spare the guard? (type "yes" or "no")')
        if choice2 == 'yes':
            print('You decide to spare the guard. He looks shocked. He stands up slowly.')
            print('"I don\'t know what to say... Thank you" he stutters.')
            print('"My friend... She is held captive here" you say.')
            print('The guard quickly looks around and starts to poke in his sack.\n '
                  'Finally, he pulls out a bronze key.')
            print('"Take it" he whispers and gives you the key. He turns his back on you.')
            print('"I haven\'t seen anyone." he says and leaves into the labyrinth.')
            print('You put the key into your pocket. It\'s time to move.')
            key_local = True
            return key_local
        elif choice2 == 'no':
            print('You decide to silence the guard permanently. You take guard\'s \n sword '
                  'lying nearby. The blade quickly slices guard\'s throat. \n The guard tries '
                  'to gasp some air, but ultimately he succumbs. \n You move his lifeless body '
                  'in an open empty cell.')
            print('Suddenly, you hear voices approaching. You have no time to search \n the '
                  'guard. You move quickly further into the labyrinth.')
            key_local = False
            return key_local
        else:
            print('You wonder for so long, that the guard takes a chance to get \n his sword. '
                  'He wails and quickly spikes you with the sword.')
            reason = 'You bleed out.'
            game_over(reason)
        return key_local
    elif choice == 2:
        print('You try to escape the guard. He shouts after you and begins \n to pursue. '
              'He\'s quick, you can feel that he\'s right behind \n you. The next turn you '
              'take you meet a dead end. You gasp in \n desperation, but the next moment you '
              'feel a sword spiking you \n through your guts.')
        reason = 'You bleed out.'
        game_over(reason)
    else:
        print('You wondered so long that the guard takes you down. You are \n thrown into '
              'a cell. As soon as he leaves, you feel that it\'s \n getting harder to breathe...')
        reason = 'The Darkness consumed you.'
        game_over(reason)
    return key_local


def prison():
    bottle = first_choice()
    key = second_choice()
    if bottle is True:
        if key is True:
            basement(bottle=True, key=True)
        else:
            basement(bottle=True, key=False)
    else:
        if key is True:
            basement(bottle=False, key=True)
        else:
            basement(bottle=False, key=False)


def basement(bottle, key):
    print('You finally reach a door that is not a cell door. You cautiously \n '
          'open the door and enter the next room. You see only one cell here. ')
    print('"' + name + '!" somebody calls your name.')
    print('You turn towards the source of voice. It\'s your friend...')
    print('"Ann..." you share a tear when you see her poor condition. \n Her golden hair '
          'has been cut, her face seems dry, she\'s skinny...')
    choice = int(input('Should you get closer quickly (type "1") or slowly (type "2")?'))
    if choice == 1:
        print('You rush towards the cell. Unfortunately, you haven\'t noticed \n that a '
              'tile on your way looks a little different than others. \n You pressed some '
              'mechanism. Suddenly, you hear a swish and your \n friend\'s cry. When you get '
              'to the cell, you notice that Ann \n is quickly getting purple.')
        print('"Poison..." she gasps.')
        if bottle is True:
            print('Thoughts run through your mind in the speed of light. "The \n bottle!" '
                  'it reaches you.')
            print('You give Ann the bottle. "Drink it, quickly!" you insist. \n She barely '
                  'manages to empty the bottle. She breathes deeply for \n a minute and then '
                  'the purple color goes off her face.')
            print('"Thank you, ' + name + '..." she whispers faintly.')
            print('You feel relieved. Now you can think how to get Ann out of here.')
            if key is True:
                print('You try to unlock the cell using the bronze key. It works!')
                print('"Ann, come with me. Use my shoulder" you say.')
                print('Ann smiles weakly and both of you exit the room. After some time \n '
                      'you manage to reach the exit.')
                message = 'You take a deep breath as you get outside. \n "It\'s gonna be ok" ' \
                          'you think.'
                happy_end(message)
            else:
                print('"How do I get her out?" you think looking around.')
                print('You desperately try to find a way to open the cell. You still \n have the metal '
                      'pipe from prison, which you use in your attempt \n to open the cell. After some '
                      'struggle you manage to break the \n lock. However, you make a lot of noise and '
                      'two guards appear quickly.')
                print('"Hold! Don\'t move!" one of guards yells.')
                print('The metal pipe is useless after breaking the lock. You have no \n means to defend. '
                      'The guards apprehend you and throw you to a dark cell.')
                print('"Stay here, you scum!" they shout and leave laughing.')
                print('...')
                print('"Well, well" you hear a sinister thin voice "So you are weak. \n Well, weak people '
                      'are also tasty" it cackles.')
                print('It\'s getting harder to breathe...')
                message = 'The Darkness consumed you. Behold eternal pain...'
                sad_end(message)
        else:
            if key is True:
                print('You quickly get the bronze key out of your pocket. You struggle \n with the '
                      'lock as your hands are shaking. Finally, you open the cell \n and grasp Ann '
                      'into your arms.')
                print('"No... Please, Ann... Don\'t go..." you sob as Ann foam appears on her mouth.')
                print('Few minutes later her body shudders and subsides.')
                print('...')
                print('The only thing you feel is despair.')
                print('...')
                print('"Splendid..." you hear a sinister thin voice "Your despair is \n mine" it cackles.')
                print('It\'s getting harder to breathe...')
                message = 'The Darkness consumed you. Behold eternal pain...'
                sad_end(message)
            else:
                print('You desperately try to break the lock using the metal pipe. \n However, before '
                      'you manage to do so, Ann is lying lifelessly \n on the ground. Before you are '
                      'able to open the cell doors two \n guards are lured by the noise.')
                print('"Hold! Don\'t move!" one of guards yells.')
                print('You ignore the guards and still try to break the lock. The guards \n don\'t wait '
                      'until you break in. They apprehend you and throw \n you to a dark cell.')
                print('"Stay here, you scum!" they shout and leave laughing.')
                print('...')
                print('"Well, well" you hear a sinister thin voice "So you are weak. Well, \n weak people '
                      'are also tasty" it cackles.')
                print('It\'s getting harder to breathe...')
                message = 'The Darkness consumed you. Behold eternal pain...'
                sad_end(message)
    elif choice == 2:
        print('You approach cautiously. Looking around you notice that one \n of tiles looks different. '
              'You skip the slab. You cautiously \n approach Ann\'s cell.')
        print('"Are you all right?" you ask quietly.')
        print('"I\'m good." she replies "I\'m only a little weakened"')
        if key is True:
            print('You try to unlock the cell using the bronze key. It works!')
            print('"Ann, come with me. Use my shoulder" you say.')
            print('Ann smiles weakly and both of you exit the room. After some \n time you '
                  'manage to reach the exit.')
            message = 'You take a deep breath as you get outside. "It\'s gonna be \n ok" you think.'
            happy_end(message)
        else:
            print('You desperately try to find a way to open the cell. You still \n have the metal '
                  'pipe from prison, which you use in your attempt \n to open the cell. After some '
                  'struggle you manage to break the \n lock. However, you make a lot of noise and two '
                  'guards appear quickly.')
            print('"Hold! Don\'t move!" one of guards yells.')
            print('You open the cell doors and the moment you enter, the other \n guard shoot a bolt '
                  'from his crossbow. Before you can do anything, \n you find yourself holding Ann. '
                  'Blood is pouring from her chest \n where the bolt landed.')
            print('"Ann!" you cry.')
            print('She smiles weakly and whispers: "I\'m glad... You\'re ok...".')
            print('Suddenly, her body shudders and subsides.')
            print('...')
            print('"...What...?" you stammer in shock. You feel anger flowing through you.')
            print('"Get up, you scum!" you hear a guard\'s shout. You stand up \n and everything '
                  'turns black.')
            print('...')
            print('The next moment you snap out you stand in the pool of blood. \n There are at '
                  'least ten guards lying at your feet. The air is \n filled with the smell of blood. '
                  'The only thing you feel is despair.')
            print('"Splendid..." you hear a sinister thin voice "Your anger is mine" it cackles.')
            print('It\'s getting harder to breathe...')
            message = 'The Darkness consumed you. Behold eternal pain...'
            sad_end(message)
    else:
        print('You spend too much time on wondering. Suddenly, it\'s getting harder to breathe...')
        reason = 'The Darkness consumed you.'
        game_over(reason)


def game_over(reason):
    print(reason)
    print('GAME OVER')
    play_again()


def happy_end(message):
    print(message)
    print('HAPPY END')


def sad_end(message):
    print(message)
    print('SAD END')


def main():
    start()


if __name__ == '__main__':
    main()
