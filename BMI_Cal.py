from tkinter import *
from tkinter.ttk import *           # ComboBox
from tkinter import messagebox

BMI_window = Tk()
BMI_window.title('BMI Calculator')
BMI_window.geometry('250x80')
BMI_window.resizable(0, 0)

# 輸出格 BMI值 Label

# Height
lb_h8 = Label(BMI_window,text="請輸入您的身高(m):")
lb_h8.place(x=0,y=0)

text_h8 = Entry(BMI_window,width=5,justify='right')
text_h8.insert(0,'0')
text_h8.place(x=120,y=0)

# Weight
lb_w8 = Label(BMI_window,text="請輸入您的體重(kg):")
lb_w8.place(x=0,y=25)

text_w8 = Entry(BMI_window,width=5,justify='right')
text_w8.place(x=120,y=25)
text_w8.insert(0,'0')

# Ans
lb_ans = Label(BMI_window,text = 'BMI值為:')
lb_ans.place(x=0,y=50)

# 計算
def btn_cal_clicked():
    h8 =  float(text_h8.get())
    w8 = float(text_w8.get())
    ans = ''

    if w8==0 :
        messagebox.showerror('錯誤訊息', '體重應該大於0')
    else:
        try:
            ans = str(w8/(h8**2))
            lb_ans.configure(text='BMI值為:' + ans)
        except ZeroDivisionError:
            messagebox.showerror('錯誤訊息', '身高應該大於0')

btn_calcuate = Button(BMI_window,text='計算',command=btn_cal_clicked,width=5)
btn_calcuate.place(x=200,y=10)

BMI_window.mainloop()