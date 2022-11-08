
def principal():                    #Mean Function
    submit=0
    phrase = input('Write the email message: ').strip().lower()
    sensitive_words = []


    while submit == 0:
        if phrase == '':
            inputEmail = input('Type a mail: ')                
            phrase = inputEmail

        print('')
        print('Type "commands" to show available commands.')
        print('')

        command = input('=> ')

###### List commands ##########
        if command == 'commands':
            print('')
            print('add - Adds a new word to censor.')
            print('submit - Executes the censorship of the selected words.')
            print('')

###### Add a new sensitive word/phrase ##########
        if command == 'add':
            word = input('|_ Enter a sensitive word/phrase: ')
            sensitive_words.append(word)
            for word in sensitive_words:
                frphrasease = phrase.replace(word, "*" * len(word))
                print('-' * 30)
                print(sensitive_words)

###### Submit the words/phrases in te mail and replace with * ##########
        if command == 'submit':
            for word in sensitive_words:
                phrase = phrase.replace(word, "*" * len(word))
            print('\033[1;30;41mMAIL VERIFIED: False \033[m')
            print(phrase)
            print(' ')
            print('\033[1;30;41mSensitive word: \033[m')

            print(sensitive_words)


principal()                    #call function