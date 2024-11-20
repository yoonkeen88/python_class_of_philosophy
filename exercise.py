#### python class of philosophy
### week 11 class is string
# s = input("생년월일을 입력해주세요(년/월/일):").split("/")


# if len(s[0])>5 or len(s[1])>3 or len(s[2])>3: 
#     print("ReEnter your birth")
# elif int(s[1]) > 13 or int(s[2])>31:
#     print("ReEnter your birth")
# else: 
#     print(f"귀하는 {s[0]}년 {s[1]}월 {s[2]}일생 입니다.")

# a = ["banana", "a","b"]
# a = ",".join(a)
# print(a.count("."))

##startswith("something") methond
# ## endswith() methond
# # print(a.startswith("a"), a.endswith("b"))
# # print(a.upper(), a.lower())

# # ## replace(a,b)
# # print(a.replace("b", "a"))

# ## strip() 디폴트는 좌우 공백 삭제
# print(",H e l l o , w o r ld,".strip(","))
# print(",Jaaa,".lstrip(","))
# print(",aa,a,".rstrip(","))

# ## find() index 와 같은 기능을 하지만 없으면 -1을 반환하기에 find 가 좋음 pop(), get()차이랑 비슷
# ## index?
# print("aaba".index("a"))
# print("aaaba".find("c"))

# print("aaabbb".index("d")) # 이렇게 하면 에러가 뜸
# ## r-string 은 익스케이프 문자를 그대로 출력
# print(r"\n\t 익스케이프 문자가 그대로 보인다")
# ## f-string 은 중간에 {} 를 넣어 변수를 그대로 출력
# a = 10
# print(f"다음 중괄호 값은 변수가 들어감{a}")

# st = "Hello this is the exam for the test of stop words and count the words"
# print(st.count("e"))
# words = st.split()

# print(f"mean of the words's length: {round(sum(len(word) for word in words ) / len(words), 3)}") # round(a, n)으로 소숫점 출력 제한
## "{:.f3}".format(a) 로 a 를 3째 자리까지 출력

## 불용어 제거는 nltk

## Twitter
s = "It's Not The Right Time To Conduct Exams. MY DEMAND IN BOLD AND CAPITAL. NO EXAM IN COVID!!!"

print(f"Entered = {s}")
count = 0
for word in s.split():
    if(word == word.upper()):
        count +=1 
print(f"\n대문자 단어의 수 = {count}")
t = s.lower().replace("!", "").replace(".", "").replace("'","")
print(f"Result: {t}")

