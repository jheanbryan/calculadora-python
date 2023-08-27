import PySimpleGUI as sg

sg.theme('Python')

layout = [  
            [sg.InputText()],
            [sg.Button('CE')],[sg.Button('C')], [sg.Button('X')], [sg.Button('/')]
            [sg.Button('7')],[sg.Button('8')], [sg.Button('9')], [sg.Button('X')]
            [sg.Button('4')],[sg.Button('5')], [sg.Button('6')], [sg.Button('-')]
            [sg.Button('1')],[sg.Button('2')], [sg.Button('3')], [sg.Button('+')]
            [sg.Button('()')],[sg.Button('0')], [sg.Button('.')], [sg.Button('=')]
        ]   

window = sg.Window('Calculadora', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('You entered ', values[0])

window.close()