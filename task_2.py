import turtle


def koch_curve(
    pen: turtle.Turtle,
    length: float,
    level: int
) -> None:
    """
    Рекурсивно малює одну сторону кривої Коха.
    """
    if level == 0:
        pen.forward(length)
        return

    segment = length / 3

    koch_curve(
        pen,
        segment,
        level - 1
    )

    pen.left(60)

    koch_curve(
        pen,
        segment,
        level - 1
    )

    pen.right(120)

    koch_curve(
        pen,
        segment,
        level - 1
    )

    pen.left(60)

    koch_curve(
        pen,
        segment,
        level - 1
    )


def draw_snowflake(
    level: int,
    length: float = 400
) -> None:
    """
    Малює сніжинку Коха з трьох кривих.
    """
    screen = turtle.Screen()

    screen.title(
        f"Сніжинка Коха — рівень {level}"
    )

    pen = turtle.Turtle()

    pen.speed(0)
    pen.hideturtle()

    # Початкова позиція для центрування малюнка
    pen.penup()
    pen.goto(
        -length / 2,
        length / 3
    )
    pen.pendown()

    for _ in range(3):

        koch_curve(
            pen,
            length,
            level
        )

        pen.right(120)

    screen.mainloop()


def main() -> None:
    try:
        level = int(
            input(
                "Введіть рівень рекурсії: "
            )
        )

        if level < 0:
            print(
                "Рівень рекурсії не може "
                "бути від'ємним."
            )
            return

        draw_snowflake(level)

    except ValueError:
        print(
            "Помилка: необхідно ввести "
            "ціле число."
        )


if __name__ == "__main__":
    main()