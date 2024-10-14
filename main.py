import os
import pyautogui
import sys

from tkinter import *
import tkinter as tk
from tkinter import ttk
import pickle

class MainWindow(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
    
    def init_main(self):
        
        notebook = ttk.Notebook()
        notebook.pack(expand=True, fill=BOTH, padx=10)
        frame1 = ttk.Frame(notebook)
        frame2 = ttk.Frame(notebook)
        frame1.pack(fill=BOTH, expand=True)
        frame2.pack(fill=BOTH, expand=True)
        
        notebook.add(frame1, text="Create File")
        notebook.add(frame2, text="Settings")
        
        start = ttk.Button(frame1, command="", width=35)
        start.config(text='Create File', command=lambda: self.printing(login_e.get(),
                                                                            pass_e.get(),
                                                                            channel_e.get(), 
                                                                            channel_e_2.get(), 
                                                                            channel_e_3.get(), 
                                                                            channel_e_4.get(), 
                                                                            channel_e_5.get(),
                                                                            check1.get(),
                                                                            check2.get(),
                                                                            check3.get(),
                                                                            ch_id_e.get(),
                                                                            token_e.get(),
                                                                            ))
        
        inputframe = Frame(frame1)
        login_l = Label(inputframe, text="Login:")
        login_e = Entry(inputframe, width=20, fg="grey", justify='center')
        login_e.insert(END, "! necessarily !")
        login_e.bind("<FocusIn>", lambda args: (login_e.delete('0', 'end'),
                                                login_e.config(fg="black"))  if login_e.get() == "! necessarily !" or login_e.get() == "" else login_e.config(fg="black"))
        login_e.bind("<FocusOut>", lambda args: (login_e.insert(END, "! necessarily !"),
                                                 login_e.config(fg="grey")) if login_e.index("end") == 0 else login_e.insert(END, ""))
            
        inputframe_p = Frame(frame1)
        pass_l = Label(inputframe_p, text="Password:")
        pass_e = Entry(inputframe_p, width=20, fg="grey", justify='center')
        pass_e.insert(END, "not necessary")
        pass_e.bind("<FocusIn>", lambda args: (pass_e.delete('0', 'end'),
                                               pass_e.config(fg="black")) if pass_e.get() == "not necessary" or pass_e.get() == "" else pass_e.config(fg="black"))
        pass_e.bind("<FocusOut>", lambda args: (pass_e.insert(END, "not necessary"),
                                                pass_e.config(fg="grey")) if pass_e.index("end") == 0 else pass_e.insert(END, ""))
        
        farm_l = Label(frame1, text="Twitch accounts (streamers):")
        
        inputframe1 = Frame(frame1)
        channel_e_l = Label(inputframe1, text="1)")
        channel_e = Entry(inputframe1, width=30)
        channel_e.insert(END, "")
        
        inputframe2 = Frame(frame1)
        channel_e_2_l = Label(inputframe2, text="2)")
        channel_e_2 = Entry(inputframe2, width=30)
        channel_e_2.insert(END, "")
        
        inputframe3 = Frame(frame1)
        channel_e_3_l = Label(inputframe3, text="3)")
        channel_e_3 = Entry(inputframe3, width=30)
        channel_e_3.insert(END, "")
        
        inputframe4 = Frame(frame1)
        channel_e_4_l = Label(inputframe4, text="4)")
        channel_e_4 = Entry(inputframe4, width=30)
        channel_e_4.insert(END, "")
        
        inputframe5 = Frame(frame1)
        channel_e_5_l = Label(inputframe5, text="5)")
        channel_e_5 = Entry(inputframe5, width=30)
        channel_e_5.insert(END, "")
        
        inputframe.pack(anchor="n", padx=32)
        login_l.pack(side=LEFT, pady=10, padx=11)
        login_e.pack(side=LEFT, pady=2, padx=0)
        
        inputframe_p.pack(anchor="n")
        pass_l.pack(side=LEFT, pady=3, padx=5)
        pass_e.pack(side=LEFT, pady=2, padx=5)
        
        farm_l.pack(anchor="n", pady=0, padx=10)
        
        inputframe1.pack(anchor="n")
        channel_e_l.pack(side=LEFT, pady=3, padx=0)
        channel_e.pack(side=LEFT, pady=3, padx=10)
        
        inputframe2.pack(anchor="n")
        channel_e_2_l.pack(side=LEFT, pady=3, padx=0)
        channel_e_2.pack(side=LEFT, pady=3, padx=10)
        
        inputframe3.pack(anchor="n")
        channel_e_3_l.pack(side=LEFT, pady=3, padx=0)
        channel_e_3.pack(side=LEFT, pady=3, padx=10)
        
        inputframe4.pack(anchor="n")
        channel_e_4_l.pack(side=LEFT, pady=3, padx=0)
        channel_e_4.pack(side=LEFT, pady=3, padx=10)
        
        channel_e_5_l.pack(side=LEFT, pady=3, padx=0)
        inputframe5.pack(anchor="n")
        channel_e_5.pack(side=LEFT, pady=3, padx=10)
        
        start.pack(anchor="n", pady=10, padx=10)

        value1 = ''
        value2 = ''
        try:
            with open("data.pkl", "rb") as file:
                my_list = pickle.load(file)
            value1 = my_list[0][1]
            value2 = my_list[1][1]
        except:
            pass

        inputframe_ch_id = Frame(frame2)
        ch_id_l = Label(inputframe_ch_id, text="Chat ID: ")
        ch_id_e = Entry(inputframe_ch_id, width=20, fg="grey", justify='center')

        if value1 == '':
            ch_id_e.insert(END, "123456789")
        else:
            ch_id_e.insert(END, value1)

        ch_id_e.bind("<FocusIn>", lambda args: (ch_id_e.delete('0', 'end'), ch_id_e.config(
            fg="black")) if ch_id_e.get() == "123456789" or ch_id_e.get() == "" else ch_id_e.config(fg="black"))
        ch_id_e.bind("<FocusOut>",
                    lambda args: (ch_id_e.insert(END, "123456789"), ch_id_e.config(fg="grey")) if ch_id_e.index(
                        "end") == 0 else ch_id_e.insert(END, ""))

        inputframe_token = Frame(frame2)
        token_l = Label(inputframe_token, text="Token: ")
        token_e = Entry(inputframe_token, width=20, fg="grey", justify='center')

        if value2 == '':
            token_e.insert(END, "123456789:shfuihreuifheuifhiu34578347")
        else:
            token_e.insert(END, value2)

        token_e.bind("<FocusIn>", lambda args: (token_e.delete('0', 'end'), token_e.config(
            fg="black")) if token_e.get() == "123456789:shfuihreuifheuifhiu34578347" or token_e.get() == "" else token_e.config(fg="black"))
        token_e.bind("<FocusOut>",
                    lambda args: (token_e.insert(END, "123456789:shfuihreuifheuifhiu34578347"), token_e.config(fg="grey")) if token_e.index(
                        "end") == 0 else token_e.insert(END, ""))

        save = ttk.Button(frame2, command="", width=35)
        save.config(text='Save Telegram Data', command=lambda: self.saving_tg(
                                                                             ch_id_e.get(),
                                                                             token_e.get(),
                                                                             ))

        Label(frame2, text="(Telegram Settings)").pack(anchor="n", pady=10, padx=5)

        inputframe_ch_id.pack(anchor="n", padx=32)
        ch_id_l.pack(side=LEFT, pady=3, padx=5)
        ch_id_e.pack(side=LEFT, pady=2, padx=0)

        inputframe_token.pack(anchor="n", padx=53)
        token_l.pack(side=LEFT, pady=3, padx=3)
        token_e.pack(side=LEFT, pady=2, padx=5)

        check1 = IntVar(value=1)
        check2 = IntVar(value=0)
        check3 = IntVar(value=0)

        ttk.Checkbutton(frame2, text="Display username", variable=check1, onvalue=1, offvalue=0).pack(anchor=N,pady=5)
        ttk.Checkbutton(frame2, text="Notification sound (Telegram)", variable=check2, onvalue=1, offvalue=0).pack(anchor=N, pady=5)    #pack(anchor=W)==
        Label(frame2, text="(Other Options)").pack(anchor="n", pady=10, padx=5)
        ttk.Checkbutton(frame2, text="Saving Logs", variable=check3, onvalue=1, offvalue=0).pack(anchor=N, pady=0)

        save.pack(anchor="n", pady=10, padx=10)

    def saving_tg(self, id, token):
        script_path = sys.argv[0]
        dir_path = os.path.dirname(script_path)

        my_list = [("id", str(id)), ("token", str(token))]

        with open(dir_path + '/' + 'data' + '.pkl', 'wb') as f:
            pickle.dump(my_list, f)

    def printing(self, login, passw, ch1, ch2, ch3, ch4, ch5, check_1, check_2, check_3, chat_id, token):

        if check_1 == True:
            print("True")
        else:
            print("False")

        if login == "! necessary !":
            return

        if passw == "not necessary":
            passw = ""

        if ch2 != "":
            r1 = ''','''
        else:
            r1 = ''''''
            
        if ch3 != "":
            r2 = ''','''
        else:
            r2 = ''''''
            
        if ch4 != "":
            r3 = ''','''
        else:
            r3 = ''''''
            
        if ch5 != "":
            r4 = ''','''
        else:
            r4 = ''''''
            
        if ch1 != "":
            f1 = '''Streamer("''' + ch1 + '''", settings=StreamerSettings(follow_raid=False , claim_drops=True  , watch_streak=True ))''' + r1
        else:
            f1 = ''''''
        if ch2 != "":
            f2 = '''\n\t\tStreamer("''' + ch2 + '''", settings=StreamerSettings(follow_raid=False , claim_drops=True  , watch_streak=True ))''' + r2
        else:
            f2 = ''''''
        if ch3 != "":
            f3 = '''\n\t\tStreamer("''' + ch3 + '''", settings=StreamerSettings(follow_raid=False , claim_drops=True  , watch_streak=True ))''' + r3
        else:
            f3 = ''''''
        if ch4 != "":
            f4 = '''\n\t\tStreamer("''' + ch4 + '''", settings=StreamerSettings(follow_raid=False , claim_drops=True  , watch_streak=True ))''' + r4
        else:
            f4 = ''''''
        if ch5 != "":
            f5 = '''\n\t\tStreamer("''' + ch5 + '''", settings=StreamerSettings(follow_raid=False , claim_drops=True  , watch_streak=True ))'''
        else:
            f5 = ''''''    
            
            
        text = ('''# -*- coding: utf-8 -*-

import logging
from colorama import Fore
from TwitchChannelPointsMiner import TwitchChannelPointsMiner
from TwitchChannelPointsMiner.logger import LoggerSettings, ColorPalette
from TwitchChannelPointsMiner.classes.Telegram import Telegram
from TwitchChannelPointsMiner.classes.Settings import Priority, Events, FollowersOrder
from TwitchChannelPointsMiner.classes.entities.Streamer import Streamer, StreamerSettings

username="''' + login + '''"
password="''' + passw + '''"

twitch_miner = TwitchChannelPointsMiner(
    username=username,
    password=password,          
    claim_drops_startup=False,                 
    priority=[                                  
        Priority.STREAK,                        
        Priority.DROPS,                         
        Priority.ORDER                          
    ],
    enable_analytics=False,                     
    disable_ssl_cert_verification=False,        
    disable_at_in_nickname=False,              
    logger_settings=LoggerSettings(
        save=''' + str(bool(check_3)) + ''',                              
        console_level=logging.INFO,             
        console_username=''' + str(bool(check_1)) + ''',                 
        auto_clear=True,                       
        time_zone="",                           
        file_level=logging.DEBUG,               
        emoji=True,                            
        less=False,                             
        colored=True,                           
        color_palette=ColorPalette(            
            STREAMER_online="GREEN",            
            streamer_offline="red",             
            BET_wiN=Fore.YELLOW                
        ),
        telegram=Telegram(                                                          
            chat_id=''' + str(chat_id) + ''',    #785808490,                                                      
            token="''' + str(token) + '''",  #"7488035285:AAFpRMgGtmdw_K_3msEtmS2CfIusFMTiXR4",   
            events=[Events.DROP_CLAIM,
                    #Events.STREAMER_ONLINE,
                    #Events.STREAMER_OFFLINE,
                    ],
            disable_notification=''' + str(bool(check_2)) + ''',                                              
        )
    ),
    streamer_settings=StreamerSettings(         
        follow_raid=False,                       
        claim_drops=True,                       
        claim_moments=False,                     
        watch_streak=True,
    )
)

twitch_miner.mine(
    [
        ''' + f1 + ''' ''' + f2 + '''''' + f3 + '''''' + f4 + '''''' + f5 + '''
    ],                                  
    followers=False,                    
    followers_order=FollowersOrder.ASC 
)
''')
        script_path = sys.argv[0]
        dir_path = os.path.dirname(script_path)
        with open(dir_path + '/' + login + '.py', 'w') as f:
            f.write(text)
        
    def run_app():
        root = tk.Tk()
        app = MainWindow(root)
        root.title(" Twitch Account Creator")
        ws = app.winfo_screenwidth()
        hs = app.winfo_screenheight()
        w = 400
        h = 350
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root.mainloop()

app = MainWindow
app.run_app()