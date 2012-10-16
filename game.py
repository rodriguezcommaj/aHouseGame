import sys
import time

print """
????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
?????????????????????????????????????????????I?I??????????I?I???I?I??III????I??I????I???????????????????????????????????
???????????????????????????I????I?I?I???III?IIII?I?IIII??I?I?IIIIIIIIIIIII?IIIIII?I?II????I???????????II????I??I????????
????????I?I?????I????????IIII?II?II?IIII?~IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII??II?I?I??I????????I??
?I?III????I??II?IIIIIIIIIIIIIII?IIIIIIII~=?IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII?II?I??I????
I??I????IIIIIIIIIIIIIIIIIIIIIII:~+IIIIII7+IIII?IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
I?III?III?IIIIIIIIIIIIIIIIIIII:~=+??~=II?+IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
IIIIIIIIIIIIIIIIIIIIIIIIIIII::~.I.:=?I+I7=?IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII?IIII+:IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
IIIIIIIIIIIIIIIIIIIIIIIIIII,~~....I.:~??+~:I+++?IIIIIIIIIIIIIIIIIIIIIII?+:~=??+??+?I~=IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
IIIIIIIIIIIIIIIIIIIIIIIIII,~..,.,.~.?,:=?II=+?I?I?++?IIIIIII+:====+++??++??+?II+???,,,IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
IIIIIIIIIIIIIIIIIIIIIIII=,:...:,::....?+:?III????III?+?7=I????+++?I?I?++I??+I+7I?I?..,.IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
IIIIIIIIIIIIIIIIIIIIIII,~~....~~~~,,...,=++?I7II?7I7I???=?++?+??+???++7?+???+???+?+..,,IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
IIIIIIIIIIIIIIIIIIIIII::..,~.~~:,:~~~~...~+~+?+????I???I?I++??+??????+?=?I?+?????.....,,IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
IIIIIIIIIIIIIIIIIIII~::,...:~:,:=:,,,~~~.:,=..~?=??IIII?I?????+?+?+?+??I++??????I,,,..,,IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
IIIIIIIIIIIIIIIIIII::=,...:~:~~~~~:~::~~~:...=~,,,,I???II77??+??+???++???+++??=+,,,,,.,:,IIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
IIIIIIIIIIIIIIIIII:,...:.:,,:,::::~~~=:,::~,,:.,:,...,,,,7II?+??+??I+?+?++~=.,:~...,,,.,,:IIIIIIIIIIIIIIIIIIIIIIIIIIIIII
IIIIIIIIIIIIIIIIII=...,,:~~~~~~~~~+~::~,,.=?:,...,,,,:~:,..,,.=:~~:......,,:,....,.,,,,,,,,?IIIIIIIIIIIIIIIIIIIIIIIIIIII
IIIIIIIIIIIIIIIIIIII~,:=~..,~,~=?~.:~........,.,....,,.,.,,::,............,:,,~.,,,,,,,,,..:,IIIIIIIIIIIIIIIIIIIIIIIIIII
IIIIIIIIIIIIIIIIIIII.::....,,,,,,,.:::,...,:.,,,,,,,,:....,,....,::,,,,,,,:,:~~.,,..,,,:.,,,:,IIIIIIIIIIIIIIIIIIIIIIIIII
IIIIIIIIIIIIIIIIIIII:~~.,,::.,,::.,:~~.,...::..,,,,,,,:,.,,,..=~:::~::..,=,:::~,,,.,,,,,.,,,,,,IIIIIIIIIIIIIIIIIIIIIIIII
IIIIIIIIIII?????++++~=~~=:::==~:==~~~~....::::,~,,.,,,,::,....~,~7I=~~,,:?::::~,,,.:::,,,,,,.,.,~==============IIIIIIIII
+++++++===++++=+++++:~~~=::,?=,::=:~:::=,.....~=,,:.....,,,,..::~.,=~=::+I~~~:~.,,,,::,,,:,,:,.,,:===+?++++++++=++++?===
+++++++++=+++++++++=~::~=:~~+=:,:~~~~~:=:~====~=...,,,,,,,,...~~=.+?~~~++I~:,,:,:,,,:::::,:,,,..,,,++?,~+++++++++I?I====
++++++++++++++++++++~::~===~I+I+~~~~~:~~:~=~=~~=:,,,::,,,,....::~.~.~=~?,?~,:::,,..,:,,:,:,:,,,...,:+?+=++=++???IIII=III
7II777III?+?7I+?+??+~~::~I:.:+~:.~:::~=~:~=~==~=......,,,.....::=.,,+~,,~=~::::::,,:,,,.,,,,,,,,,..+??IIIIIIIIIIIII?I~,,
7777777I777777777777:=~~~I..~=+..+=~~~~=,+=~=~~~.,.....,:::..:~~~,..?~,.:~:~~~::::,,,,:,,:=,,,,,,,,:IIII~II=++IIII+:::==
7II7I777I7II777777II~~~:~I..==+..+=:::~~:~=~=~=~,:::,,.,,,,..:~:=,..?~:.::::::::~~,,,.,,,:+,,:,.,,,II???+~~=~=+?+,,=~~==
+II77777I77777I77777~~~~~I,.:=?.:~~~~~~~:=?:=.~~,:~~,,,,,,,,.::~~:..?~~.::::~~:::~:,:,:,,~???,,.,,,..=~+::~~~~==?=~=::::
,,~,,=:+:=:=:,=:,~~.~:~~=7I77=???+~~~~~~:~~~~=:~:~~=~,,..,,..::~~?+?I:+++??=~~:~,:,~++:::::::::.,,,7~?~+:~~~~~~+=+~~~~~~
=7::~?::?~::?+?~:~=.~~::.,,,,::~~:~~~~~::=~~=~~~.,,::::,,,...?~~,,,,,.,,,,,~~::~:,,:,:::::,:::~:=:=:II?+~?+?++~+=++?=+??
I,:I~,.I:~=+:~,I+~:7~~~~=~=~===~=~=~~::~,=~:~:~~....,.,,:::,,,,,:~:~~:::~:::~=:~,:::::7I~~+~:~II?I+?+?????+:.~=+I??+++==
::I~?++==+I+:~,7I,?+=~==~~~~~==~~~~+=~~~,~=~====:::,,,,.,,,,.::::::~~:::~:::~+:~++=+::+I~+??II~+?++?+=?+???~,?7~II?+++=+
I=?=?+==+==?++=~+~=~=+?+++========,,,,,~:,,.::,==,:~:,~~,,,::::~=~=++=+++++=?+?+==+=?++++?+++++++?~~~,:++??=~:~:~?=::~~~
~~~=:==~======::~:~=:=~+====++++~,:~:,+====~++~++=++====+=++++=====+++======+=+=++++?????++?++=~==~+=~~~=+I+==+~:?==++=:
~==+~:=~+++==+=~======+~===~========++?++=~~==+=~+===~=++=+====~=+=~~+=~=====+===++====+========+==+=+++++==+=====+++==?
+===+=====+===++==~==+++++=~:~=====~=+=+==~==~+==+==+==+==============~~===+===+==+==~+===+===+=++===+=====~+=+===+~+=+?
++=======~==+~:~~~~~~==~===========~======+=+++++++++++==+=+============+++=+++++++++=========~=~==~~+=========+========
+=====+===~~~~=~~~~~~~~~=====~====+++=====+====+===~~~==~=~~~=====+=+=++++====++===++=====+=======~+=++========~==+~~===
~~=~===~~~=~==++====~=+=======+=+========+=+=======+===~=~~==7+?+==+?+++++?=++++=+=+==++=======~~~==~==~==~=~~~:::======
~==~+~===~~=++===~~~~==~=====~=~====~~==+=========~=======~==+=++++=~==++=++++==~+~==+=~~~~=~~::::~~~::~~~====~~=:=~=~++
"""

print "You are standing on a wet, grassy hill.\nThere is a rundown house nearby.\nIt is dark and cold, but a soft glow emanates from underneath the door and through the cracks in the boarded up windows."
print "You hear the screams of a woman issue forth from the house."
print "Do you < RUN > towards the house to investigate? Or do you < RETREAT > back down the hill and forget you heard anything?"

bravery = raw_input("> ")

if bravery == "RUN":
	print "You sprint as fast as you can towards the house, your heart pumping as adrenaline fills your veins."
	print "You find the door barricaded.\nThere is an axe lying on the ground nearby.\nDo you < USE THE AXE > or try to < BREAK DOWN THE DOOR > to get in?"

	door = raw_input("> ")

	if door == "USE THE AXE":
		print "It takes a few swings, but you are able to get in.\nYou see a young woman, covered in blood, lying on the floor.\nShe looks lifeless."
		print "You only look around for a few seconds before you see something out of the corner of your eye..."
		time.sleep(2)
		print "..."
		time.sleep(2)
		print "..."
		time.sleep(2)
		print """
		++:.++?+==~=~~++++++=+=+++++++==+===????II7777777II:~,+~:~~:?7III7II7II77I777III?=~=++=~~~=~==~=++===~=~~~~:+::+?????+??
		+?::=??+=====++==++++=+++++++++++++===+??II7I77I777I~~~::=+I77I77I777777I7I?II+++++=~=~~~~~~=+=++~~~:=~~~~:~+~::=+=?????
		+=,~++==+::=+===++=+=+++++++++++==+++===?II7I77777777I7I7III77777777777I7IIIII?==~==~~~::~~==~:=~:,,,,::~,:~=~~~~=??I???
		++,=?:===~===~=+==+++++++++=+++======+++??IIII777777777II7I77777777777I7II7II++=~~:::::~:~==,,:::,::.,,,,,::~~~~::++?+??
		?+,==~=~~=~======++++=+=+=~=======~==~~~+?IIII77I7777III7777777II777III7III?==~~::::,::~:,..,,,,:,,,,I+..:,,,~~~~:~???I?
		??:+====~:======~~~==:=~~:~~,~~~~~~~~~~~~++I?I7III7777IIII77IIII7I77III7I?I+~~::::,,:,:,......,.,,,,.,,=......~:~::+?+??
		?+~+?=~~~=~=~~:~,::,,,,,:,,,,:,:~~=~~~~:~~=+??IIII7IIIIIII7I77IIIII7IIIII?+=:::,,,,,,.,...........,..,,,,.....,:~:,++?I?
		I+~+++~::~~,:::,.,....,..........,::~~::::~=???IIIIII7II77II7I7I7I7IIII??++:,,,,,..=...........................,::=+I??+
		?+=??=:::,::......,,,..,..........:,~~~:::::~++?IIIIIIIIIIIIIIIIIIIII???+::,,,,,................:.,..........,,:::??I?I?
		??==++:::,.:....,..,.....,,.....,,.,:~~~~::,,:~=?IIIIIIIIIII77IIII?I??+:,,,,,,.......,...,,,:,...,.............,.:==???I
		?=~+?+=:.,..,.......,=+???????+:.,:..,:~~~::,~::~+IIII777III777II????=::::,,:,,...,,.,=+??????++~.,............,.=++?+I?
		?+:~II~:,,,.......:=?II+,:::::III=,.:...::~::~~==~=?I77777I777II?I?++~~~~~~:,....,::?II=::::::?II++:..........,,~II?:7?I
		?+~:+??+~,.......~+?II,~==++=+==7I?:.::...::~~~=++++I7777777I7III???+?==~~~,:,..,,=?I?~=+=+===:~II?+:........,===?:~I+?I
		?+::,,=+=........~???:===II?I?+~+III~.,..,.,~+++?I??III77777777II?I?II?++~~,...,:?III~==?I???~=:?I?+=,.........,.??~~=?+
		I,:=?=?I?.=......~=+?,=~~:=.++==~III?++...,+III?IIIIII77777777IIIIIIIII?+~,..,,?+??I?:~=~=.?+~~~~???=.......,..~:~=~?I+?
		+:=I7I=:I+=,.....,::=~~+=~=~====+?????,.::~=?I77IIIIII7777777777IIIIIIII=+=,....+??II:====~===~:+==:.,,....:+IIII??=II??
		?++?IIIII=:::.......~:,,,.,,.,:..:~:~,:,,.,+II77I77III777777777IIIIIII77I?+~~=,,..,,.,=~?+===::::=..,......,?7IIII++IIII
		??++?IIIII~++=.,.........,.,.:,:~::,~,~++I??I7777IIII7I777777II77IIII7777II?~,~+~~,,:.,,.=...............:=:I7III?+??III
		I~?I?IIIII+=+~=~:,.........=~~:..~==+II7II777III77II77777777777777IIII7I777IIII,:::=:~==,~,:,,,=:.......=?,++III????IIII
		????IIIIII?+=~~??:~~~:?,~,,:::,~=++7IIII77777777III77777777777777777II7II7777777::,,,,,...,::,:,,......=???++?II?????I+?
		~+?+???IIII=+~~=I?I?=+~~,,,:+?IIIIIIIII777II77IIIII77777777777777I77IIIII7I77777?I:..................~:=,::,,~IIIII?++??
		??I????I??+~.,.?=:~::~?IIII7?I??I?III7777777I7III77I77777777777777II7IIII777777I77I??:,............~????+?I+:~++II??I??+
		=????II??+?:=:~?~+IIIIIIII?III?I??I77777777777III77I7II7777777777777IIIII77777I77777II?,........~~+??III?+?+,~I?II??I???
		++?IIIIIII~7,.~II???II?I??III??777777777I777777IIIIII7I7777777777IIIIIII7III7I7I7777777I7,~,,~=+,+IIIII7I7I,,.7?IIII?7??
		++?IIIIII+I~II77IIIII7I?III777I7I77777777777777I7777I7777777777777IIIIII7777III77I77II777?~.~III777II7I77III?IIII??I????
		=+??III7I7~+7III7777777I77777777I7I77777I7777IIIIIIIII777777777777IIIII777I7777777777777I7,,IIII77I77IIII7IIIIIIII?I?I??
		+++III7II7~IIIIII777777I777777I77I777777I777IIIIIIIIII7777777777777I7II77III777777777777I?::?77777I7I7IIIIIIIIIIIII?II??
		?++?III777=IIII7I7777I77777777I7I777777777777IIIIII777I777777777I77IIIIII7II7777777777777III?7I7777777IIIIIIIIIIII?III??
		+?+?IIIII+III77I7I7IIIII77777777777777I77I77IIIIIIIIIIII7777777I77IIIIIIIIIIIII777777777777II77I7I77777I7IIIIII?III?7??+
		+?+I?IIII+IIIIIIIIII7I777777777777777I77I777IIIIIIIII777777777777IIIIIIIIII7IIIIII7II7777777II77I7I7777IIIIIIIIII???7??+
		+??+?IIII+IIIIIIIIII777777777777I7II7IIIIIIIIIIIIII777777777777III7777IIIIIIII7IIIII777I77II~IIIII77I7IIIIIIIII?I??II?+=
		?+?+?I?I+III?IIIII7III7I7777777II7I77II7IIIIIIIIIIIII7777777777III7II7I7II7IIII7IIIII7III7II+II7IIIIII7IIIIIIIII?I?II?==
		++?+????~I?IIIIIIIIIIIIIII7I7II7III7IIIIIIII7III7II7I7I7777777777III7777IIIIIIIIII?IIIIIIIII?IIIIIIIIIIIIIIIIII????I??~+
		.?++???~II?III?IIIIIII7III777IIIII7III?IIIIIIII77IIIIII777777777II7I7I7777IIIIIII7I?IIIIII?+7IIIIIIIIIIIIIII?II??+?II?=+
		.++++??+???IIIIIIIIIIIIII7IIIIIIII?I7II+IIIIII7IIIIIII77777777777IIII7777IIIIIII7I7I?IIIII+I7IIIIIIIIIIIIIIIIII+??+II?,.
		.=+?+???=I?I?IIII?IIIIIIIIIIIIIII?IIII????I??I??IIIIII7777777777II??IIIIIII??II77IIIII?I7??77IIIIIIIIIIII?II?II+???II?,,
		.=+=+??I~+II??IIIIIIII?IIIIIIIIIIIIIIII??+++?+:=++?+?II7I777IIII????,.,::+???IIII77I7II??++IIIIIIIIIIIII?II????I?I?I?I,,
		.=++????=??I??I?I??IIIIIIII7IIIIII7II?II?I+++++?=:,~+??IIII?I??++=,,~=?II?+III?I7III777I?=IIIIIIIII?III??I??II+?I??I??,,
		.~++?????+??III?????IIIIIIIII?IIII7I7IIII????+??+++=:==+??+++?=+~=+??II??I?I?IIIIII7I7III?I?IIIIIIIIII?????I???I?I?I?,,,
		.,=+??II???II?II?I??II?IIIIIIII7IIIIIIIIIIII?I??++????=+++++==+++?I?IIIIIII?IIIIII7IIIIIII+IIIIII7II?IIIIIIII+I?I?+:=,..
		..=++??II=I??I??I?+??III?II7II7IIIIIIIIIIIIIII?II??????++==+==+?III??IIII7IIIIIIIIIII7IIIII??IIIIIIIII+??III+?IIII?=:...
		..==+??II+IIIIII??I?IIII?IIIIIIIIIIIIIII7II7I7IIIIIII??III????I?III7I7I7I7IIII7IIIIIIIIIIIII??I??IIIIIIIIIII?IIII??+~...
		...+=?II??IIIIIII???II?IIIIIIIIIIIIIII77?I7I7IIII7I7IIIII????II77III77I7I7III777II7IIIII?IIII+???IIIII?II?II?III??++....
		...+++?III=I?IIIIII??IIIIIIIIIIIII???+??III??IIIIIIII7IIIII??III77I777777I7II77IIIII?II?IIIIII+IIIIIIIII?III?IIII?+,....
		"""
		print "You find yourself floating above your own body.\nLooking down, you see yourself mutilated on the floor next to the young woman, who's name you never knew.\nYou float higher and higher and feel like you are drifting off to sleep.\nYou are dead."

	elif door == "BREAK DOWN THE DOOR":
		print "You run into the door repeatedly.\nEach time, you feel more blood run down your shoulder.\nIn your struggle to get in, you suffer serious injuries and soon pass out from the pain and loss of blood."
		time.sleep(1)
		print "You slowly blink, coming to..."
		time.sleep(1)
		print "..."
		time.sleep(1)
		print "... You slowly get up, the pain in your shoulder spreading throughout your body.\nYou find the door open."
		print "The house is empty, save for a large pool of blood on the old, wooden floorboards."
		print "You leave back down the hill in search of medical attention."

	else:
		print "You were confused and waited too long.\nThe screams die down and you smell a strange odor before passing out."
		time.sleep(2)
		print "You slowly blink, coming to..."
		time.sleep(2)
		print "..."
		time.sleep(1)
		print "... You slowly get up, confused at what happened.\nYou find the door to the house open."
		print "The house is empty, save for a large pool of blood on the old, wooden floorboards."
		print "You leave back down the hill in search of help."

elif bravery == "RETREAT":
	print "You find yourself lacking any semblance of bravery.\nTerrified, you crawl back down the hill a coward."

else:
	print "You are terrified and confused. Overwhelmed with fear, you pass out on the side of the hill."
	time.sleep(2)
	print "You slowly blink, coming to..."
	time.sleep(2)
	print "..."
	time.sleep(1)
	print "... You slowly get up, confused at what happened.\nYou find the door to the house open."
	print "The house is empty, save for a large pool of blood on the old, wooden floorboards."
	print "You leave back down the hill in search of help."


