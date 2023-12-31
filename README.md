Программа на языке Python, для вычисления Fn (числа Фибоначчи от n). 

Имеется возможность вычисления за $O(N)$ и $O(\log N)$.

### Инструкция
1. Клонировать репозиторий
```bash
git clone https://github.com/VladSatyshev/fibonacci.git
```
2. Зайти в корень проекта
```bash
cd fibonacci
```
3. Запустить программу в соответствии с примерами:

Вычисление 100го числа Фибоначчи за $O(N)$
```bash
python fib.py -n 100 -a N
```

Вычисление 100го числа Фибоначчи за $O(\log N)$
```bash
python fib.py -n 100 -a LogN
```

Выполнить тесты
```bash
python fib.py --test
```

### Дополнительно
Общие комментарии к программе находятся в [файле](https://github.com/VladSatyshev/fibonacci/blob/main/md/prog_comments.md).

Пояснение алгоритма вычисления числа Фибоначчи за $O(\log N)$ находится в [файле](https://github.com/VladSatyshev/fibonacci/blob/main/md/logN_explanation.md).
