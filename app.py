import random
import math

# your code here
who = ['the dog','my granma','his turtle','my bird']
what = ['eat','pissed','crushed','broked']
when = ['before the class','right in time','when I finished','during my lunch','while I was praying']

len_Who = len(who)
len_What = len(what)
len_When = len(when)

rnd_who = random.randrange(0,len_Who)
rnd_what = random.randrange(0,len_What)
rnd_when = random.randrange(0,len_When)

excuse = str(who[rnd_who]) + " " + str(what[rnd_what]) + " " + str(when[rnd_when])
print(str(excuse))