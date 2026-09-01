import os

import pygame

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"


def play_music(folder, song_name):
    file_path = os.path.join(folder, song_name)
    if not os.path.exists(file_path):
        print("File was not found")
        return

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    print(f"\nNow playing: {song_name}")
    print("Commands: [P]ause, [R]esume, [S]top")

    while True:
        command = input("> ").upper()
        if command == "P":
            pygame.mixer.music.pause()
            print("Paused")
        elif command == "R":
            pygame.mixer.music.unpause()
            print("Resumed")
        elif command == "S":
            pygame.mixer.music.stop()
            print("Stopped")
            return
        else:
            print("Invalid command")


def main():
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print("Failed to initialize Audio player!", e)
        return

    folder = "music"
    if not os.path.isdir(folder):
        print(f"Folder '{folder}' does not exist")
        return

    mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]
    if not mp3_files:
        print("No music, add files to the library")
    while True:
        print("MP3 PLAYER")
        print("My song list:")
        for index, song in enumerate(mp3_files, start=1):
            print(f"{index}. {song}")
        choice_input = input("\nEnter the song # to play (or 'Q' to quit): ")
        if choice_input.upper() == "Q":
            print("Quitting...")
            break
        if not choice_input.isdigit():
            print("Please enter a valid song number")
            continue

        choice = int(choice_input) - 1
        if 0 <= choice < len(mp3_files):
            play_music(folder, mp3_files[choice])
        else:
            print("Invalid choice, selected song doesn't exist")


if __name__ == "__main__":
    main()
