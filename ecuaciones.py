from sympy import symbols, solve, diff, Eq

def despejar(update, context):
    equation = update.message.reply_to_message.text
    equation = equation.replace('^', '**')  # Reemplazar el operador '^' por '**'

    # Verificar si la ecuación contiene un signo de igualdad
    if '=' not in equation:
        context.bot.send_message(chat_id=update.effective_chat.id, text="La ecuación no contiene un signo de igualdad.")
    else:
        # Obtener la parte izquierda y derecha de la ecuación
        parts = equation.split('=')
        left_side = parts[0].strip()
        right_side = parts[1].strip()

        # Crear la ecuación con sympy
        x = symbols('x')
        eq = Eq(eval(left_side), eval(right_side))

        # Intentar resolver la ecuación
        try:
            result = solve(eq, x)

            if len(result) == 0:
                context.bot.send_message(chat_id=update.effective_chat.id, text="No se encontró una solución para x.")
            else:
                result_str = f"La ecuación con x despejada es: {result[0]}"
                if len(result) > 1:
                    result_str += f" \n(también se encontraron otras soluciones: {result[1:]})"

                context.bot.send_message(chat_id=update.effective_chat.id, text=result_str)
        except:
            context.bot.send_message(chat_id=update.effective_chat.id, text="No se pudo despejar la ecuación.")

def derivar(update, context):
    equation = update.message.reply_to_message.text

    # Intentar calcular la derivada de la ecuación
    try:
        x = symbols('x')
        derivative = diff(equation, x)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"La derivada de la ecuación es: {derivative}")
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="No se pudo calcular la derivada de la ecuación.")
