import tkinter as tk
from pytube import Playlist

def download_playlist():
    playlist_url = url_entry.get()

    playlist = Playlist(playlist_url)

    for video in playlist.videos:
        try:
            print(f"Téléchargement de la vidéo : {video.title}")
            video.streams.get_audio_only().download(output_path='downloads/')
            print(f"La vidéo {video.title} a été téléchargée avec succès!")
        except Exception as e:
            print(f"Erreur lors du téléchargement de la vidéo {video.title}: {str(e)}")

    print("Tous les téléchargements sont terminés!")

window = tk.Tk()
window.title("Vdownloader")
window.geometry("350x100")

url_label = tk.Label(window, text="URL de la playlist")
url_label.pack()
url_entry = tk.Entry(window)
url_entry.pack()

download_button = tk.Button(window, text="Télecharger", command=download_playlist)
download_button.pack()

window.mainloop()