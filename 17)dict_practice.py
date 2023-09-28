                                                                #
from collections import defaultdict

info = {'Name': 'Arseny', 'SecondName': 'Cheplukov', 'age': 17}
print(info)

phone = {'Name': None, 'Company': None, 'OS': None, 
        'Version': None, 'Memory': None}
phone['Name'] = 'A31'
phone['Company'] = 'Gnusmus'
phone['OS'] = 'Android'
phone['Version'] = 10.0
phone['Memory'] = 128
print(phone)

text = """
Delicate omens traced in air
To the lone bard true witness bare;
Birds with auguries on their wings
Chanted undeceiving things
Him to beckon, him to warn;
Well might then the poet scorn
To learn of scribe or courier
Hints writ in vaster character;
And on his mind, at dawn of day,
Soft shadows of the evening lay.
For the prevision is allied
Unto the thing so signified;
Or say, the foresight that awaits
Is the same Genius that creates.
FATE.
It chanced during one winter, a few years ago, that our cities were bent on discussing the theory of the Age.
By an odd coincidence, four or five noted men were each reading a discourse to the citizens of Boston or New York,
on the Spirit of the Times. It so happened that the subject had the same prominence in some remarkable pamphlets
and journals issued in London in the same season. To me, however, the question of the times resolved itself into a practical question of the conduct of life. How shall I live? We are incompetent to solve the times. Our geometry cannot span the huge orbits of the prevailing ideas,
behold their return, and reconcile their opposition. We can only obey our own polarity.
'Tis fine for us to speculate and elect our course, if we must accept an irresistible dictation.
In our first steps to gain our wishes, we come upon immovable limitations. We are fired with the hope to reform men. After many experiments, we find that we must begin earlier,—at school. But the boys and girls are not docile; we can make nothing of them. We decide that they are not of good stock. We must begin our reform earlier still,—at generation: that is to say, there is Fate, or laws of the world.
But if there be irresistible dictation, this dictation understands itself. If we must accept Fate, we are not less compelled to affirm liberty, the significance of the individual, the grandeur of duty, the power of character. This is true, and that other is true. But our geometry cannot span these extreme points, and reconcile them. What to do? By obeying each thought frankly, by harping, or, if you will, pounding on each string, we learn at last its power. By the same obedience to other thoughts, we learn theirs, and then comes some reasonable hope of harmonizing them. We are sure, that, though we know not how, necessity does comport with liberty, the individual with the world, my polarity with the spirit of the times. The riddle of the age has for each a private solution. If one would study his own time, it must be by this method of taking up in turn each of the leading topics which belong to our scheme of human life, and, by firmly stating all that is agreeable to experience on one, and doing the same justice to the opposing facts in the others, the true limitations will appear. Any excess of emphasis, on one part, would be corrected, and a just balance would be made.
But let us honestly state the facts. Our America has a bad name for superficialness. Great men, great nations, have not been boasters and buffoons, but perceivers of the terror of life, and have manned themselves to face it. The Spartan, embodying his religion in his country, dies before its majesty without a question. The Turk, who believes his doom is written on the iron leaf in the moment when he entered the world, rushes on the enemy's sabre with undivided will. The Turk, the Arab, the Persian, accepts the foreordained fate.
"On two days, it steads not to run from thy grave,
The appointed, and the unappointed day;
On the first, neither balm nor physician can save,
Nor thee, on the second, the Universe slay."
The Hindoo, under the wheel, is as firm. Our Calvinists,
in the last generation, had something of the same dignity.
They felt that the weight of the Universe held them down to their place. What could they do?
Wise men feel that there is something which cannot be talked or voted away,—a strap or belt which girds the world.
"The Destiny, minister general,
That executeth in the world o'er all,
The purveyance which God hath seen beforne,
So strong it is, that tho' the world had sworn
The contrary of a thing by yea or nay,
Yet sometime it shall fallen on a day
That falleth not oft in a thousand year;
For, certainly, our appetites here,
Be it of war, or peace, or hate, or love,
All this is ruled by the sight above."
CHAUCER: The Knight's Tale.
"""
text_list = text.split(' ')
counter_dictionary = {}
for word in text_list:
    counter_dictionary.setdefault(word, 0)
    counter_dictionary[word] += 1
print(counter_dictionary)

