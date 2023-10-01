from pytube import Playlist

import Converter

playlist_url = str(input("Entrez l'URL de la playlist : "))

playlist = Playlist(playlist_url)

for video in playlist.videos:
    print(f"Téléchargement de la vidéo : {video.title}")
    video.streams.get_lowest_resolution().download(output_path='downloads/')
    print(f"La vidéo {video.title} a été téléchargée avec succès!")

print("Tous les téléchargements sont terminés.")

#Demande pour convertir les fichiers mp4 en mp3 après le téléchargement
convertir = str(input("Voulez-vous convertir les mp4 en mp3 ? (o/n)"))
if convertir=="o":
    Converter.convertirMp3()

#Demande pour supprimer les fichiers mp4 après la convertion
    supprimer = str(input("Voulez-vous supprmier les fichiers mp4 ? (o/n)"))
    if supprimer=="o":
        Converter.supprimerMp4()




