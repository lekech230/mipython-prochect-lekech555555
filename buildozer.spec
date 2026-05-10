[app]

# Название приложения и пакадж
title = My Pygame Game
package.name = mygame
package.domain = org.example

# Путь к исходникам
source.dir = .
source.include_exts = py,png,jpg,ttf,wav,mp3

# ВАЖНО: Зависимости
# Мы используем pygame, а sdl2 библиотеки нужны для звука и шрифтов
requirements = python3, pygame, sdl2_ttf, sdl2_image, sdl2_mixer

# Версия
version = 0.1

# Ориентация экрана (portrait - вертикальная, landscape - горизонтальная)
orientation = portrait

# Иконка (если есть, укажи путь)
#icon.filename = icon.png

# Полноэкранный режим
fullscreen = 1

# (Android specific)
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Минимальная и целевая версии SDK (обычно менять не нужно)
android.api = 33
android.minapi = 21
android.ndk = 25b

[buildozer]
# Уровень логирования (2 — чтобы видеть ошибки, если сборка упадет)
log_level = 2
warn_on_root = 1
