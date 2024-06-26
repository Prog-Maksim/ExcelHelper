# Программа "ExcelHelper"

## Описание

<image src="documentation_image\ExcelHelper.png" alt="ExcelHelper">
<image src="documentation_image\DUO ExcelHelper.png" alt="ExcelHelper">

* Программа была сделана для одной компании, для уменьшения времени создания отчетности.

Программа "ExcelHelper" служит облегчить работу с excel файлами. Данная программа ищет
в excel файле столбцы "Увеличение" и "Уменьшение" и выделяет идентичные числа голубым
цветом, а два числа из одного столбца в сумме дающие число из другого столбца выделяются
серым цветом.

<image src="documentation_image\Preview processing ExcelHelper.png" alt="ExcelHelper">

## Возможности

Данная программа позволяет быстро и эффективно обработать excel файлы как с компьютора так и с Google Drive и сохранить в 
любое удобное для вас месте в формате .xlsx

Поддерживаемые форматы:
* .xlsx
* .xls

Помимо обработки файла программа может защитить данный файл от изменений. Доступно три 
варианта защиты файла.

* Защита изменения структуры таблицы
* Защита отслеживания истории изменений
* Защита листа от изменений

Для этого нужно выбрать соответствующую кнопку перед обработкой файла.

Из дополнительных возможностей можно установить темную или светлую тему на выбор.

<image src="documentation_image\Theme.png" alt="ExcelHelper">

### Горячие клавиши 

Для быстрой и удобной работы с программой, есть ряд горячих клавиш:

<image src="documentation_image\HotKeys.png" alt="ExcelHelper">

## Установка

1. Клонируйте репозиторий с github командой `git clone <репозиторий>`
2. Создайте виртуальное окружение 
3. Установите зависимости `pip install -r requirements.txt`
4. Запустите программу командой `python3 UI/main.py`

## Используемые материалы

Иконки программы - <https:/www.flaticon.com>

## Примеры

1. [Оригинальный excel файл](https://github.com/Prog-Maksim/ExcelHelper/Materials/Не_обработанная_таблица.xlsx)
2. [Обработанный excel файл](https://github.com/Prog-Maksim/ExcelHelper/Materials/Обработанная_таблица.xlsx) 
