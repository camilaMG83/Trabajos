import flet as ft
import flet_audio as fta

songs = [
    {"src": "/Users/camilamontas/Desktop/PYtube/Hey Jessie.mp3", "title": "Hey Jessie", "cover": "https://static.wikia.nocookie.net/disney-mania/images/7/7c/Jessie.jpg/revision/latest?cb=20211018201210"},
    {"src": "/Users/camilamontas/Desktop/PYtube/Better in Stereo.mp3", "title": "Better in Stereo", "cover": "https://m.media-amazon.com/images/I/81z3i2BrIAL._UF1000,1000_QL80_.jpg"},
    {"src": "/Users/camilamontas/Desktop/PYtube/KC Undercover.mp3", "title": "KC Undercover", "cover": "https://m.media-amazon.com/images/M/MV5BMTQ5MzQxMDA1NF5BMl5BanBnXkFtZTgwMzkxNzMwNDE@._V1_FMjpg_UX1000_.jpg"},
    {"src": "/Users/camilamontas/Desktop/PYtube/Princesita Sofía.mp3", "title": "Princesita Sofia", "cover": "https://images.justwatch.com/poster/303001283/s718/sofia-the-first.jpg"},
    {"src": "/Users/camilamontas/Desktop/PYtube/Alas Soy Luna.mp3", "title": "Alas - Soy Luna", "cover": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Disney_Soy_Luna_logo.svg/1200px-Disney_Soy_Luna_logo.svg.png"},
]
# POR SI ACASO LA CANCION DE SOY LUNA DURA PILA PORQUE SU INTRO ES MUY MALA PERO SI DESPUES DE COMO 5 SEGUNDOS SE ESCUCHA :) 
# esta malo el playlist porque no encontre canciones normales pg13, entonces toco disney, pero eso no importa
current_song_index = 0

def main(page: ft.Page):
    global current_song_index
    current_song = songs[current_song_index]

    audio1 = fta.Audio(src=current_song["src"], autoplay=False, volume=1)
    page.overlay.append(audio1)

    song_title = ft.Text(f"Playing... {current_song['title']}")
    album_cover = ft.Image(src=current_song["cover"], width=200, height=200)

    def update_song():
        audio1.src = songs[current_song_index]["src"]
        album_cover.src = songs[current_song_index]["cover"]
        song_title.value = f"Playing... {songs[current_song_index]['title']}"
        page.update()

    def next_song(_):
        global current_song_index
        current_song_index = (current_song_index + 1) % 5
        update_song()
        audio1.play()

    def prev_song(_):
        global current_song_index
        current_song_index = (current_song_index - 1) % 5
        update_song()
        audio1.play()

    def adjust_volume(e):
        audio1.volume = e.control.value / 100
        audio1.update()

    def pick_file(e):
        if e.files:
            file_path = e.files[0].path
            audio1.src = file_path
            song_title.value = "Playing...: YOUR CHOOSEN SONG HURRAYYYY"
            album_cover.src = ""
            page.update()
            audio1.play()

    volume_slider = ft.Slider(min=0, max=100, value=50, label="Volume: {value:.2f}")
    volume_slider.on_change = adjust_volume

    file_picker = ft.FilePicker(on_result=pick_file)
    page.overlay.append(file_picker)

    page.add(
        song_title,
        album_cover,
        ft.ElevatedButton("Play", on_click=lambda _: audio1.play()),
        ft.ElevatedButton("Pause", on_click=lambda _: audio1.pause()),
        ft.Row([
            ft.ElevatedButton("Previous", on_click=prev_song),
            ft.ElevatedButton("Next", on_click=next_song),
        ]),
        volume_slider,
        ft.ElevatedButton("Choose File", on_click=lambda _: file_picker.pick_files(allow_multiple=False))
    )

ft.app(main)
