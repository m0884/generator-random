from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    
    if request.method == 'POST':
        try:
            min_num = int(request.form['min'])
            max_num = int(request.form['max'])
            
            if min_num >= max_num:
                result = "Ошибка: минимальное число должно быть меньше максимального"
            else:
                random_number = random.randint(min_num, max_num)
                result = f"Случайное число: {random_number}"
                
        except ValueError:
            result = "Ошибка: введите корректные числа"
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)