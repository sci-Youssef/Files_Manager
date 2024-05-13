from customtkinter import *
from os import mkdir, listdir, chdir
from shutil import move

app = CTk()
app.geometry("400x300")
app.title("Files Manager")

message = CTkLabel(app, text="""Choose The Folder That Contain:
PDF, Powerpoints, Photos, Videos""")
message.pack()


def clicked():
    folder_path = filedialog.askdirectory()
    chdir(folder_path)

    PDFs = [f for f in listdir() if '.pdf' in f.lower()]
    vids = [v for v in listdir() if '.mp4' in v.lower()]
    ppts = [p for p in listdir() if '.ppt' in p.lower()]
    photos = [pic for pic in listdir() if
              '.png' in pic.lower() or '.jpg' in pic.lower() or '.jpeg' in pic.lower() or '.gif' in pic.lower()]
    folders = listdir()
    if len(PDFs) > 0 and "PDFs" not in folders:
        mkdir('PDFs')
    for PDF in PDFs:
        if PDF in folders:
            new_path = 'PDFs/' + PDF
            move(PDF, new_path)

    if len(vids) > 0 and "Videos" not in folders:
        mkdir('Videos')
    for video in vids:
        if video in folders:
            new_vid_path = 'Videos/' + video
            move(video, new_vid_path)

    if len(ppts) > 0 and "Powerpoints" not in folders:
        mkdir("Powerpoints")
    for ppt in ppts:
        if ppt in folders:
            new_ppt_path = 'Powerpoints/' + ppt
            move(ppt, new_ppt_path)

    if len(photos) > 0 and "Photos" not in folders:
        mkdir("Photos")
    for photo in photos:
        if photo in folders:
            new_photo_path = 'Photos/' + photo
            move(photo, new_photo_path)
    done = CTkLabel(app, text="DONE!", text_color="#37FBB3")
    done.pack()


btn = CTkButton(master=app, text="Open", hover_color="green", command=clicked)
btn.pack()

app.mainloop()
