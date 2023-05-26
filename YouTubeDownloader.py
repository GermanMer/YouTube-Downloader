#Para instalar pytube, ejecute el siguiente comando en su terminal: pip install pytube
#To install pytube, run the following command in your terminal: pip install pytube

idioma = input("Para idioma español, escriba español. For english, write english: ")

from pytube import YouTube

if idioma.lower() == "español":
    msg_ingreso_link = "Introduce el enlace del video que deseas descargar: "
    msg_link_incorrecto = "El enlace ingresado es inválido, por favor ingrese un enlace válido."
    msg_descargando = "Descargando video en la mejor calidad, esto puede demorar algunos minutos"
    msg_completado = "¡Descarga completada!"
elif idioma.lower() == "english":
    msg_ingreso_link = "Enter the link of the video you want to download: "
    msg_link_incorrecto = "The entered link is invalid, please enter a valid link"
    msg_descargando = "Downloading video in the best quality, this may take a few minutes"
    msg_completado = "Download completed!"
else:
    print("Opción de idioma no válida. Se establecerá el idioma en español por defecto.\nInvalid language option. The language will be set to Spanish by default.")
    msg_ingreso_link = "Introduce el enlace del video que deseas descargar: "
    msg_link_incorrecto = "El enlace ingresado es inválido, por favor ingrese un enlace válido."
    msg_descargando = "Descargando video en la mejor calidad, esto puede demorar algunos minutos"
    msg_completado = "¡Descarga completada!"

while True:
    link = input(msg_ingreso_link)
    try:
        yt = YouTube(link)
        break
    except:
        print(msg_link_incorrecto)

print(msg_descargando)
yt.streams.get_highest_resolution().download()

print(msg_completado)
