"""

Dasturlash asoslari

#08-dars: Ro'yxatlar bilan ishlash

Muallif: Murodjon Sadullaev

"""
#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar = ["O'zbekiston","Qozog'iston", "Rossiya", "Malayziya", "Singapur", "AQSh"]
print(davlatlar)

#Ro'yxatning uzunligini konsolga chiqaring
print(len(davlatlar))

#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(davlatlar))

#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(sorted(davlatlar, reverse=True))

#Asl ro'yxatni qaytadan konsolga chiqaring
print(davlatlar)

#reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()
print(davlatlar)

#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
sonlar = list(range(120,1200))

#Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print(sum(sonlar))

#Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
print(max(sonlar)-min(sonlar))

#Ro'yxatdagi elementlar sonini hisoblang
print(len(sonlar))

#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[530:550])

#taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['osh','somsa','norin','shashlik','qozonkabob']

#nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]

#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove('norin')
nonushta.remove('shashlik')
nonushta.remove('qozonkabob')
nonushta.append('non va qaymoq')
nonushta.append('issiq non')

#Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(taomlar)
print(nonushta)

#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non"

"""

1. O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring

2. Ro'yxatning uzunligini konsolga chiqaring
    sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
    sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring

3. Asl ro'yxatni qaytadan konsolga chiqaring
    reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
    sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.

4. 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing

5. Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring

6. Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring

7. Ro'yxatdagi elementlar sonini hisoblang

8. Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring

9. taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting

10. nonushta degan yangi ro'yxatga taomlardan nusxa oling

11. Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing

12. Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring

13. Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.

"""