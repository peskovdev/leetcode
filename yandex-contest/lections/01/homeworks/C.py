"""
Телефонные номера в адресной книге мобильного телефона имеют один из следующих форматов:
    +7<код><номер>,
    8<код><номер>,
    <номер>,
где <номер> — это семь цифр, а <код> — это три цифры или три цифры в круглых скобках.
Если код не указан, то считается, что он равен 495. Кроме того, в записи телефонного номера может
стоять знак “-” между любыми двумя цифрами (см. пример). На данный момент в адресной книге телефона
Васи записано всего три телефонных номера, и он хочет записать туда еще один.
Но он не может понять, не записан ли уже такой номер в телефонной книге.
Помогите ему! Два телефонных номера совпадают, если у них равны коды и равны номера.
Например, +7(916)0123456 и 89160123456 — это один и тот же номер.
"""


def tidy_number(number: str):
    number = number.replace("-", "").replace("(", "").replace(")", "")
    if len(number) == 7:
        return f"+7495{number}"

    if number[0] == "8":
        number = f"+7{number[1:]}"
    return number


def solution(existed_numbers, new_number):
    for number in existed_numbers:
        if new_number == number:
            print("YES")
        else:
            print("NO")


def main():
    new_number = tidy_number(input())

    existed_numbers = []
    for _ in range(3):
        existed_numbers.append(tidy_number(input()))

    solution(existed_numbers, new_number)


# main()


print("=====================1======================")
numbers = [
    "+7-4-9-5-43-023-97",
    "4-3-0-2-3-9-7",
    "8-495-430",
]
solution([tidy_number(number) for number in numbers], tidy_number("8(495)430-23-97"))


print("=====================2======================")
numbers = [
    "83341994118",
    "86406361642",
    "83341994118",
]
solution([tidy_number(number) for number in numbers], tidy_number("86406361642"))


print("=====================3======================")
numbers = [
    "+78047952807",
    "+76147514928",
    "88047952807",
]
solution([tidy_number(number) for number in numbers], tidy_number("+78047952807"))
