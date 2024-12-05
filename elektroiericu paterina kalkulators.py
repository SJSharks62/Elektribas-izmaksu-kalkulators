import PySimpleGUI as sg
import math

layout=[[sg.Text("*Elektroierīces jauda W:   ",background_color='#006E7F'), sg.Push(background_color='#006E7F') ,sg.Input(size=(21,1), key="-jauda-"),],
        [sg.Text("Ierīces izmantošanas laiks h/dienā:    ",background_color='#006E7F'), sg.Push(background_color='#006E7F') ,sg.Input(size=(21,1), key="-laiks-"),],
        [sg.Text("Elektroenerģijas cena €/kWh:   ",background_color='#006E7F'), sg.Push(background_color='#006E7F') ,sg.Input(size=(21,1), key="-cena-"),],
        [sg.Text("Ierīces izmantošanas biežums dienas/mēnesī:   ",background_color='#006E7F'), sg.Push(background_color='#006E7F') ,sg.Input(size=(21,1), key="-dienas-"),],
        [sg.Push(background_color='#006E7F'), sg.Button("Aprēķināt",font=('verdana',10,'bold'), size=(20,1), button_color = ('#0B0B45', '#999999')), sg.Push(background_color='#006E7F'),],
        [sg.Text(key="-izmantošanas laiks-",background_color='#006E7F'), sg.Push(background_color='#006E7F'),],
        [sg.Text(key="-patērētā enerģija-",background_color='#006E7F'), sg.Push(background_color='#006E7F'),],
        [sg.Text(key="-lietošanas izmaksas-",background_color='#006E7F'), sg.Push(background_color='#006E7F'),],
        [sg.Text("* Dažām elektroierīcēm jauda W nav norādīta.\n  Tomēr parasti tad ir norādīts strāvas stiprums A un spriegums V.\n  Šeit vari aprēķināt jaudu.",background_color='#006E7F'), sg.Push(background_color='#006E7F'),],
        [sg.Text("Elektroierīces spriegums V:   ",background_color='#006E7F'), sg.Push(background_color='#006E7F') ,sg.Input(size=(21,1), key="-spriegums-"),],
        [sg.Text("Ierīces strāvas stiprums A:    ",background_color='#006E7F'), sg.Push(background_color='#006E7F') ,sg.Input(size=(21,1), key="-stiprums-"),],
        [sg.Push(background_color='#006E7F'), sg.Button("Aprēķināt jaudu",font=('verdana',10,'bold'), size=(20,1), button_color=('#0B0B45', '#999999')), sg.Push(background_color='#006E7F'),],
        [sg.Text(key="-ierices jauda-",background_color='#006E7F'), sg.Push(background_color='#006E7F'),]]

window = sg.Window("  Elektroierīču patēriņa kalkulators", layout, element_justification='center',background_color='#006E7F')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Aprēķināt":
        try:
            a = float(values["-jauda-"])
            b = float(values["-laiks-"])
            h = float(values["-cena-"])
            c = float(values["-dienas-"])
            if a > 0 and b > 0 and h > 0 and c > 0:
                menesis = (b * c)
                menesisR = round(menesis,2)
                T = f"Ierīces izmantošanas laiks mēnesī: {menesisR} h"
                window["-izmantošanas laiks-"].update(T, text_color = "#F58311")
                energija = (a / 1000) * menesis
                energijaR = round(energija,2)
                U = f"Ierīces patērētā enerģija mēnesī: {energijaR} kWh"
                window["-patērētā enerģija-"].update(U, text_color = "#F58311")
                rezultats = (energija * h)
                rezultatsR = round(rezultats,2)
                V = f"Elektroierīces lietošanas izmaksas mēnesī: {rezultatsR}€"
                window["-lietošanas izmaksas-"].update(V, text_color = "#F58311")
            else:
                sg.popup("Prasītajiem lielumiem jābūt lielākiem par 0!")
                window["-izmantošanas laiks-"].update("")
        except (ValueError):
                sg.popup("Prasītie lielumi jānorāda skaitļos!")
                window["-izmantošanas laiks-"].update("")
    if event == "Aprēķināt jaudu":
        try:
            d = float(values["-spriegums-"])
            e = float(values["-stiprums-"])
            if d > 0 and e > 0:
                iericesjauda = (d * e)
                iericesjaudaR = round(iericesjauda,2)
                S = f"Ierīces jauda: {iericesjaudaR} W"
                window["-ierices jauda-"].update(S, text_color = "#F58311")
            else:
                sg.popup("Prasītajiem lielumiem jābūt lielākiem par 0!")
                window["-ierices jauda-"].update("")
        except (ValueError):
                sg.popup("Prasītie lielumi jānorāda skaitļos!")
                window["-ierices jauda-"].update("")

window.close()