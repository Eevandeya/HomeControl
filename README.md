# HomeControl

### Что это?
Телеграм бот на `aiogram`.
Бот создавался для "родительского контроля" несколько лет назад.
По сути он является обычным редактором списков,
в котором админы создают списки, а юзеры могут в них отмечать
статусы заданий.

### Взгляд сейчас
Сейчас прикрутил бы СУБД, вместо текстовых файлов,
улучшил бы безопасность, улучшил бы файловую структуру проекта
(текущая никуда не годится) и в целом бы поработал над 
стилем и структурой кода,
признаюсь, сейчас он выглядет страшненько.
### Как пользоваться
1. Токен добавить в переменную окружения `TOKEN`.
2. В файле `users.py` добавить пользователей (админов и юзеров).
