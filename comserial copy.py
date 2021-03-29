import tkinter as tk
from tkinter import font
 
import sys
 
 
class myApp(object):
     
    def __init__(self, **kw):
        #insira toda a inicialização aqui
                            
        self.root = tk.Tk()
        self.root.title("Bem vindo a Interface Tk")
        self.root.geometry('800x600')
        self.create_menu_bar()
        self.create_canvas_area()
        self.create_status_bar()
         
         
         
    def create_status_bar(self):
        self.status = tk.Label(self.root,
                               text="Interface tk",
                               bd=1, relief=tk.SUNKEN)
        self.status.pack(side= tk.BOTTOM, fill = tk.X)
 
 
 
    def clear_status_bar(self):
        self.status.config(text="")
        self.status.update_idletasks() 
         
    def set_status_bar(self, texto):
        self.status.config(text=texto)
        self.status.update_idletasks()       
 
    def create_menu_bar(self):           
        menubar = tk.Menu(self.root)
         
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.finaliza_software)
        
        
        menubar.add_cascade(label="File", menu=filemenu)
         
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.mnu_about)
        menubar.add_cascade(label="Help", menu=helpmenu)
         
        self.root.config(menu=menubar)
 
    def create_canvas_area(self):
        lbl1 = tk.Label(self.root, text="Interface test",fg= "blue", font= ("Arial" ,"28", "bold"))
 
         
        text1 = tk.Text(self.root, height=20, width=60)
        text1.insert(tk.END, "\t\tPronto para entrar em operação!\n")
        text1.insert(tk.END, "\tNão esqueça configuração da porta serial")
 
         
         
        frame1 = tk.Frame(self.root)
         
        btnVersao= tk.Button(frame1, text = "Versão?")
        btnTemp= tk.Button(frame1, text = "Temperatura?")
        btnIntervalo= tk.Button(frame1, text ="Intervalo:")
        entry1= tk.Entry(frame1,width=5 )
        entry1.insert( 0,"10")
         
        btnVersao.pack(side = tk.LEFT, padx= 10, pady= 15)
        btnTemp.pack(side = tk.LEFT,  padx= 10, pady= 15)
        btnIntervalo.pack(side = tk.LEFT, padx= 10, pady= 15)
        entry1.pack(side = tk.LEFT,pady= 15)
                 
        lbl1.pack()
        text1.pack()
        frame1.pack()
         
         
         
         
         
    def finaliza_software(self):
        self.root.quit()       
     
         
    def mnu_about(self):
        pass
  
     
    def execute(self):
        self.root.mainloop()
 
 
 
 
def main(args):
    app_proc = myApp()
    app_proc.execute()
    return 0
 
 
if __name__ == '__main__':
    sys.exit(main(sys.argv))
