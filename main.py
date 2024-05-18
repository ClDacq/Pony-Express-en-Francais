PlACEHOLDER = '[name]'


with open('input/Names/invites_a_la_fete') as names_file:
    marshals = names_file.readlines()
    print(marshals)

with open('./input/letters/message.txt') as letter_file:
    contenu_du_message = letter_file.read()
    for name in marshals:
        pierre = name.strip()
        nouveau_message = contenu_du_message.replace(PlACEHOLDER, pierre)
        with open(f'./output/Pony_Is_Antsy/message_pour_{pierre}.txt', mode='w') as message_termine:
            message_termine.write(nouveau_message)
