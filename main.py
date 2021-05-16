from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube 

Folder_Name = ""
#file location
def openLocation():
	global Folder_Name
	Folder_Name = filedialog.askdirectory()
	if(len(Folder_Name)>1):
		locationError.config(text = Folder_Name,fg ="green")
	else:
		locationError.config(text = "Please Choose Folder!!",fg ="red")

#download vedio
def Downloadvedio():
	choice = ytdchoices.get()
	url = ytdEntry.get()

	if (len(url)>1):
		ytdError.config(text = "")
		yt = YouTube(url)

		if(choice == choices[0]):
			select = yt.streams.filter(progressive = True).first()

		elif(choice == choices[1]):
			select = yt.streams.filter(progressive = True,file_extension ='mp4').last()
		elif(choice == choices[2]):
			select = yt.streams.filter(only_audio = True).first()
		else:
			ytdError.config(text = "Paste Link again!!",fg = "red")
	select.download(Folder_Name)
	ytdError.config(text = "Download Completed!")



root = Tk()
root.title("YouDown")
root.geometry("360x400")
root.iconbitmap("Youdownicon.ico")
root.columnconfigure(0,weight = 1)  

#ytd link label
ytdLabel = Label(root,text="Enter the URL of the Vedio",font = ("jost",15))
ytdLabel.grid()

#entry box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width = 50,textvariable=ytdEntryVar)
ytdEntry.grid()

#error
ytdError = Label(root,text = "Error Msg",fg = "red",font = ("jost",10))
ytdError.grid()

#save file

saveLabel = Label(root,text = "Save the Vedio File",font=("jost",15,"bold"))
saveLabel.grid()

#button of save file
saveEntry = Button(root,width = 10,bg = "red",fg = "white",text = "Choose Path",command=openLocation)
saveEntry.grid()


#Error msg loc

locationError = Label(root,text = "Error Msg of Path",fg="red",font=("jost",10))
locationError.grid()

#download Quality
ytdQuality = Label(root,text = "Select Quality",font = ("jost",15))
ytdQuality.grid()

#combox
choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

#download button
downloadbtn = Button(root,text = "Download",width = 10, bg = "red",fg = "white",command = Downloadvedio)
downloadbtn.grid()

#devloper label

devloperlabel = Label(root,text = "by Dhanush-E",font = ("jost",15))
devloperlabel.grid()



root.mainloop() 