import threading
from tkinter import Tk, StringVar,N,W,E,S
from tkinter import ttk 
import subprocess 

# gui
root = Tk()
root.title("run command by button click")
# gui vars
stdoutput = StringVar() 
# gui widget
cmd = ttk.Label(root,text="deno run app.ts")
cmd.pack()
#
btn_run =ttk.Button(root,text="run")
btn_run.pack()
#
btn_stop = ttk.Button(root,text="stop")
btn_stop.pack()
#
btn_close = ttk.Button(root,text="close")
btn_close.pack()
#
btn_clear = ttk.Button(root,text="clear")
btn_clear.pack()
#
terminal = ttk.Label(root,text="")
terminal.pack()
# functions and the comand list
command = ["deno", "run", "--allow-all", "--unstable", "app.ts"] # you can change this comand
def run_command():
    text = ""
    process = subprocess.Popen(command, stdout=subprocess.PIPE,shell=False)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            t = ""
            t = output.decode('UTF-8')
            #t = t.strip()
            text = stdoutput.get()
            text = text + t
            stdoutput.set(text)
            terminal.config(text=stdoutput.get())
def fn():
    threading.Thread(target=run_command,args=()).start()  
def clear_output():
    stdoutput.set("")
    terminal.config(text="")
def close_window():
    root.destroy()
# config
btn_run.config(command=fn)
btn_close.config(command=close_window)
btn_clear.config(command=clear_output)
#
root.mainloop()