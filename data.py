from classes import Autor, Articulo, Volumen, RevistaCientifica


def data():
    autor1 = Autor("María", "Zapatero", "autor1@example.com", "0000-0001-2345-6789")
    autor2 = Autor("Antonio", "Acedo", "autor2@example.com", "0000-0002-3456-7890")
    autor3 = Autor("Science", "", "autor3@example.com", "0000-0003-4567-8901")
    autor4 = Autor("Conversus", "", "autor4@example.com", "0000-0004-5678-9012")
    autor5 = Autor("Science & Technology", "", "autor5@example.com", "0000-0005-6789-0123")
    autor6 = Autor("Investigación y Ciencia", "", "autor6@example.com", "0000-0006-2314-8764")
    autor7 = Autor("Autor", "Prueba", "autor7@example.com", "0000-0007-9780-2321")

    resumen1 = ("La astronomía es una fascinante disciplina científica que estudia los astros y fenómenos celestes que "
                "se encuentran más allá de la atmósfera terrestre. Desde tiempos inmemoriales, el ser humano ha "
                "mirado al cielo en busca de respuestas sobre el origen y la naturaleza del universo. A lo largo de "
                "la historia, la astronomía ha evolucionado desde las observaciones a simple vista hasta la "
                "sofisticada tecnología de telescopios y sondas espaciales.")

    resumen2 = ("La ciencia es un proceso continuo de exploración, descubrimiento y comprensión del mundo que nos "
                "rodea. A través de la observación, la experimentación y el razonamiento lógico, los científicos "
                "buscan desentrañar los misterios de la naturaleza, desde las leyes fundamentales del universo hasta "
                "los intrincados detalles de la vida en la Tierra.")

    resumen3 = ("La nanotecnología es un campo de la ciencia y la ingeniería que se centra en la manipulación y "
                "control de la materia a una escala extremadamente pequeña, a nivel de átomos y moléculas. Al "
                "trabajar en esta escala nanométrica, los científicos pueden crear materiales con propiedades únicas "
                "y desarrollar tecnologías innovadoras con aplicaciones en una amplia gama de campos.")

    resumen4 = ("La ciencia y la tecnología son dos campos interrelacionados que han transformado radicalmente la "
                "forma en que vivimos, trabajamos y nos relacionamos. La ciencia, a través de la observación, "
                "experimentación y análisis, busca comprender el mundo que nos rodea, desde los componentes más "
                "pequeños de la materia hasta los vastos confines del universo. Esta comprensión se traduce en "
                "conocimientos fundamentales sobre la naturaleza y sus leyes, lo que a su vez impulsa el avance "
                "tecnológico.")

    resumen5 = ("La vida artificial es un campo fascinante de la ciencia que se enfoca en la creación y estudio de "
                "sistemas biológicos sintéticos que imitan características de los organismos vivos. A través de la "
                "combinación de la biología, la informática, la ingeniería y la química, los investigadores buscan "
                "comprender los principios fundamentales de la vida y desarrollar nuevas formas de vida artificial "
                "con aplicaciones innovadoras.")

    articulo1 = Articulo("Astronomía", [autor1, autor2], ["astronomía", "universo"], resumen1, 100, "Aceptado para publicación", "./covers/cover5.jpg")
    articulo2 = Articulo("Ciencia", [autor3], ["ciencia"], resumen2, 200, "Aceptado para publicación", "./covers/cover6.jpg")
    articulo3 = Articulo("Nanotecnología", [autor4], ["ingeniería", "átomo"], resumen3, 150, "Aceptado para publicación", "./covers/cover2.jpg")
    articulo4 = Articulo("Rise of Intelligent Machines: Al & Robotics", [autor5], ["ciencia", "tecnología"], resumen4, 150, "Rechazado", "./covers/cover4.jpg")
    articulo5 = Articulo("Vida Artificial", [autor6], ["artificial", "sistemas"], resumen5, 150, "Pendiente de evaluación", "./covers/cover1.jpg")

    volumen1 = Volumen("Volumen 1")
    volumen1.agregar_articulo(articulo1)
    volumen1.agregar_articulo(articulo2)

    volumen2 = Volumen("Volumen 2")
    volumen2.agregar_articulo(articulo3)

    volumen3 = Volumen("Volumen 3")

    revista = RevistaCientifica()
    revista.agregar_volumen(volumen1)
    revista.agregar_volumen(volumen2)
    revista.agregar_volumen(volumen3)


    return revista
