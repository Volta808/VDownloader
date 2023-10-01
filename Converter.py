import os
from moviepy.editor import *

def convertirMp3():
    download_folder = 'downloads'

    output_folder = 'mp3_converted'
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(download_folder):
        if filename.endswith('.mp4'):
            input_path = os.path.join(download_folder, filename)

            output_filename = os.path.splitext(filename)[0] + '.mp3'
            output_path = os.path.join(output_folder, output_filename)

            video_clip = VideoFileClip(input_path)
            audio_clip = video_clip.audio

            audio_clip.write_audiofile(output_path)

            video_clip.close()
            audio_clip.close()

    print("Toutes les vidéos MP4 ont été converties en MP3 avec succès.")
def supprimerMp4():
    dossier_downloads = 'downloads'

    if os.path.exists(dossier_downloads):
        for fichier in os.listdir(dossier_downloads):
            chemin_complet_fichier = os.path.join(dossier_downloads, fichier)
            try:
                if os.path.isfile(chemin_complet_fichier):
                    os.remove(chemin_complet_fichier)
                elif os.path.isdir(chemin_complet_fichier):
                    os.rmdir(chemin_complet_fichier)
            except Exception as e:
                print(f"Erreur lors de la suppression du fichier {chemin_complet_fichier}: {str(e)}")
    else:
        print(f"Le dossier '{dossier_downloads}' n'existe pas.")
