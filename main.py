from flask import Flask
import math

app = Flask(__name__)

@app.route('/')
def hello():
    str ='''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>calc</title>
</head>
<body>
    <p>Для базовых функций калькулятора вводить значения с помощью /default/</p>
    <p>Функционал:</p>
    <p>1.Сложение (Пример: https://terehoffeg27.pythonanywhere.com/default/1+1)</p>
    <p>2.Вычитание (Пример:  https://terehoffeg27.pythonanywhere.com/default/1-1)</p>
    <p>3.Умножение (Пример:  https://terehoffeg27.pythonanywhere.com/default/2*1)</p>
    <p>4.Деление (Пример:  https://terehoffeg27.pythonanywhere.com/default/1:1)</p>
    <p>5.Квадратный корень (Пример:  https://terehoffeg27.pythonanywhere.com/default/sqrt4)</p>
    <p>6.Степень (Пример:  https://terehoffeg27.pythonanywhere.com/default/2**2)</p>
    <p>7.Целочисленное деление (Пример:  https://terehoffeg27.pythonanywhere.com/default/3::2)</p>
    <p>8.Остаток от деления(Пример:  https://terehoffeg27.pythonanywhere.com/default/3!2)</p>
    <p>2.Для тригонометрических функций калькулятора вводить значения с помощью /trig/</p>
    <p>Функционал:</p>
    <p>1.Синус (Пример:  https://terehoffeg27.pythonanywhere.com/trig/sin1)</p>
    <p>2.Косинус (Пример:  https://terehoffeg27.pythonanywhere.com/trig/cos1)</p>
    <p>3.Тангенс (Пример: https://terehoffeg27.pythonanywhere.com/trig/tg1)</p>
    <p>4.Котангенс (Пример:  https://terehoffeg27.pythonanywhere.com/trig/ctg1)</p>
    <p>5.Арксинус (Пример: https://terehoffeg27.pythonanywhere.com/trig/asin1)</p>
    <p>6.Арккосинус (Пример:  https://terehoffeg27.pythonanywhere.com/trig/acos1)</p>
    <p>7.Для конвертации в радианы или градусу (Пример: https://terehoffeg27.pythonanywhere.com/trig/acos 1 rad/grad
</body>
</html>
'''
    return str

@app.route('/default/<do>')
def calc_default(do:str) -> str:
    try:
        if ":" in do:
            do = do.replace(":","/")
        elif "sqrt" in do:
            do = do.replace("sqrt", "")
            if do.isnumeric():
                return f"sqrt({do}) = {str(math.sqrt(float(do)))}"
            else:
                return "Ошибка"
        elif "::" in do:
            do=do.replace("::","//")
        elif "!" in do:
            do=do.replace("!","%")
        return f"{do} = {str(eval(do))}"
    except:
        return "Некорректный ввод"


@app.route('/trig/<do>')
def calc_trig(do: str) -> str:
    try:
        parts = do.split()
        result = ""
        if "deg" in do:
            value = float(parts[1])/360 * math.pi * 2
        else:
            value = parts[1]
        if 'sin' in do:
            if -10000 <= float(value) <= 10000:
                result = math.sin(float(value))
            else:
                return "Некорректный ввод"
            return f"{do} = {result}"

        elif 'cos' in do:
            if -10000 <= float(value) <= 10000:
                result = math.cos(float(value))
            else:
                return "Некорректный ввод"
            return f"{do} = {result}"

        elif 'ctg' in do:
            result = math.cos(float(value) / math.sin(float(value)))
            return f"{do} = {result}"


        elif 'tg' in do:
            result = math.tan(float(value))
            return f"{do} = {result}"

        elif 'acos' in do:
            if -1 <= float(value) <= 1:
                result = math.acos(float(value))
            else:
                return "Некорректный ввод"
            return f"{do}={result}"
        elif 'asin' in do:
            if -1 <= float(value) <= 1:
                result = math.asin(float(value))
            else:
                return "Некорректный ввод"
            return f"{do}={result}"


    except:
         return "Некорректный ввод"




#https://terehoffeg27.pythonanywhere.com/default