import tkinter as tk

# Загрузка изображений
bird_images = [
    tk.PhotoImage(file="bird1.png"),
    tk.PhotoImage(file="bird2.png"),
    tk.PhotoImage(file="bird3.png")
]


def animate_bird():
    global current_image_index

    # Получаем текущее изображение
    current_image = bird_images[current_image_index]

    # Обновляем изображение на канвасе
    canvas.itemconfig(bird, image=current_image)

    # Изменяем индекс изображения для следующей итерации
    current_image_index = (current_image_index + 1) % len(bird_images)

    # Запускаем следующую итерацию анимации через 100 мс
    root.after(100, animate_bird)


# Создаем главное окно приложения
root = tk.Tk()
root.title("Анимация полета птицы")

# Создаем канвас для отображения анимации
canvas = tk.Canvas(root, width=500, height=300)
canvas.pack()

# Рисуем начальное положение птицы
x, y = 50, 150
bird = canvas.create_image(x, y, anchor='nw', image=bird_images[0])

# Индекс текущего изображения
current_image_index = 0

# Начинаем анимацию
animate_bird()

# Запуск главного цикла обработки событий
root.mainloop()