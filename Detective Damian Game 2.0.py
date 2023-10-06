#Dective Damian Game

#Game Check
#Intro
import time

#Varibles

wifeFN = 'Stacy'
wifeLN = 'Montgommery'
mistressFN = 'Marilyn'
mistressLN = 'Martin'
officerFN = 'Arthur'
officerLN = 'Dolye'
lawyerFN = 'John'
lawyerLN = 'Ghotti'
workerFN = 'Tom'
workerLN = 'Fox'
player_name = 'Dollar'
Lawyer = "John Gotti"
Detective = "Damian Dollar"
trust = 0
questioned_tom = 0
tom_spouse = 0
Evidence = {'Dectectives Badge','Trench Coat'}
self_accusation = 0
sweets = False
killerCorrect = False 
poisonMediumCorrect = False 
poisonSellerCorrect = False
motiveCorrect = False
poisonApplierCorrect = False
poison_found = False




def sleep_line(message):
    print(f"{message}")
    time.sleep(2.1)
sleep_line("'''''''''''''''''''''''''''''''''''''''''''''")
sleep_line("The Stuckupshire Times has reported that the death of a local businessman and philanthropist, Charles Montgomery.")
sleep_line("The deceased Montgomery was found dead in his bed at roughly 5am this morning.")
sleep_line("The police have declared the death was a murder because of a note left on a desk in the police station. \nThe note simply said that 'Charles Montgomery was murdered.'")
sleep_line("The opulent mansion where Mr Montgomery lived has been declared a crime scence, and the police are investigating it now.")
sleep_line("Something fishy is going on however. It seems like they need some, shall we say, outside perspective...")
sleep_line("'''''''''''''''''''''''''''''''''''''''''''''")

def dialogue(character, message, delay=1):
    print(f"{character}: {message}")
    time.sleep(3)


dialogue("???","You are Detective Damian Dollar, a seasoned investigator known for solving complex cases.")
dialogue("???","One gloomy evening, rain pooring down in buckets, threatening to drown even the local clock tower, you are sitting, waiting for the ringing you know is coming.")
dialogue("???","You receive a call from an old friend.")


dialogue("Captain", "Dective Dollar, we've got a murder at the Montgomery Mansion.")
dialogue(player_name, "I told you sir, that you don't have to call me that anymore.")
dialogue("Captain", "And you don't have to call me sir anymore. But enough chat, I need you, at least this once. I'm calling in a favour")
dialogue(player_name, "Last I checked, you owed me some favours, not the other way around. ")
dialogue("Captain", "For me then. As a friend.")
dialogue(player_name, "... Got it. I'll head on over")
dialogue(player_name, "You grab your coat and badge and head to the scene, ready to unravel the mystery and seek justice.")
print('[Evidence Acquired - Trench Coat]')
print('[Evidence Acquired - Detective\'s Badge]')
time.sleep(2)


def dialogue(character, message, delay=1):
    print(f"{character}: {message}")
    time.sleep(3)  

print('You arrive, soaked and freezing at the Montgommery Mansion. It\'s extravagant, but in the rain and gloomy weather, looks colourless and drained.')
time.sleep(3)
print(f'There are a few on-duty officers, rookies doing the basic stuff, all around the entrance. One runs over and lets you know that Officer {officerLN} is inside, and can brief you')
time.sleep(3)
print(f'They also let you know that the other witnesses are inside, waiting for questioning.')
time.sleep(3)
print(f'The wife {wifeFN} {wifeLN}, is inside and waiting for answers')
time.sleep(3)
print(f'Charles Montgommery\'s business partner, Mr Martin, hasn\'t arrived yet, but his wife, Mrs. {mistressLN} has, and is in a bad state.')
time.sleep(3)
print(f'Charles\'s lawyer, John Ghotti, who was a close associate of the victim, needs to be questioned as well.')
time.sleep(3)
print(f'In addition, one of the workers, Tom Fox, in the mansion seems to have been brought in for questioning. They may know something.')
time.sleep(3)
print('You step into the central foyer, and glance around. Some of the witnesses are here, but there are others around the mansion. What should I do first')
time.sleep(3)
def tutorial():
    print('You must interrgoate and question the people inside the mansion, gathering clues and evidence until you are ready to make a final deduction.')
    time.sleep(3)
    print('When presenting evidence, please type it exactly as written')
    time.sleep (2)

tutorial()


def menu():
    print("Please select one of these options to proceed.")
    print("1. Find Arthur\n2. Talk to Stacy\n3. Speak to Marylin\n4. Speak to the Lawyer\n5. Find Tom\n6. View the Evidence\n7. Accuse Suspect\n8. Repeat the tutorial.")
    menuM = True
    while menuM == True:
        menu_selection = input("Select one of these options to proceed: ")
        if menu_selection == "1":
            menuM = False
            officer()
        elif menu_selection == "2":
            menuM = False
            wifeInterrogation()
        elif menu_selection == "3":
            menuM = False
            mistressInterrogation(mistressFN,mistressLN)
        elif menu_selection == "4":
            menuM = False
            lawyer_questioning()
        elif menu_selection == "5":
            menuM = False
            tom()
        elif menu_selection == "6":
            evidenceFun()
        elif menu_selection == "7":
            endgame = int(input('Are you sure you want to do this? There is no turning back?\n1. Yes\n2. No\n'))
            if endgame == 1:
                menuM = False
                theAccusation()
            elif endgame == 2:
                print('Gather more clue\'s, and we\'ll catch the true killer yet')
                time.sleep(2)
            else:
                print('Hmm. You seem unsure. We\'ll put you back, just in case')
                time.sleep(2)
        elif menu_selection == "8":
            tutorial()
        else:
            print("Please use a valid option.")



def evidenceFun():
    print((f'My current evidence is:'))
    for x in Evidence:
        print(x)
        time.sleep(0.5)

def mistressInterrogation(mistressFN,mistressLN):
    mistressMood = 3
    print(f'I approach a scared looking girl, sat in one of the tea rooms with another officer, and quickly nod for him to leave.')
    time.sleep(3)
    print(f'She seems to be shivering in from the cold rain, and despite this she is wearing a dry fur coat. This must his business partners wife, {mistressFN} {mistressLN}.')
    time.sleep(3)
    print('It is clear that something has got her scared, as her eyes dart around the room.\nShe may take some careful interragation tactics to give up the answers I need.')
    time.sleep(5)
    print(f'"Well Ms. {mistressLN}, I see you arrived here quite quickly. I appricieate your co-operation with us, I just need to ask you a few questions."')
    time.sleep(3)
    print('"..."')
    time.sleep(2)
    print('"Miss?"')
    time.sleep(2)
    print('"I understand."')
    time.sleep(2)
    interragation = True
    while interragation == True:
        questions = int (input('What line of questioning shall I go down first\n1. Act of the murder\n2. Motive of the murder\n3. Alibi for the murder\n4. End the Conversation\n'))
        if questions == 1:
            murderInterragtion = True
            print('"I should question her about the act of the murder."')
            time.sleep(2)
            print('He died from posion it appears, so I need to find out if she knows anything about it, or if she had the chance to apply it any point.')
            time.sleep(2)
            print('"It appears that the the victim suffered from some kind of alergic attack or posion."')
            time.sleep(3)
            print('"Oh my word...!"')
            time.sleep(2)
            while murderInterragtion == True:
                murderIntial = True
                MMurderQuestions = int(input('1. Would you happpen to know if he suffered from any ailments, or that that he hid from others?\n2. Had he eaten or taken anything unusual recently \n3. Your husband has dealings in dangerous chemicals, Does he not? You wouldn\'t happen to know anything about that would you?\n4. Do I have any evidence I can show her?\n5. Stop this line of questions.\n'))
                if MMurderQuestions ==  1:
                    print ('"Oh, um... I think..."')
                    time.sleep(2)
                    print('She glances to the side, but I can\'t tell at what.')
                    time.sleep(3)
                    print('"I think had developed a heart condition called..."')
                    time.sleep(2)
                    print('Her eyes dart again, to inside the jacket this time.')
                    time.sleep(3)
                    print('"Broncha... something. I don\'t remember its name in particular.')
                    time.sleep(2)
                    print('Hmm. Why wouldn\'t she remember that? Odd.')
                    Evidence.add('Misrembered Heart Condition')
                    print ('[Added "Misrembered Heart Condition" to evidence]')
                    time.sleep(5)
                    mistressLieCaught = True
                elif MMurderQuestions == 2:
                    print('Oh um... I uh... bought some foreign sweets about a week ago, on a business trip. I forgot to give them to him when we got back. So I came over and handed them to him yesterday..."')
                    time.sleep(4)
                    print('"but I shouldn\'t think..."')
                    time.sleep(2)
                    Evidence.add('Exotic Sweets')
                    time.sleep(2)
                    print('That seems like something I should inquire about...')
                    print ('[Added "Exotic Sweets" to evidence]')
                    global sweets
                    sweets = True
                    time.sleep(5)
                elif MMurderQuestions == 3:
                    print ('"Yes, we do... but what does that have to do with anything?"')
                    time.sleep(2)
                    print ('"Mr Montogommery wasn\'t involved in any of that. Besides, you need to fill out a huge form to take anything from those anywhere near the site."')
                    time.sleep(2)
                    Evidence.add('Chemical Forms')
                    print ('It seems like she doesn\'t know enough. I wonder if she might know who does though?')
                    print ('[Added "Chemical Forms" to evidence]')
                    time.sleep(5)
                elif MMurderQuestions == 4:
                    print('If I can present any of my evidence, that contradicts one of her statements about the posion, now would be the time')
                    time.sleep(2)
                    print((f'My current evidence is:'))
                    for x in Evidence:
                        print(x)
                        time.sleep(0.5)
                    MMurderEvidence = str(input('Do I have anything for this?\n'))
                    if MMurderEvidence == 'Misremembered Heart Condition':
                        print(f'"So, Mrs {mistressLN}, you have heard about this unheard of heart condition?"')
                        time.sleep(2)
                        print(f'"Well, I mean... Mrs {wifeLN}... she mentioned it too me... I think only she knew"')
                        time.sleep(2)
                        Evidence.remove('Misremembered Heart Condition')
                        print ('I don\'t think that\'ll be relevant anymore')
                        print ('[Evidence Removed - Misrememebered Heart Condition]')
                        time.sleep(2)
                    elif MMurderEvidence == 'Exotic Sweets':
                        print (f'"These sweets, why were they so important that you would take time out of your day to deliver them to him?"')
                        time.sleep(2)
                        print (f'"Well they were his favourite and his wif-... I mean, I thought that maybe it would cheer him up after he and Mrs.{wifeLN} had a fight')
                        time.sleep(2)
                        print ('Hmm. Maybe he and his wife were having trouble.')
                        print ('[Added Evidence - \'Domestic Issues\']')
                        Evidence.add('Domestic Issues')
                        time.sleep(5)
                    elif MMurderEvidence == 'Chemical Forms':
                        print (f'"These forms and these chemicals, who would be able to move them?"')
                        time.sleep(2)
                        print (f'"Well, I there\'s a few people, for example, Mr. {workerLN} over there can do it, he works a second job at our business."')
                        time.sleep(2)
                        print (f'Maybe I should confront {workerFN} {workerLN} about about this...')
                        time.sleep(4)
                    elif MMurderEvidence == 'Trench Coat' and mistressLieCaught == True:
                        print ('Please, take my Trench Coat. It\'s much warmer than that one..."')
                        time.sleep(2)
                        print ('"Wait you can\'t..." You snatch the coat from her and give her your own.')
                        time.sleep(2)
                        print ('Her coat is beautiful and made of expensive white fur, but inside one of the pockets, appears to be small little script, with pre-prepared answers on it.')
                        print ('[Evidence Acquired - Mistress\'s Script]')
                        print ('[Evidence Removed - Trench Coat]')
                        Evidence.add('Mistress\'s Script')
                        Evidence.remove('Trench Coat')
                        time.sleep(6)
                        if mistressMood >= 1:
                            mistressMood = mistressMood - 1
                    elif MMurderEvidence == 'Mistress\'s Script' and mistressMood >= 3:
                        print(f'"Okay okay. I\'ll tell you.\nMrs.{wifeLN}, she\'s blackmailing me."')
                        time.sleep(3)
                        print(f'"She caught me and her husband in an affair, and will tell everyone if I didn\'t do what she says."')
                        time.sleep(2)
                        print('She just told me to deliever that box of sweets was all!')
                        time.sleep(2)
                        print('Hmmm. This will be very useful. Maybe I should tell The Sun...')
                        print ('[Evidence Acquired - Blackmail]')
                        print ('[Evidence Removed - Mistress\'s Script')
                        Evidence.remove('Mistress\'s Script')
                        Evidence.add('Blackmail')
                        time.sleep(5)
                    elif MMurderEvidence == 'Mistress\'s Script' and mistressMood <= 3:
                        print('"I have no idea what your talking about"')
                        time.sleep(2)
                        print('Maybe if I improve her mood a little more, I could get her to fess up about the script...')
                        time.sleep(2)
                    elif MMurderEvidence == 'Detective Badge':
                        print ('"That\'s a very nice badge"')
                        time.sleep(2)
                        print('"Thank you Miss"')
                        time.sleep(2)('"So why are you showing it to me?"')
                        print ('"I worked very hard for this badge. Bought a Trench Coat and everything"')
                        time.sleep(2)
                        print ('"..."\n')
                        time.sleep(2)
                        if mistressMood >= 1:
                            mistressMood = mistressMood - 1
                    else:
                        print ('I don\'t think that\'s relevant here')
                        time.sleep(2)
                elif MMurderQuestions == 5:
                    print('I\'ll stop this line of questioning')
                    murderInterragtion = False
                    time.sleep(2)
                else:
                    print('[Please input the number option]')
                    time.sleep(2)
        elif questions == 2:
            motiveInterragation = True
            print ('I should question her about her motive. She and her husband were business partners with the victim, and both couples met regularly. Although, there is something here I dont\'t think I\'m seeing')
            time.sleep(5)
            while motiveInterragation == True:
                MMotiveQuestions = int(input('1.You got here pretty quickly, but I don\'t see your husband about. Where might he be, what with his business partner dead?\n2.You seem to be quite shook up. What\'s bothering you?\n3.Had the victim, Charles, ever slighted you?\n4. Do I have any evidence I can show her?\n5.Stop this line of questions.\n'))
                if MMotiveQuestions == 1:
                    print('"Well of course. I mean, he was a good friend, and I couldn\'t bare to think he had passed away. My husband will be here after work today. Apparently the world of business does not stop turning even for the death of a great man...*sniff*"')
                    time.sleep(5)
                    print('She seems to admire the victim very much. Maybe a little too much...')
                    print ('[Evidence Acquired - Admiration of Charles]')
                    Evidence.add('Admiration of Charles')
                    time.sleep(5)
                elif MMotiveQuestions == 2 and mistressMood <= 3:
                    print('"We were close, we worked together for a long time. Even after... no I shouldn\'t say anything"')
                    time.sleep(2)
                    print('Maybe if I improve her mood a little more...')
                    time.sleep(2)
                elif MMotiveQuestions == 2 and mistressMood >= 4:
                    print(f'Well me and Charles were close... And whenever Mrs.{wifeLN} would see us, she would always become enraged. She once... Well let\'s just say there was an incident. I Just worry that maybe something awful happened..."')
                    time.sleep(5)
                    print('(They were clearly having some kind of romantic affair. Maybe I shouldn\'t pry but...)')
                    print ('[Evidence Acquired - Secret Affair]')
                    Evidence.add('Secret Affair')
                    time.sleep(5)
                elif MMotiveQuestions == 3:
                    print('"Charles? No, No, No, not at all. Me and his wife sometimes get into a childish spat, but it\'s never... well it never got out of hand. We uh..., got everything under control.')
                    time.sleep(4)
                    print('(It seems that something is up, but I don\'t think I should press this issue, at least right now futher. Maybe there\'s another line of questioning)')
                    time.sleep(3)
                elif MMotiveQuestions == 4:
                    print('If I have anything I think contradicts her motives\'s, I should bring it up now')
                    time.sleep(2)
                    print((f'My current evidence is:'))
                    for x in Evidence:
                        print(x)
                        time.sleep(0.5)
                    MMotiveEvidence = str(input('Do I have anything for this?\n'))
                    if MMotiveEvidence == 'Admiration of Charles':
                        print('"You admire Charles a great deal it seems"')
                        time.sleep(2)
                        print('"Yes, detective. He was a great philantrophist, and I have know him since we were both children. I wasn\'t able to win him over until... after his current wife had already done so.')
                        time.sleep(4)
                        print('That\'s nothing I don\'t already know. But she seems a bit happier after talking about him')
                        if mistressMood <= 5:
                            mistressMood = mistressMood + 1
                        print ('[Evidence removed - Admiration of Charles]')
                        Evidence.remove('Admiration of Charles')
                        time.sleep(3)
                        #This does loop allow for a loop to gain infinite mood with the Mistress, which for now is intentional
                    elif MMotiveEvidence == 'Secret Affair':
                        print('"It really does seem to me like you two had something going on that went a little bit deeper..."')
                        time.sleep(2)
                        print('"What? That\'s perpostourous! We never had anything of the sort! How dare you!')
                        time.sleep(2)
                        print('Directly accusing her of having affair does seem to be a bit of a sore spot...')
                        if mistressMood >= 1:
                            mistressMood = mistressMood - 1
                        Evidence.remove('Secret Affair')
                        time.sleep(2)
                        print('Evidence')
                    elif MMotiveEvidence == 'Detective Badge':
                        print ('"That\'s a very nice badge"')
                        time.sleep(2)
                        print('"Thank you Miss"')
                        time.sleep(2)('"So why are you showing it to me?"')
                        print ('"I worked very hard for this badge. Bought a Trench Coat and everything"')
                        time.sleep(2)
                        print ('"..."\n')
                        time.sleep(2)
                        if mistressMood >= 1:
                            mistressMood = mistressMood - 1
                    else:
                        print('I don\'t think that\'s relevant right now')
                        time.sleep(2)
                elif MMotiveQuestions == 5:
                    print('I\'ll stop this line of questioning')
                    motiveInterragation = False
                    time.sleep(2)
                else:
                    ('Please input a valid option')
                    time.sleep(2)
        elif questions == 3:
            alibi_Interragation = True
            print ('I should question her alibi. She says she visited the day before, maybe there\' something in that I can pick up')
            time.sleep(2)
            while alibi_Interragation == True:
                MAlibiQuestions = int(input('1. You visited the Montgommery Mansion to speak to Charkes yesterday, correct? What did you do before then?\n2. What did you and Charles talk about? Had he said anything, or did he seem worried when you last spoke to him? \n3.What did you do afterwards?\n4. Do I have any evidence I can show her?\n5.Stop this line of questions.\n'))
                if MAlibiQuestions == 1:
                    print('"I don\'t think that I did anything particualrly important. I saw Tom around the garden, but I believe he is currently working for the Montgommery\'s. He did seem a little worried about something, but I didn\'t think anything of it')
                    time.sleep(5)
                    print('If Tom know\'s anything, I should question him')
                    time.sleep(2)
                elif MAlibiQuestions == 2:
                    print('"Well, he seemed quite calm. Apparenltly he and his wife had just settled an arguement apparently. She always complains about money and such."')
                    time.sleep(2)
                    print('"Money? It thought they were quite well off?"')
                    time.sleep(2)
                    print('"Yes, but there appears to have been some issue with the will or something')
                    time.sleep(2)
                    print('"Hmmm. I wonder if the lawyer would know anything about that?')
                    time.sleep(2)
                elif MAlibiQuestions == 3:
                    print('"Well, I had to grab something from the garden, you see I uh... Dropped my wedding ring outside the last time I was here. It was the main reason I came over despite the weather')
                    time.sleep(4)
                    print('Eh? That seems suspicious? I should question that more')
                    Evidence.add('Wedding Ring')
                    print('[Evidence Acquired - Wedding Ring')
                    time.sleep(4)
                elif MAlibiQuestions == 4:
                    print('If I have anything I think contradicts her motives\'s, I should bring it up now')
                    time.sleep(2)
                    print((f'My current evidence is:'))
                    for x in Evidence:
                        print(x)
                        time.sleep(0.5)
                    MAlibiEvidence = str(input('Do I have anything for this?\n'))
                    if MAlibiEvidence == 'Wedding Ring':
                        print('"This wedding ring... you dropped it in the garden?"')
                        time.sleep(2)
                        print('"Yes?"')
                        time.sleep(1.5)
                        print('"That must have been worrying"')
                        time.sleep(2)
                        print(f'Yeah, it was. I also saw Mrs.{wifeLN}, she seemed to be burying something there...')
                        time.sleep(2)
                        print('She might have been hiding something important. I should question the wife about this.')
                        print ('[Evidence removed - Wedding Ring]')
                        print ('[Evidence Acquired - Burying in the garden]')
                        Evidence.remove('Wedding Ring')
                        Evidence.add('Burying in the garden')
                        time.sleep(5)
                    elif MAlibiEvidence == 'Detective Badge':
                        print ('"That\'s a very nice badge."')
                        time.sleep(2)
                        print('"Thank you Miss."')
                        time.sleep(2)('"So why are you showing it to me?"')
                        print ('"I worked very hard for this badge. Bought a Trench Coat and everything."')
                        time.sleep(2)
                        print ('"..."\n')
                        time.sleep(2)
                        if mistressMood >= 1:
                            mistressMood = mistressMood - 1
                    else:
                        print('I don\'t think that\'s relevant right now.')
                        time.sleep(2)
                elif MAlibiQuestions == 5:
                    print ('I should stop this line of questioning.')
                    alibi_Interragation = False
                    time.sleep(2)
                else:
                    print('Please input a valid option')
                    time.sleep(1.5)
        elif questions == 4:
            print (f'Goodbye, Mrs. {mistressLN}')
            time.sleep(2)
            interragation = False
            menu()
        else:
            print ('[Please input the number option]')
            time.sleep(2)

def wifeInterrogation():
    print('Speaking to one of the officer\'s, you find that there is a variety sitting rooms, fully kitted out with bookshelves, lighting, ashtrays and alcohol.')
    print('Inside one of these rooms, Stacy Montgommery is sat, simply reading and waiting for interrogation.')

    introLoop = True
    while introLoop == True:
        loopChoice =int(input("1 .Would you like to get Stacy to make a statement? \n2. Would you like to show some evidence \n3. Leave\n"))
        if loopChoice == 1:
            print(f"Mrs. {wifeLN}, could you please give your statement?")
            introLoop = False
        elif loopChoice == 2:
            print('What evidence should I show her?')
            print((f'My current evidence is:'))
            for x in Evidence:
                print(x)
                time.sleep(0.5)
            wifeEvidence = str(input('Do I have anything?\n'))
            if wifeEvidence == 'Rat Posion':
                print('"Now, a worker named Tom Fox says that you knew about his chemical background, and was asking about rat poison?"')
                time.sleep(2)
                print('"I mean I know a lot about my workers. And yes, I may have needed him to kill some rats.')
                time.sleep(2)
                print('"Now that is interesting, because we haven\'t found any traces of rat poison. Except inside your husband.')
                time.sleep(2)
                print('"And no rat poison elsewhere. Odd, isn\'t it?')
                time.sleep(2)
                print('If I can just find what it was used on, I might be able to get more.')
                poison_found = True
            if wifeEvidence == 'Burying in the garden' and poison_found == True:
                print('"You say you were at a Charity event, but we have witness putting you in the garden at around that time, buring in something in there.')
                time.sleep(2)
                print('"I have no idea what your talking about.')
                time.sleep(2)
                print("You might not, but when I sent out a man to look, I found this box of sweets.")
                time.sleep(2)
                print('From your pocket, a box of "Fabolous Flavours of Chupa Chups (Indian Spices)" emerges, covered in mud.')
                time.sleep(2)
                print('"And I should expect then, that you know nothing about these."')
                time.sleep(2)
                print('A look of panic sets in, and she begins shaking. She knows exactly what they are.')
                time.sleep(2)
                print('"And what do you know, traces of rat poison were found all along these.')
                time.sleep(2)
                print('A deathly silence fills the room.')
                time.sleep(2)
                print('Evidence Aquired - Poisoned Exotic Sweets.')
                Evidence.add ('Poisoned Exotic Sweets')
                time.sleep(5)
            if wifeEvidence == 'Hole digging':
                print('"You say you were at a Charity event, but we have witness putting you in the garden at around that time, buring in something in there.')
                time.sleep(2)
                print('"I have no idea what your talking about.')
                time.sleep(2)
                print("Maybe I should put her under a bit of pressure. If I knew what the murder weapon was, I could press for more.")
                time.sleep(5)
            elif wifeEvidence == 'Blackmail':
                print ('"So you were blackmailing Mrs. Martin. She did confess after all."')
                time.sleep(2)
                print ('"She\'s a silly girl isn\'t she? I simply told her to keep her mouth shut about the affair."')
                time.sleep(2)
                print ('"I can\'t let anything call into question the transf- well the normal state of affairs. I have my pride, you know?')
                time.sleep(2)
                print ('I think she\'s trying something. Whatever her motive was, I won\'t get it from her.')

            else:
                print('Hmmm maybe I don\'t have anything...')
                time.sleep(2)
        elif loopChoice == 3:
            print('You return to the entrance')
            time.sleep(2)
            introLoop = False
            menu()
        else:
            print("Pleas einsert a valid input: 1. 2. or 3.")
            time.sleep(2)

        print("Detective: Mrs. Stacy Montgommery, we need to ask you some questions regarding your husband's death.")
        time.sleep(2)
        print("Detective: Your cooperation is crucial in resolving this case. Let's begin.")
        time.sleep(2)
        print("I don't have to know if she's lying yet. I should get her statement, Then return once I have evidence.")

    correct_answers = 0

    print("\nDetective: Where were you on the night of your husband's death?")
    time.sleep(2)
    print("Stacy:I was at a charity event all night.")
    time.sleep(2)
    print("Is Stacy lying about this?")
    time.sleep(2)

    choice1 = int(input("1 = Truth. \n2 = Lie\n"))
    time.sleep(2)
    if choice1 == 1:
        print("That seems to be true")
        time.sleep(2)
    elif choice1 == 2:
        print("Shes's lying, I should bring this up to her later")
        time.sleep(2)
    else:
        print("I can't make a choice yet")
        time.sleep(2)

    print("Detective: Did you have any knowledge of your husband's will and financial matters?")
    time.sleep(2)
    print("Stacy: No, I was not involved in his financial affairs.")
    time.sleep(2)

    choice2 = int(input("1 = Truth. \n2 = Lie"))
    if choice2 == 1:
        print("That seems to be true")
        time.sleep(2)
    elif choice2 == 2:
        print("Hmmm, I don\'t think that\'s true. When she\'s done, I should show some evidence that contradicts that.\n")
        time.sleep(2)
    else:
        print("I can't make a choice yet")
        time.sleep(2)

    print("\nDetective: Did you have any conflicts or disputes with your husband recently?")
    time.sleep(2)
    print("Stacy: Yes, we had arguments about his will and inheritance.")
    time.sleep(2)

    choice3 = int(input("1 = Truth. \n2 = Lie.\n"))
    if choice3 == 1:
        print("That seems to be true")
        time.sleep(2)
        correct_answers += 1
    elif choice3 == 2:
        print("Hmmm, I don\'t think that\'s true. When she\'s done, I should show some evidence that contradicts that.")
        time.sleep(2)
    else:
        print("I can't make a choice yet")
        time.sleep(2)

    print("\nDetective: Were you aware of any other individuals who might have had a motive to harm your husband?")
    time.sleep(2)
    print("Stacy: No, I can't think of anyone.")
    time.sleep(2)

    choice4 = int(input("1 = Truth. \n2 = Lie.\n"))
    if choice4 == 1:
        print("That seems to be true")
        time.sleep(2)
    elif choice4 == 2:
        print("Hmmm, I don\'t think that\'s true. When she\'s done, I should show some evidence that contradicts that.")
        time.sleep(2)
    else:
        print("I can't make a choice yet")
        time.sleep(2)


    print("\nDetective: Did you have access to any poisonous substances in your home?")
    time.sleep(2)
    print("Stacy: No, we didn't have anything like that.")
    time.sleep(2)

    choice5 = input("1 = Truth. \n2 = Lie.\n")
    if choice5 == 1:
        print("That seems to be true.")
        time.sleep(2)
        correct_answers += 1
    elif choice5 == 2:
        print('Hmmm, I don\'t think that\'s true. When she\'s done, I should show some evidence that contradict\'s that.')
        time.sleep(2)
    else:
        print("I can't make a choice yet.")
        time.sleep(2)
    
    print('Hmmm. Once I\'ve gathered some evidence, I should come back and question her.\n')
    time.sleep(2)
    menu()

import time
def sleep_line(message): #This function will be used so after each line, there is a pause.
    print(f"{message}")
    time.sleep(0.7)
# The follwing variables are used so that the officer will say different things and may help depending on if you asked him
asked_officer = 0
questioned_officer = 0
witness_asked = 0
victim_asked = 0

def officer():
    global questioned_officer
    if questioned_officer == 0:
        sleep_line("You have entered a side room in the Montgomery mansion, probably a tea room. or small dining room where there is a officer stood there taking notes.")
        sleep_line("You have approach one of the officers working on this case, Arthur Doyle.")
        sleep_line("He is a middle aged looking man, wearing a brown coat, a policeman's hat and black trousers.")
        sleep_line("Arthur: Hello Detective Damian.")
        sleep_line("Arthur: It's a awful case, isn't it? I'm sure you will hear that many times today.")
        sleep_line("Arthur: I've gathered some information about this case, just ask and I'll tell you what I've found.")
    else:
        sleep_line("You have returned to the room in the Montgomery mansion where Arthur is.")
        sleep_line("Arthur: Hello Damian. Do you have more questions to ask me?")
    ask_question() # Run the ask_question function which is the menu selection for this character

def ask_question():
    global asked_officer
    global questioned_officer
    sleep_line("Press 1 to ask about Arthur. \nPress 2 to ask his view on the suspects. \nPress 3 to ask about Arthur about the murder weapon. \nPress 4 to ask about Arthur about the Victim. \nPress 5 to ask Arthur about the evidence in the case. \nPress 6 to finish asking questions.")
    evidence = input("Enter your choice: ")
    if evidence == "1":
        sleep_line("Arthur: I am the senior officer assigned onto this case.")
        sleep_line("Arthur: I am quite experienced in this job, I've been catching perps for such a long time now.")
        sleep_line("Arthur: But every case is still suprising to me.")
        asked_officer = 1
        sleep_line("Arthur: Is there anything else you need from me?")
        ask_question() # Returning to the ask_question function
    elif evidence == "2":
        sleep_line("Arthur: There are 3 suspects in this case.")
        suspect()
    elif evidence == "3":
        sleep_line("Arthur: The victim appeared to be killed by some poison, all the possible killers could have been anywhere when Mr Montgomery died.")
        sleep_line("Arthur: I hope that was useful information. It shows that anyone could have done it, the motive will help you find the killer, Damian.")
        ask_question()
    elif evidence == "4":
        victim()
    elif evidence == "5":
        case_evidence()
    elif evidence == "6":
        sleep_line("Arthur: It's a strange case, isn't it?")
        if asked_officer == 1: # After the 2 if statements, Arthur will say good luck
            sleep_line("Arthur: This officer job is still suprising everyday.")
        else:
            sleep_line("Arthur: It's going to be a long day.")
        #Keep space between the 2 if statements on this part to make sure that all the code is executed
        sleep_line("Arthur: Good luck Damian, I'll be here all day if you need to speak to me again.")
        sleep_line("You walk out of the room after hearing Arthur's investigation results.")
        questioned_officer = 1
        menu()
        #Enter code to return to selection menu/ Replace this line with the function to return to the main game selection menu
    else:
        sleep_line("Please enter a valid choice using the number keys. ")
        ask_question() # Ask question again because of invalid input

def suspect(): # This whole section can be changed later depending on the story
    global witness_asked
    global asked_officer
    sleep_line("Which suspect would you like to ask Arthur about? \nPress 1 for Marilyn Martin. \nPress 2 for Tom Fox. \nPress 3 for Stacy Montgommery \nPress 4 to finish asking Arthur about the witnesses.")
    victim_choices = input("Enter your choice: ") # The playey's choice will lead to different functions which are the choices that Arthur can answer about.
    if victim_choices == "1":
        sleep_line("Arthur: Marilyn is the wife of the victim\'s business partner, Mr. Martin. Mr Montgomery was a extremely wealthy man.")
        sleep_line("Arthur: If you want to ask me about what I think about her, I do not really trust her. I think she is hiding something. I tried questioning her earlier but Ms Martin came off as too scared. Perhaps you'd have better luck?")
        sleep_line("Arthur: Regarding an alibi, she was outside in the town when the murder occurred, I have not properly questioned her still so you will need to Damian.") 
        sleep_line("Arthur: Anyway, was there something else you wanted to ask me about regarding the witnesses?")
        if asked_officer == 1:
            print("Arthur: I have a strange feeling about her.") # If the player asks about Arthur in the previous section and then asks about Marilyn, he will give a hint.
        witness_asked += 1
        suspect()
    elif victim_choices == "2":
        sleep_line("Arthur: Tom was employed by Mr Montgomery. He was a good servant to the victim, and always got his work done.")
        sleep_line("Arthur: He was nearby, when the victim was murdered. I think he also some relationship with some chemical companies.")
        sleep_line("Arthur: I am not really sure if he has a motive or not, you may need to question him, I was not able to get anything out of him.")
        sleep_line("Arthur: Was there anything else you wanted to ask regarding the witnesses?")
        witness_asked += 1
        suspect()
    elif victim_choices == "3":
        sleep_line("Arthur: Stacy Montgommery is the wife of the victim.")
        sleep_line("Arthur: She was in another part of the mansion when the Mr Montgomery died.") 
        sleep_line("Arthur: I think she may have a motive to murder the victim, but I have yet to figure out what that may be.")
        sleep_line("Arthur: Anyway, was there something else you wanted to ask me about regarding the witnesses?")
        witness_asked += 1
        suspect()
    elif victim_choices == "4":
        if witness_asked == 0:
            sleep_line("Arthur: No questions at all about the victim Damain, Very Well.")
            sleep_line("Arthur: Do you have any other questions to ask me?")
            ask_question() # Returning to the ask_question function
        elif witness_asked > 0 and witness_asked <= 3:
            sleep_line("Arthur: I hope this is enough information.")
            sleep_line("Arthur: Do you have any other questions to ask me?")
            ask_question()
        elif witness_asked > 3:
            sleep_line("Arthur: I've told you a lot of information. I hope it is useful.")
            sleep_line("Arthur: Do you have any other questions to ask me?")
            ask_question()
        else:
            sleep_line("Please enter a valid choice using the number keys. ")
            suspect()
    else:
        sleep_line("Please enter a valid choice using the number keys. ")
        suspect()

def victim():
    global victim_asked
    sleep_line("Arthur: What would you like to ask about the victim?")
    sleep_line("Press 1 to ask about the Victim's recent life. \nPress 2 to ask about his relationship with the suspects. \nPress 3 to finish asking arthur about the Victim.")
    victim_choice = input("Enter your choice: ")
    if victim_choice == "1":
        sleep_line("Arthur: The victim's recent life is quite interesting. He had a wife and a mistress, Stacy Montgommery and Marilyn Martin.")
        sleep_line("Arthur: Mr Montgomery had many business relations. I'm sure you can tell that though due to the size of this mansion.")
        sleep_line("Arthur: Anyway, was there anything else you wanted to ask me about the victim?")
        victim_asked += 1
        victim()
    elif victim_choice == "2":
        sleep_line("Arthur: The victim's relationship with Ms Martin was that she was his mistress.") # Add in code about their relationship
        sleep_line("Arthur: Mrs MOntgommery was married to Mr Montgomery and I think she knew about Ms Martin.") # Enter code about their relationship
        sleep_line("Arthur: And Tom is a labourer, Mr Montgomery was his employer") # Add in code about their relationship
        sleep_line("Arthur: Is there anything else you wanted to ask me about the victim?")
        victim_asked += 1
        victim()
    elif victim_choice == "3":
        sleep_line("Arthur: This case seems quite complex, doesn't it?")
        if victim_asked > 2:
            sleep_line("Arthur: I would deem the victim's closer relationships to be more suspicious.") # If the player asks Arthur 3 times (which requires answering at least 3 times), he will give a hint.
        else:
            sleep_line("3 suspects...")
            sleep_line("I wonder if there were any collaborators.")
        sleep_line("Arthur: Do you have any other questions?")
        ask_question() # Returning to the ask_question function
    else:
        sleep_line("Please enter a valid choice using the number keys. ")
        victim()

def case_evidence():
    sleep_line("Arthur: What do you need to know anything from me about the evidence in this case?")
    sleep_line("Press 1 to find about the poison. \nPress 2 to find about the sweets \nPress 3 to finish asking Arthur about the evidence.") # Add in code about other pieces of evidence
    case_evidence_choice = input("Enter your choice: ")
    if case_evidence_choice == "1":
        sleep_line("Arthur: The poison used is very expensive. I think someone wealthy could have done it.")
        case_evidence()
    elif case_evidence_choice == "2":
        sleep_line("Arthur: There were sweets on the floor of the murder scene, they were scattered around the room, maybe they have something to do with the murder.")
        if sweets == True:
            sleep_line("Arthur: If they were given to him last night, I think it's say to say they were poisoned. If you could determine who, that would do you some great insight")
            print('Evidence Aquired - Poisoned Exotic Sweets')
            Evidence.add ('Poisoned Exotic Sweets')
            time.sleep(5)
        case_evidence()
    elif case_evidence_choice == "3":
        sleep_line("Arthur: I hope I'm leading you to the correct answer.")
        sleep_line("Arthur: Do you have any other questions?")
        ask_question() # Returning to the ask_question function
    else:
        sleep_line("Please enter a valid choice using the number keys. ")
        case_evidence()

#The following function will be refered to in the menu to meet with the officer. 
#officer() # Calling the function to a1sk the officer - Arthur Doyle. Make sure this code comes after the officer function being defined.

#Tom has worked for afew other familys/ companies over the past few years so has a good wealth of knowlage. He sometimes does jobs on the side for a near by factory than handles chemicals.
#The detective enters the room. You see a man sitting on a chair. His clothes are damp and smeared with dirt. Your typical common man who works hard and may know something. Could he be after the fortunes or just a fast way out.
#Why/how would a handyman kill his employer.


import time
def sleep_line(message): #This function will be used so after each line, there is a pause.
    print(f"{message}")
    time.sleep(0.7)

def tom():
    global questioned_tom
    if questioned_tom == 0:
        sleep_line("You have entered a servant\'s room in the Montgomery mansion near the garden.")
        sleep_line("A man is sat of a chair, his clothes are damp and smeared with dirt. The floor is also drenched in rain.")
        sleep_line("He hears your footsteps and his attention diverts to you from the job he was doing")
        sleep_line("Tom: Who are you?")
        sleep_line("You respond telling him that you are Damian, a dectective working on the case of the murder of Charles Montgomery.")
        sleep_line("This must be Tom Fox")
        sleep_line("He relaxes his guard a little but seems to still be defensive.")
        sleep_line("It seems like you will have to earn his trust before he answers your questions.")
        questioned_tom + 1
        tom_earn_trust()
    else:
        sleep_line("You have entered a servant\'s room in the Montgomery mansion near the garden.")
        sleep_line("A man is sat of a chair, his clothes are damp and smeared with dirt. The floor is also drenched in rain.")
        sleep_line("He hears your footsteps and his attention diverts to you from the job he was doing")
        sleep_line("Tom: Ah, Mr. Dollar! Did you need anything")
        tom_earn_trust()


def tom_earn_trust(): # For this witness/suspect, you will have to earn his trust or he may not reveal any good information.
    global trust # The trust variable will be used to keep track of your trust, this varialbe will remain invisible to the player.
    global tom_spouse # The variable will turn from 0 to 1 if you ask Tom about his family.
    sleep_line("What do you want to tell tom?")
    sleep_line("Press 1 to give him a cigarette. \nPress 2 to chat to him about his daily life. \nPress 3 to ask him about his family. \nPress 4 ask about his relation to Mr Montgomery. \nPress 5 to begin questioning him.")
    input1 = input("Enter your choice: ")
    if input1 == "1":
        sleep_line("You give Tom a cigarette.")
        sleep_line("Tom: Thank you.")
        trust += 2
        sleep_line("You talk to tom for a little while, during which you have a smoke.")
        sleep_line("He seems to be a bit more friendly now.")
        tom_earn_trust2()
    elif input1 == "2":
        sleep_line("You talk to Tom about his daily life.")
        sleep_line("He doesn't reveal a lot, he just talks about his work life but he seems more comfortable now.")
        trust += 1
        tom_earn_trust2()
    elif input1 == "3":
        sleep_line("You ask Tom about his family.")
        sleep_line("He mentions that he has a spouse.")
        tom_spouse = 1
        trust += 2
        tom_earn_trust2()
    elif input1 == "4":
        sleep_line("You ask Tom about his relationship to Mr Montgomery.")
        sleep_line("He doesn't talk a lot about his relationship with him.")
        sleep_line("He remains defensive.")
        # No trust will be added for this statement because it appears if you are questioning him already.
    elif input1 == "5":
        sleep_line("You begin questioning Tom.")
        tom_questioning()
    elif input == "6":
        sleep_line("Goodbye, Mr Fox")
        menu()
    else:
        sleep_line("Please enter a valid choice.")
        tom_earn_trust()
    
def tom_earn_trust2():
    global trust
    global tom_spouse
    if trust < 1:
        sleep_line("Tom still appears defensive.")
        sleep_line("It appears that he will not be helpful right now.")
    elif trust > 1:
        sleep_line("Tom appears more comfortable with your presence.")
        sleep_line("Tom: Is there anything I can do to help you Damian?")
    # the next line is not indented because it appears after both if statements.
    sleep_line("Is there anything you want to ask tom?")
    sleep_line("Press 1 to chat with him about his job. \nPress 2 to talk to him about his views on life. \nPress 3 to talk to him about the news. \nPress 4 to begin questioning him.")
    input2 = input("Enter your choice: ")
    if input2 == "1":
        sleep_line("You talk to Tom about his job.")
        sleep_line("He reveals that he has worked for many companies over the past few years.")
        if trust < 1:
            sleep_line("Tom chats with you generally about his job.")
            trust += 1
        else:
            sleep_line("Tom tells you about his previous job at a chemical factory.")
            trust += 2
        tom_questioning()
    elif input2 == "2":
        sleep_line("Tom reveals that he is working because he wants to provide for someone.")
        if tom_spouse == 1:
            sleep_line("Tom talks about his spouse who he calls his 'lady'.")
            sleep_line("His eyes light up when he talks about her.")
            trust += 2
            sleep_line("It looks like he prefers his life over working.")
        else:
            sleep_line("You can he that he is happier when talking about his life.")
            trust += 1
        tom_questioning()
    elif input2 == "3":
        sleep_line("You talk to Tom about the news.")
        sleep_line("He talks about the news of the day generally to you.")
        sleep_line("You both have a conversation about how steam has affected your lives.")
        trust += 1
        tom_questioning()
    elif input2 == "4":
        sleep_line("You begin questioning Tom.")
        tom_questioning()
    else:
        sleep_line("Please enter a valid choice.")
        tom_earn_trust2()

def tom_questioning():
    global questioned_tom
    global trust
    global tom_spouse
    sleep_line("You ask tom if he spoke to Miss Montgommery yesterday, and did she ask about rat poison?")
    if trust > 3 and tom_spouse == 1: #This indicates that Tom has maximum trust in you.
        sleep_line("Tom: Yes I did speak to miss Montgommery. Being the odd jobs man I do often speak with her from time to time. she did leave some money to get more rat poison.")
        sleep_line("Tom: After saying that she would use what was left to get the blighters in the cellar.")
        sleep_line("Evidence Acquired - Rat Poison")
        Evidence.add('Rat Poison')
        poison_found = True
    elif trust > 3 and tom_spouse == 0: # This is the second best outcome.
        sleep_line("Tom: Yes I did speak to miss Montgommery. she wanted to know about the rat poison. Asking how fast it would get a large rat she spotted in the cellar.")
        sleep_line("Tom: I Told her to use what was left as I can always get more next time im on a supply run.")
        sleep_line("Evidence Acquired - Rat Poison")
        Evidence.add('Rat Poison')
        poison_found = True
    elif trust == 2: # This is the third best outcome.
        sleep_line("Tom: Yes I did speak to miss Montgommery. She left some money saying something about rat poison.")
        sleep_line("Evidence Acquired - Rat Poison")
        Evidence.add('Rat Poison')
        poison_found = True
    else:
        sleep_line("Tom: Yes I did speak to miss Montgommrey. But I am unsure as to why you are questioning me.")
        sleep_line("Tom: I am only the odd jobs man. She did say something about the rat poison and did leave some money to go get more")
        sleep_line("Evidence Acquired - Rat Poison")
        Evidence.add('Rat Poison')
        poison_found = True
    sleep_line("You note down what Tom has said.")
    sleep_line("Next you ask Tom about the time he has taken off recently.")
    if trust > 3 and tom_spouse == 1:
        sleep_line("Tom: I took some time off to prepare to marry my lady.")
    elif trust > 2:
        sleep_line("Tom: Yes i did ask for more time off, but I have been busy recently.")
    else:
        sleep_line("Tom: Yes i did ask for some time off, but I did not kill my employer.")
    sleep_line("You note down what Tom has said again.")
    if trust > 3:
        sleep_line("Tom appears innocent.")
    sleep_line("You thank him for his time and leave.")
    questioned_tom = 1
    menu()

def lawyer_questioning():

    scene = "lawyer_discussion"

    print('Inside the grand library, there is only one man, not even a police officer in sight.')
    time.sleep(3)
    print('He sits, quiely going through paperwork.')
    time.sleep(3)
    print('This must be John Gotti, Charles\'s lawyer')
    time.sleep(3)
    print('"Excuse me, but are you Mr. Ghotti?')

    dialogue(Lawyer, "Oh yes, sure, how can I be of assistance?")
    dialogue(Detective, "We suspect this is a murder, and a formal statement, and a few answers, from you may be of help to us.")
    dialogue(Lawyer, "What are you looking for?")

    while True:
        if scene == "lawyer_discussion":
            print("Choose a question to ask the lawyer:")
            print("1. What can you tell me about Charles Montgommery?")
            print("2. Tell me more about Charles's relationship with Marilyn Martin.")
            choice = input("Enter the number of your question (1/2): ")
            if choice == "1":
                dialogue(Lawyer, "Charles Montgommery was a complex individual.")
                dialogue(Lawyer, "He had a lot of secrets, and I was privy to some of them.")
                dialogue(Lawyer, "What would you like to know about him?")
                scene = "lawyer_discussion_2"
            elif choice == "2":
                dialogue(Lawyer, "Ah, Charles's relationship with Marilyn Martin.")
                dialogue(Lawyer, "That was a delicate matter, and I have some information that might interest you.")
                dialogue(Lawyer, "What specifically would you like to know about their relationship?")
                scene = "lawyer_discussion_2"
            else:
                print("Invalid choice. Please enter '1' or '2'.")

        elif scene == "lawyer_discussion_2":
            print("Choose a question to ask the lawyer:")
            print("1. Tell me more about the confidential agreement.")
            print("2. Did Charles mention any potential enemies or threats?")
            choice = input("Enter the number of your question (1/2): ")
            if choice == "1":
                dialogue(Lawyer, "Certainly. Charles was deeply enamored with Marilyn, but he was well aware of the complications such a relationship could bring, given his marriage to Stacy.")
                dialogue(Lawyer, "To address this, he had me draft a confidential document, a 'side agreement' as he called it.")
                dialogue(Lawyer, "It outlined his intentions to provide for Marilyn discreetly in the event of his death, as long as she maintained their relationship away from the public eye.")
                dialogue(Detective, "A secret agreement, huh? This could be a significant piece of the puzzle.")
                dialogue(Detective, "Did Charles's wife, Stacy, know about this agreement?")
                scene = "lawyer_discussion_3"
            elif choice == "2":
                dialogue(Lawyer, "Charles didn't explicitly mention any enemies or threats to me.")
                dialogue(Lawyer, "However, he was aware of the potential risks associated with his business dealings and personal life.")
                dialogue(Detective, "I see. It's essential to consider all angles. Let's get back to the agreement.")
                scene = "lawyer_discussion_3"
            else:
                print("Invalid choice. Please enter '1' or '2'.")

        elif scene == "lawyer_discussion_3":
            dialogue(Lawyer, "Charles was concerned that his relationship with Marilyn could tarnish his reputation, and he wanted to ensure her financial well-being without causing a scandal.")
            dialogue(Detective, "Thank you for sharing this, Mr. Gotti. It adds a new dimension to the case.")
            dialogue(Detective, "We'll need to look into that agreement and its implications further.")
            dialogue(Lawyer, "Yes, Detective Dollar, this agreement was a well-guarded secret.")
            dialogue(Lawyer, "As far as I know, neither Stacy nor Marilyn were aware of its existence.")
            dialogue(Lawyer, "But considering their domestic situation, it's possible that they might have discovered it.")
            break

    print("End of conversation.")
    menu()

def good_ending():
    print('As the hubababalu settled down around the town, it is clear that it would never be the same around here')
    time.sleep (2)
    print('The Montgommery business empire quickly faded as Stacy was forced to give it all to Mr. Martin')
    time.sleep (2)
    print('Unfortunatly, he was not able to keep it running by himself, so instead began to hire managers internally to run it')
    time.sleep (2)
    print('Coincidentally, one of those promoted was a man called Tom Fox, who settled after the incident into a nice, cushy, well-paying job')
    time.sleep (2)
    print('Mr and Mrs Martin\'s relationship never recovered. They split amicablly, both going their seperate ways, and maintained a mutual friendship, but never anything more than that')
    time.sleep (3)
    print('Arthur Doyle, recived a promotion for the case, despite not solving it. He however found himself a new career, about 5 years later.')
    time.sleep (2)
    print('The mansion itself was turned into a mansion, with Arthur leading tours, warbarling on about what \'an intresting case\' this mansion is.')
    time.sleep (2)
    print('John Ghotti quickly took out all of his stakes in the Montgommery business, and moved to the big city, in order to continue practice as great business lawyer.')
    time.sleep (3)
    print('Damian Dollar however, vanished not long after. The Captain looked everywhere, and eventually, found a note saying "I\'m not doing this again. I\'m moving to Belguim. Nothing instresting ever happens there for detectives"')
    time.sleep (4)
    print('But for many years, sleep returned to Stuckupshire...')
    time.sleep (2)

def bad_ending():
    print("You got both the killer and evidence wrong.")
    time.sleep(1)
    print("Your reputation as a detective has been tarnished.")
    time.sleep(1)
    print("In this world of steam, you have to always be quick and precise.")
    time.sleep(1)
    print("Maybe in the future, you will be able to restore your reputation.")
    time.sleep(1)
    print("But for now, your future is a mystery.")
    time.sleep(1)
    print("--------------------------------------------")
    print("You have achieved the bad ending.")
    time.sleep(1)
    print("Game Over")


def neutral_ending_wrong_evidence():
    print("It seems like some of your answers were correct, but there is something missing.")
    time.sleep(1)
    print("You return to your detective agency, with this case fresh in your mind.")
    time.sleep(1)
    print("You think to yourself, 'have I missed something?', but you just can't figure it out.")
    time.sleep(1)
    print("Suddenly,there is a knock on the door of your agency.")
    time.sleep(1)
    print("You go to the door and open it, a police officer is on the other side with his face full of worry.")
    time.sleep(1)
    print("Police officer: Detective Damian, another murder has occured.")
    time.sleep(1)
    print("Police officer: Please come with me.")
    time.sleep(1)
    print("You follow the officer, it seems like you will have no time to think about the Montgomery case.")
    time.sleep(1)
    print("The streets are bus with activity, steam fills the air but also fogs your mind.")
    time.sleep(1)
    print("---------------------------------------------------------------")
    print("You have acheieved the neutral ending.")
    time.sleep(1)
    print("You got the suspect correct but not the evidence.")
    time.sleep(1)
    print("Game over.")

def neutral_ending_wrong_killer():

    print("It seems like some of your answers were correct, but there is something missing.")
    time.sleep(1)
    print("You return to your detective agency, with this case fresh in your mind.")
    time.sleep(1)
    print("You remember the faces of the people in the Montgomery mansion.")
    time.sleep(1)
    print("Their reaction to the poison was one of shock except for one of the suspects.")
    time.sleep(1)
    print("The face of that suspect appeared almost happy.")
    time.sleep(1)
    print("You think to yourself 'Who was that?'")
    time.sleep(1)
    print("Suddenly,there is a knock on the door of your agency.")
    time.sleep(1)
    print("You go to the door and open it, on the other side, there is a police officer with his face full of worry.")
    time.sleep(1)
    print("Police officer: Detective Damian, another murder has occured.")
    time.sleep(1)
    print("Police officer: Please come with me.")
    time.sleep(1)
    print("Your thoughts about that other suspect cannot be dealt with now, there is a new case to deal with.")
    time.sleep(1)
    print("You follow the officer, as he leads you through the smoke and mist.")
    time.sleep(1)
    print("The streets are bus with activity, steam fills the air but also fogs your mind.")
    time.sleep(1)
    print("---------------------------------------------------------------")
    print("You have acheieved the neutral ending.")
    time.sleep(1)
    print("You got the evidence correct but not the suspect.")
    time.sleep(1)
    print("Game over.")

def secret_ending():
    print('After acussing yourself, Damain Dollar is thrown into prison. He has been sentenced to death')
    time.sleep(2)
    print('Or is it? Was this all part of his plan?')
    time.sleep(2)
    
    while True:
        answer = input("Do you want to find a way to escape prison? (yes/no): ")
        if answer.lower() == "yes":
            print("The process starts.")
            time.sleep(2)
            prison_escape()
            break
        elif answer.lower() == "no":
            print("You will stay in prison then.")
            time.sleep(2)
            break
        else:
            print("Please enter 'yes' or 'no'.")

def prison_escape():
    answer = 'yes'
    if answer.lower() == "yes":
        print(f"{player_name}: I am making a request to escape prison.")
        time.sleep(1)
        print("Unfortunately, you are not allowed out of prison for the murder.")
        time.sleep(2)
    
        print("You have found a way to escape prison, and the police are after you.")
        time.sleep(1)
        print("You only have one chance to press the correct button for the police not to catch you. If you press the wrong one, you will be caught and executed in prison. GOOD LUCK!")
        time.sleep(2)

        user_input = int(input("Damian Dollar, enter any number between 0 and 6: "))
        
        if user_input % 2 == 0 and user_input < 6:
            print("Unfortunately, you have failed in escaping prison.")
            time.sleep(2)
        elif user_input % 2 != 0 and user_input < 6:
            print("You have successfully escaped!")
            time.sleep(2)
        else:
            print("Please insert a number between 1-6.")
            time.sleep(2)

def theAccusation():
    self_accusation = 0
    killerCorrect = False 
    poisonMediumCorrect = False 
    poisonSellerCorrect = False
    motiveCorrect = False
    poisonApplierCorrect = False
    poison_found = False
    print('I should have everything I need. I ring a glass to gather attention of everyone in the room, and ask the other officers to gather everyone else.')
    time.sleep(2)
    print('All I need is to do now is prove it.\n"Attention all. I have not only figured out who the killer is, but how and why they did what they did."')
    time.sleep(2)
    print(f'{officerFN} pipes up.\n"Now, now that seems awfully quick. You\'ve been here less than an hour!"')
    time.sleep(2)
    print('"It\'s all quite elementary really. Let me walk you through it, step by step, so all of you gathered can understand too.')
    time.sleep(2)
    print('"First things first. The killer in this case had one goal in mind."')
    time.sleep(2)
    motiveFinal = int(input('What was the motive for the crime\n1. Lust\n2. Gluttony\n3. Greed\n4. Sloth\n5. Wrath\n6. Envy\n7. Pride\n'))
    if motiveFinal == 3:
        print('"Greed. They needed poor Charles\'s death to look like an accident, or natural so that all the paper work would go through without an issue."')
        motiveCorrect = True
        time.sleep(2)
    elif motiveFinal == 1:
        print('"Lust. They wanted Charles all to themselves, but they couldn\'t, so they killed him instead!"')
        time.sleep(2)
    elif motiveFinal == 2:
        print('"Gluttony. Charles was a famous eater of exotic sweets, and they decided that they were going to take and hide them all2')
        time.sleep(2)
    elif motiveFinal == 4:
        print('"Sloth. They had wanted to kill him for a long time, but could not be bothered to find that oppurtunity. Perhaps they worked to hard, and wanted to work less..."')
        time.sleep(2)
    elif motiveFinal == 5:
        print('"Wrath. This was a crime of passion. Charles had angered them, and they lashed out by poisoning him"')
        time.sleep(2)
    elif motiveFinal == 6:
        print('"Envy. Jelously is a common motivator for these types of crimes. Perhaps they were Jelous of his or someone close to his position, and wanted to change that"')
        time.sleep(2)
    elif motiveFinal == 7:
        print('"Pride. They disliked Charles and his actions, as they brought down their name and business."')
        time.sleep(2)
    else:
        print('I have no idea')
        time.sleep(1)
    print('"Now, in order to succeed with killing, they decided it would be necesary to posion the man. Now what to use, what to use..."')
    time.sleep(2)
    print('"There are many poisons avaliable in the world, espicially to the rich"')
    time.sleep(2)
    print('"But would they know that? I don\'t think so, considering who they aquired the poison off?"')
    time.sleep(2)
    poisonSellerFinal = int(input('Who did they aquire the posion off?\n1. Damian Dollar\n2. John Ghotti \n3. Marylin Martin\n4. Tom Fox \n5.Arthur Doyle\n6. Stacy Montgommery\n7. Charles Montgommery\n'))
    if poisonSellerFinal == 4:
        print('"Poor Mr. Worker, had his posion bought off him. For some reason, the killer knew about it, and aquired it off him. He must be overwhelmed with guilt now."')
        poisonSellerCorrect = True
        time.sleep(3)
    elif poisonSellerFinal == 1:
        print('"I owned the poison. It is common household poison, and I really hate rats, you know? Anyway..."')
        self_accusation = self_accusation + 1
        time.sleep(3)
    elif poisonSellerFinal == 2:
        print('"The Lawyer. He was all to happy to take a cut of his will, and supplied the rat poison from a different case he was invloved in"')
        time.sleep(3)
    elif poisonSellerFinal == 3:
        print(f'"Did you all know that Mrs.{mistressLN} is the wife and co-owner of a dealer in deadly chemicals? It was all too easy to take some of it for a personal vendetta..."')
        time.sleep(3)
    elif poisonSellerFinal == 5:
        print(f'"Our good officer {officerLN}. He could easily have acquired it from any number of murder cases, and no one would think the wiser"')
        time.sleep(2)
    elif poisonSellerFinal == 6:
        print(f'"Mrs. {wifeLN}, she is the caretaker of this large house. Why, she should be the biggest dealer in rat poison in the world. Ha Ha Ha..."')
        time.sleep(2)
    elif poisonSellerFinal == 7:
        print('"In a cursed bit of fate, Charles himself sold the poison to his killer. Now I can\'t speak as to why, but I should imagine he certainly regrets it now"')
        time.sleep(2)
    else:
        print('I have no idea')
        time.sleep(2)
    print('"Then, they needed to posion poor Mr. Montgommery. The killer needed to do it an a way that would draw suspicision away from themselves, so they used very sneaky medium to administer the posion."')
    time.sleep(2)
    mediumLoop = True
    while mediumLoop == True:
        print("Enter the evidence exactly as it is written.")
        poisonMediumFinal = str(input('What did the killer use to poison Charles Montgommery? [To see evidence, type "E" or "e"]'))
        if poisonMediumFinal == 'e' or poisonMediumFinal == 'E':
            for x in Evidence:
                        print(x)
                        time.sleep(0.5)
        elif poisonMediumFinal.lower() == 'poisoned exotic sweets':
            print('"They put them in something Charles could never resist. Some of his favourite forigen sweets"')
            poisonMediumCorrect = True
            mediumLoop = False
            time.sleep(2)
        else:
            print('I don\'t think that is right, but I\'m on a roll now so...')
            mediumLoop = False
            time.sleep(2)
    print('"Now who to poison him. They could get a lot of people to do it, but maybe they only trusted themselves to do it?"')
    time.sleep(2)
    poisonApplierFinal = int(input('Who applied the posion?\n1. Stacy Montgommery\n2. John Ghotti \n3. Marylin Martin \n4. Tom Fox\n5.Arthur Doyle\n6. Charles Montgommery\n7. Damian Dollar\n'))
    if poisonApplierFinal == 3:
        print('"If the not so secret mistress give\'s the poison to Charles, then they would for far more likely to succeed"')
        poisonApplierCorrect = True
        time.sleep(2)
        if poisonMediumCorrect == True:
            print('"I mean, who would refuse sweets from a secret lover?"')
            time.sleep(2)
    elif poisonApplierFinal == 1:
        print(f'"In a cruel twist of fate, the wife was the one to apply it, either through a servant, or maybe something she had on herself"')
        time.sleep(2)
    elif poisonApplierFinal == 2:
        print(f'"In one of their recent meetings, Mr {lawyerLN} applied it, using a moment of trust, maybe sticking it a tray of food, or as a gift to a long-term client"')
        time.sleep(2)
    elif poisonApplierFinal == 4:
        print(f'"Now while {workerFN} wouldn\'t have had many oppurtunities, it does seem to me that he took his chance when he had to. He could always be there, but never be seen. A true invisible worker."')
        time.sleep(4)
    elif poisonApplierFinal == 5:
        print(f'"If say a police officer were to give you something, as an unpstanding member of society, you wouldn\'t want to refuse anything from them"')
        time.sleep(2)
        print(f'"So I suspect it was {officerFN} who, on a routine patrol, may have passed him something!"')
        time.sleep(2)
    elif poisonApplierFinal == 6:
        print('"Charles knew about the posion, he\'s not an idiot. But he wanted to, no he HAD to take it, in order to succeed with his goal"')
        time.sleep(2)
    elif poisonApplierFinal == 7:
        self_accusation = self_accusation + 1 #This was added in on 12:18 on the 25th of september so the secret ending can be reached.
        print('"Perhap\'s a nosy dective, such as myself, while calling him for a secret meeting, passed him something. Perhap\'s he was suspicous, but not enough. He fell for it all the same"')
        time.sleep(4)
#Add the Extra line for the appliers
    print('Finally, who orcustrated all of this. All of these machinations, these evil doings. Who is the killer, the mastermind?')
    time.sleep(2)
    killerFinal = int(input('Who is the mastermind?\n1. Damian Dollar\n2. John Ghotti\n3. Marlyn Martin\n4. Tom Fox\n5. Arthur Doyle\n6. Stacy Montgommery\n7. Charles Montgommery\n'))
    if killerFinal == 6:
        SwifeFName = wifeFN.upper()
        killerCorrect = True
        print(f'"...THAT\'S RIGHT...{SwifeFName}"')
        time.sleep(4)
        print('"You organised everything!"')
        time.sleep(2)
        print('"WHAT. THAT\'S A LIE. HOW DARE YOU ACCUSE ME OF SUCH NONSENSE"')
        time.sleep(2)
        print('"You\'re coming in!"')
        time.sleep(2)
    elif killerFinal == 1:
        self_accusation = self_accusation + 1
        print('"That\'s right you fools! I did it"')
        time.sleep(4)
        print('"And you all needed me to spell it out for you!"')
        time.sleep(2)
        print('"I\'m dissapointed in you all"')
        time.sleep(2)
    elif killerFinal == 2:
        print(f'"Mr.{lawyerLN}, you dasdardly fool. Did you really think you\'d get away with it?"')
        time.sleep(2)
        print('"What, I don\'t believe it..."')
        time.sleep(2)
        print('"I hope you can defend yourself in court..."')
        time.sleep(2)
    elif killerFinal == 4:
        print(f'"I\'m sorry, {workerFN} I know you did it. I\'m going to have to bring you in..."')
        time.sleep(2)
        print('"What? I would never do anything like that...')
        time.sleep(2)
    elif killerFinal == 3:
        print(f'"Mrs. {mistressLN}, You are the killer! It is quite clear that this is your fault"')
        time.sleep(2)
        print('"That\'s impossible, I would never hurt Charles..."')
        time.sleep(2)
        print('"We\'re bringing you in Miss"')
        time.sleep(2)
    elif killerFinal == 5:
        print(f'"{officerFN}, It\'s time to confess."')
        time.sleep(2)
        print('"Confess what?"')
        time.sleep(2)
        print('"Confess that you killed Charles! As an officer of the law, I am dissapointed in you"')
        time.sleep(2)
    elif killerFinal == 7:
        print('"I am sorry to say, but it appears that Charles... Orcastrated his own demise."')
        time.sleep(3)
        print('"Everyone looks taken aback? "What are you talking about?" The wife pipes up, looking fustered"')
        time.sleep(2)
        print(f'"He posioned himself, using such a roundabout method?" {officerFN} seems very confused"')
        time.sleep(2)
        print('"Yes, in order to frame someone. Luckly, or should I say, I skillfully prevented any such framing. You can thank me later"')
        time.sleep(2)
    else:
        print('I have no idea')
    
    if killerCorrect == True and poisonApplierCorrect == True and poisonMediumCorrect == True and poisonSellerCorrect == True and motiveCorrect == True:
        good_ending()
    elif killerCorrect == True and self_accusation != 3:
        neutral_ending_wrong_killer()
    elif poisonApplierCorrect == True or poisonMediumCorrect == True or poisonSellerCorrect or motiveCorrect == True and self_accusation != 3:
        neutral_ending_wrong_evidence()
    elif self_accusation == 3:
        secret_ending()
    else:
        bad_ending()

#Add extra lines for the killers
menu()



