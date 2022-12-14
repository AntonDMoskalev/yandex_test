Тестовое задание Яндекс.Практикум
# Тестовое задание Яндекс.Практикум

### Технологии:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)

## Описание технической части проекта:

#### Скрипт принимает на вход модули Python (.py) студентов Яндекс.Практикум и проверяет правильность наименований функций, классов и методов. Возвращая значение в зависимости от результатов проверки (для демонcтрации был применён метод print).
#### Вывод: 
> 1 - True тест пройден

> 0 - False тест провален

#### Правило тестирование имен:
> Имена функци и классов - стиль CamelCase (пример HyWorld)

> Имена методов классов - стиль snake_case (привер goodbye_world). Из проверки исключены служебные "магические" методы (__init__ и тд.)

#### Тестирование скрипта:
#### В корне проекта есть папка (test) с тестовыми классами и функциями:

##### Запуск: python syntax_check.py test/test_successful.py
> test_successful.py - вернёт 1 (True)

##### Запуск: python syntax_check.py test/test_failed.py
> test_failed.py - вернёт 0 (False)

##### Запуск: python syntax_check.py test/test_successful.py test/test_failed.py
> Запустит проверку нескольких модулей

---

### Контакты:
##### [Linkedin](https://www.linkedin.com/in/anton-dev-py/)
##### [Telegram](https://t.me/MoskalevAD)
##### [GitHub](https://github.com/AntonDMoskalev)
