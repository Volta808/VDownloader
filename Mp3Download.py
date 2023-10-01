from pytube import Playlist

playlist_url = str(input("Entrez l'URL de la playlist : "))

playlist = Playlist(playlist_url)

for video in playlist.videos:
    print(f"Téléchargement de la vidéo : {video.title}")
    video.streams.get_audio_only().download(output_path='downloads/')
    print(f"La vidéo {video.title} a été téléchargée avec succès!")

print("Tous les téléchargements sont terminés.")

