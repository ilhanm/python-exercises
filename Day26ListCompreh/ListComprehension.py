a=[1,2,3,4,5,6,7,8]

b=[i+1 for i in a]
print(b)

b=[i for i in a if i%2==0]
print(b)
premier_league="liverpool,chelsea,leicester,manchester,birmingham,arsenal,everton"
europa_cup='barcelona,psg,liverpool,benfica,everton,porto,chelsea,arsenal,sevilla,napoli'
b=[i+" !" for i in premier_league.split(",") if i in europa_cup.split(",")]
print(b)
print(list("Angela"))

mylist=[i*2 for i in range(1,5)]
print(mylist)

sentence="hello my name is ilhan"
words=sentence.split()
x=" ".join([word.capitalize() for word in words])

print(x)


numbers1=[1,2,3,2,1,4,5,7,8,9,5,3,2,24,4,6,7,5,4,3,7,9,0,12,23,321]
numbers2=[3,4,5,6,3,2,1,4,6,7,8,4,34,1,12,5,321,11,23]

print([i for i in set(numbers1) if i in set(numbers2)])