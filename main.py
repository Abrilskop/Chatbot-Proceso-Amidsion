import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Hola', ['hola', 'BUENOS DIAS', 'saludos', 'buenas'], single_response = True)
        response('MODALIDAD', ['cronograma', 'ADMISION', 'CUANDO', 'PROCESO', 'INFORMACION', 'EXAMEN'], single_response=True)
        response('Domingo, 29 de diciembre de 2024', ['ordinario'], single_response=True)
        response('Domingo, 24 de noviembre de 2024', ['secundaria', 'primera opcion'], single_response=True)
        response('Foto de DNI, constancia, foto actualizada, pago por derechos', ['requisitos'], single_response=True)
        response('Sede Cusco: 509, Filiales: 316', ['cuanto es el pago','monto','pagar'], single_response=True)
        response('visita la pagina oficial', ['resultados','notas','ingresantes'], single_response=True)

            # Respuestas sobre nota mínima para ingresar
        response('La nota mínima para ingresar a Ingeniería de Sistemas es 14.',
                ['nota minima', 'ingenieria', 'sistemas'], required_words=['nota'])

        response('La nota mínima para ingresar a Ingeniería Civil es 13.',
                ['nota mínima', 'ingeniería', 'civil'], required_words=['nota'])

        response('La nota mínima para ingresar a Ingeniería Ambiental es 12.',
                ['nota mínima', 'ingeniería', 'ambiental'], required_words=['nota'])

        response('La nota mínima para ingresar a Economía es 13.',
                ['nota mínima', 'economía'], required_words=['nota'])

        response('La nota mínima para ingresar a Ingeniería Industrial es 14.',
                ['nota mínima', 'ingeniería', 'industrial'], required_words=['nota'])

        response('La nota mínima para ingresar a Arquitectura es 15.',
                ['nota mínima', 'arquitectura'], required_words=['nota'])

        # becas
        response('Hay diferentes tipos de becas disponibles según el rendimiento académico. Consulta la página oficial para más detalles.',
                ['becas', 'ayuda', 'financiera'], required_words=['becas'])

        response('Las clases comenzarán el 1 de marzo de 2025. Asegúrate de estar inscrito a tiempo.',
                 ['inicio', 'clases'], required_words=['inicio'])

        response('Las vacantes para cada carrera pueden variar. Consulta la página de admisión para más detalles.',
                 ['vacantes', 'carreras'], required_words=['vacantes'])

        response('Hay becas disponibles para estudiantes destacados. Consulta los requisitos en la página de becas.',
                 ['becas', 'ayuda', 'financiera'], required_words=['becas'])

        response('Puedes realizar consultas en la oficina de admisiones de lunes a viernes de 8 a 16 horas.',
                 ['consultas', 'oficina'], required_words=['oficina'])

        response('Recomendamos prepararte con antelación para el examen. Hay materiales de estudio disponibles en línea.',
                 ['preparación', 'examen'], required_words=['preparación'])

        response('Recibirás un correo electrónico con la confirmación de tu inscripción una vez que completes el proceso.',
                 ['confirmación', 'inscripción'], required_words=['confirmación'])

        response('Si tienes preguntas adicionales sobre el proceso de admisión, no dudes en preguntar aquí.',
                 ['preguntas', 'admisión'], required_words=['preguntas'])

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)


        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'búscalo en la pagina oficial a ver que tal'][random.randrange(3)]
    return response

while True:
    print("Bot: " + get_response(input('You: ')))