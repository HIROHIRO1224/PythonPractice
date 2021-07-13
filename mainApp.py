import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
 
class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        # 動画元を開く (ウェブカメラで開くか試みる)
        self.vid = MyVideoCapture(self.video_source)

        # 動画のデータのサイズに合うようにCanvasオブジェクトを生成
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        # 一度呼ばれた後、delayに入っている時間(ms)の間隔でupdateメソッドを自動的にもう一度呼び出す
        self.delay = 15
        self.update()

        self.window.mainloop()
 
    def update(self):
        # 動画元の画像を取得する
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

        self.window.after(self.delay, self.update)

class myTimer:
    def FirstTimer():
        global T_First_Min
        T_First_Min=3

        while T_First_Min>0:
            T_First_Min-=1
            time.sleep(1)

        

class MyVideoCapture:
    def __init__(self, video_source=0):
        # 動画元を開く
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # 動画元の幅と高さを取得する
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.cascade_path = "./haarcascade_frontalface_alt2.xml"
        self.cascade = cv2.CascadeClassifier(self.cascade_path)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # 顔検出
                facerect = self.cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))
     
                # 矩形線の色
                rectangle_color = (0, 255, 0) #緑色
 
                # 顔を検出した場合
                if len(facerect) > 0:
                    for rect in facerect:
                        cv2.rectangle(frame, tuple(rect[0:2]),tuple(rect[0:2] + rect[2:4]), rectangle_color, thickness=2)

                # ブール値の成功フラグとBGRに変換した映像データを返す
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)


    # ウィンドウを閉じたときメモリを開放する
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


if __name__ == "__main__":
    # 高dpi対応
    import ctypes
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
    except:
        pass
    # Create a window and pass it to the Application object
    App(tkinter.Tk(), "Tkinter and OpenCV")