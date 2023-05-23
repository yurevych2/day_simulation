# day_simulation
Лабораторна робота з дискретної математики. Моделяція життя за допомогою скінченних автоматів.

# Архітектура
Автомат складається з п'яти станів. Діаграма зображена у файлі diagram.png. День починається зі сну і є трьох варіантів. Рандомно ви можете проспати на годину або дві. Далі треба доїхати до УКУ, але якщо не пощастить і автобус не приїде, то доведеться йти пішки і витратити годину. Пари закінчуються о 15:00 після чого є обідня перерва (2 години). Далі треба доїхати додому. Вдома ви сідаєте дивитися Нетфлікс, але не знаєте, скільки це часу займе. Якщо серіал виявиться цікавим, то 3 години, як ні, то одну. Вечеря і нічний сон.

# Приклад
Щоб почати, треба запустити файл main.py і ввести кількість днів, яку хочете змоделювати.

Приклад роботи:
_____________________________________
Enter number of days to simulate.
3.
_____________________________________
sleep.
sleep.
sleep.
sleep.
sleep.
sleep.
sleep.
_____________________________________
O`clock: 7

Wow! On time. Let`s grab a bite!
_____________________________________
O`clock: 7

Commuting to UCU.
_____________________________________
O`clock: 8

Classes time... Yay...
_____________________________________
O`clock: 15

Classes ended.
_____________________________________
O`clock: 15

Finally, lunch!
_____________________________________
O`clock: 17

Commuting home!
Yoooo, bus!
_____________________________________
O`clock: 17

Let`s relax and watch some Ntflix.
Wow! What wonderful series!
_____________________________________
O`clock: 20

Dinner is... Ok. Now I want to sleep.
_____________________________________
sleep.
sleep.
sleep.
sleep.
sleep.
sleep.
sleep.
_____________________________________
O`clock: 9

F*CK! I have passed a class! I have to run.
_____________________________________
O`clock: 9

Commuting to UCU.
Yoooo, bus!
_____________________________________
O`clock: 9

Classes time... Yay...
_____________________________________
O`clock: 15

Classes ended.
_____________________________________
O`clock: 15

Finally, lunch!
_____________________________________
O`clock: 17

Commuting home!
_____________________________________
O`clock: 18

Let`s relax and watch some Ntflix.
Ehh... Nothing especial...
_____________________________________
O`clock: 19

Dinner is... Ok. Now I want to sleep.
_____________________________________
sleep.
sleep.
sleep.
sleep.
sleep.
sleep.
sleep.
_____________________________________
O`clock: 8

Shit. One hour later... Don`t have time for breakfast.
_____________________________________
O`clock: 8

Commuting to UCU.
Yoooo, bus!
_____________________________________
O`clock: 8

Classes time... Yay...
_____________________________________
O`clock: 15

Classes ended.
_____________________________________
O`clock: 15

Finally, lunch!
_____________________________________
O`clock: 17

Commuting home!
_____________________________________
O`clock: 18

Let`s relax and watch some Ntflix.
Wow! What wonderful series!
_____________________________________

O`clock: 21

Dinner is... Ok. Now I want to sleep.
_____________________________________
sleep.
sleep.
sleep.
_____________________________________
Simulation is ended.
