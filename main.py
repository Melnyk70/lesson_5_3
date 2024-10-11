#ДЗ 5.3. hashtag
# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
# Декілька правил:
# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.
# Приклади:
#'Python Community' -> #PythonCommunity
#'i like python community!' -> #ILikePythonCommunity
#'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes
#'t!e@s#t t%e^s&t' => #TestTest
import string
list_p=string.punctuation+string.digits
hashtag0="#"
#text=str(input("Введіть речення або девиз для майбутньої кришмітки: "))
lst='t!e@s#t t%e^s&t ghghgh 56565 ..... !!!!! yyyyy uuuuuu gjgjgjgjg djdjdjdjd djdjdjdjd llll rrrrrrrrrr ttttttttt uuuuuuuuuu aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbcdddbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
print(lst)
lst1=[]
i=0
for i in range(len(lst)):
    umova=(lst[i] in list_p)
    if not umova:
        lst1.append(lst[i])
        i=i+1
    elif umova:
        i=i+1
lst1.insert(0,hashtag0)
lst=str(''.join(lst1))
lst=lst.title()
lst=lst.replace(" ", "")
if int(len(lst))<=139:
    print(lst)
else:
    print(lst[:140])


