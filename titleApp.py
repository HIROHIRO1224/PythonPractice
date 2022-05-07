import tkinter
from tkinter import ttk

class titleApp:
    def __init__(self,window,window_name):
        self.window=window
        self.window.title=window_name

        Title_label=ttk.Label(self.window,text='これはタイトル画面です')
        Button1=ttk.Button(self.window,text='Press Start',width=25,command=self.AppStart)
        Title_label.pack()
        Button1.pack()

        self.window.mainloop()

    def AppStart(self):
        import subprocess
        command=["python","./mainApp.py"]
        # command=["start","mainApp.exe"] <---後々exeパッケージした後用のコマンド
        subprocess.Popen(command ,shell=True)
        self.window.destroy()

if __name__ == "__main__":
    import ctypes
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
    except:
        pass
    titleApp(tkinter.Tk(),'タイトル')