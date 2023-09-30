# Программа "ExcelHelper"

## Описание

<image src="documentation_image\ExcelHelper.png" alt="ExcelHelper">
<image src="documentation_image\DUO ExcelHelper.png" alt="ExcelHelper">

* Программа была сделана для одной компании, для уменьшения времени создания отчетности

Программа "ExcelHelper" служит облегчить работу с excel файлами. Данная программа ищет
в excel файле столбцы "Увеличение" и "Уменьшение" и выделяет идентичные числа голубым
цветом, а два числа из одного столбца в сумме дающие число из другого столбца выделяются
серым цветом.

<image src="documentation_image\Preview processing ExcelHelper.png" alt="ExcelHelper">

## Возможности

Данная программа позволяет быстро и эффективно обработать excel файлы и сохранить в 
любое удобное для вас месте в формате .xlsx

Поддерживаемые форматы:

* .xlsx
* .xls

Помимо обработки файла программа может защитить данный файл от изменений. Доступно три 
варианта защиты файла.

* Защита изменения структуры таблицы
* Защита отслеживания истории изменений
* Защита листа от изменений

<image src="documentation_image\Preview security.png" alt="ExcelHelper">

Для этого нужно выбрать соответствующую кнопку перед обработкой файла.

Из дополнительных возможностей можно установить темную или светлую тему на выбор, 
а также установить зеленое или синее оформление.

<image src="documentation_image\Preview theme.png" alt="ExcelHelper">

### Горячие клавиши 

Для быстрой и удобной работы с программой, есть ряд горячих клавиш:

1. Ctrl + W - Выбор пути к файлу
2. Ctrl + E - Выбор путь для сохранения файла
3. Ctrl + Enter - Запуск обработки файла
4. Ctrl + Q - Открытие Информационного меню
5. Ctrl + R - Закрытие Информационного меню
6. Ctrl + A - Столбцы с данными "5 и 7"
7. Ctrl + F - Столбцы с данными "6 и 8"
8. Ctrl + Z - Столбцы с данными "Другое"
9. Ctrl + X - Выбор сохранения файла "По умолчанию"
10. Ctrl + C - Выбор сохранения файла "Заменить исходное"
11. Ctrl + D - Установка темной темы
12. Ctrl + L - Установка светлой темы
13. Ctrl + S - Установка темы как в системе
14. Ctrl + G - Установка зеленого оформления
15. Ctrl + B - Установка синего оформления

## Установка

1. Клонируйте репозиторий с github
2. Создайте виртуальное окружение 
3. Установите зависимости `pip install -r requirements.txt`
4. Запустите программу командой `python3 Interface_window.py`

## Используемые материалы

Иконки программы - <https:/www.flaticon.com>

## Примеры

1. [Оригинальный excel файл](https://github.com/ProgMaksim/ExcelHelper/blob/master/Materials/Не_обработанная_таблица.xlsx)
2. [Обработанный excel файл](https://github.com/Prog-Maksim/ExcelHelper/blob/master/Materials/Обработанная_таблица.xlsx) 
