def ayuda(update, context):
    a = "Responde a un mensaje con:\n"
    b = "/esp para traducir al castellano\n"
    c = "/ing para traducir al inglés\n"
    d = "/fra para traducir al francés\n"
    e = "/rus para traducir al ruso\n"
    f = "/ita para traducir al italiano (no c muy bien) \n"
    g = "/jap para traducir al japones\n"
    h = "/ale para traducir al alemán\n"
    i = "/cor para traducir al coreano\n"
    j = "/por para traducir al portugués\n\n"
    k = "/operar para el resultado matemático (usa ^1/2 para raíz cuadrada u otras...)\n"
    l = "/despejar para el valor de x (no uses otras variables) \n"
    m = "/derivar para enviarte la derivada de f(x) (no uses otras variables, ** = ^)\n\n"
    n = "/dolares para pasar de dólares a pesos colombianos\n"
    o = "/pesos para pasar de pesos colombianos a dólares\n"
    p = "/euros para pasar de euros a pesos colombianos\n\n"
    q = "/voz para que te lo lea"
    r = "Además puedes enviar:\n"
    s = "/perro para que envíe una imagen de un perro (a veces no encuentro)\n"
    t = "/gato para que envíe una imagen de un gato\n"
    u = "/pato para que envíe una imagen de un pato (Me demoro pero siempre encuentro)\n"
  
    texto = a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u
    context.bot.send_message(chat_id=update.effective_chat.id, text =texto)
