s = "AbrakadabraAbrakadabra"
str = "bra"
print(s.find(str))
print(s.rfind(str))
print(s.find("add"))

#count(sub[str,start,end])
print(s.count(str))
print(s.count(str,4))
print(s.count(str,4,16))

# split()
# Contact was added: egdfukw3574632483pjfskjdfj;sldlfg'd
print("****************************")
s = 'Cat, Dog, Monster Rabbit, Pig'
print(s.split())
print(s.split(','))
print(s.split(',',3))


#*************************************
#rjust() & lJust()
s = 'Hi!'
print(s.rjust(10,'*'))
print(s.ljust(10,'#'))

test = ["Login","Cart","API"]
for t in test:
    print(t.ljust(15),"OK")

order = "125"
print(order.rjust(8, "0"))

#****************************************
s = 'AbrakaDaAbrakaDabra1'
print(s.isalpha())
print(s.isdigit())


#index()
text = "QA automation with Python"
pos  = text.index("automation")
print(pos)

#******************
#replace()
text1 = "I like Python"
print(text1.replace("Python","Python and Coffee"))


text  = "2026-07-03"
new_text = text.replace("-","/")
print(new_text)