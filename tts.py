#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pyttsx3')


# In[2]:


import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from gtts import gTTS
from playsound import playsound


# In[3]:


get_ipython().system('pip install gtts')


# In[4]:


import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from gtts import gTTS
from playsound import playsound


# In[5]:


get_ipython().system('pip install playsound')


# In[6]:


import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from gtts import gTTS
from playsound import playsound


# In[7]:


root = Tk()
root.title("Text to speech converter")
root.geometry("1000x580+200+80")
root.resizable(False,False)
root.configure(bg="#14A7DD")
#root.mainloop()


# In[8]:


tts = pyttsx3.init()
def speaknow():
    text = text_box.get(1.0,END)
    gender = gender_box.get()
    speed = speed_box.get()
    voices = tts.getProperty('voices')
    
    def setvoice():
        if (gender == 'Male'):
            tts.setProperty('voice',voices[0].id)
            tts.say(text)
            tts.runAndWait()
        else:
            tts.setProperty('voice',voices[1].id)
            tts.say(text)
            tts.runAndWait()
            
    if(text):
        if(speed == 'Fast'):
            tts.setProperty('rate',250)
            setvoice()
        elif(speed == 'Medium'):
            tts.setProperty('rate',150)
            setvoice()
        else:
            tts.setProperty('rate',60)
            setvoice()


# In[9]:


upper_frame = Frame(root, bg="#ffffff" , width = 1200, height = 130)
upper_frame.place(x=0, y=0)

picture = PhotoImage(file = "C:/Users/shubhe/Downloads/txt.png")
Label(upper_frame, image=picture, bg="#ffffff").place(x=150, y=30)

#root.mainloop()


# In[10]:


Label(upper_frame,text="Text to Speech Converter",font="TimesNewroman 40 bold", bg ="#ffffff", fg = 'black').place(x=250, y=35)
#root.mainloop()


# In[11]:


logo_image = PhotoImage(file= "C:/Users/shubhe/Downloads/txt.png")
root.iconphoto(False, logo_image)
#root.mainloop()


# In[12]:


text_box = Text(root, font="calibri 20", bg="white", relief = GROOVE, wrap= WORD, bd=0)
text_box.place(x=30, y=150,width=940,height=180)
#root.mainloop()


# In[13]:


gender_box = Combobox(root,values=['Male','Female'], font = "Robote 12", state='r', width = 12)
gender_box.place(x=340 , y=400)
gender_box.set('Male')
#root.mainloop()


# In[14]:


speed_box = Combobox(root,values=['Fast','Medium','Slow'], font = "Robote 12", state='r', width = 12)
speed_box.place(x=540 , y=400)
speed_box.set('Medium')
#root.mainloop()


# In[15]:


play_button= PhotoImage(file= "C:/Users/shubhe/Downloads/play.png")
play_btn = Button(root, text= "Play",compound= LEFT, image=play_button,bg='white',width=130, font="arial 14 bold",borderwidth = '0.1c',command =speaknow)
play_btn.place(x=435,y=450)
root.mainloop()


# In[ ]:




