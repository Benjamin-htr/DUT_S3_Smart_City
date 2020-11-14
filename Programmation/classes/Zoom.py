from tkinter import *

class zoom(Frame) :
    def __init__(self, gestionSimulation, master):

        self.gestSim = gestionSimulation
        self.master = master
        self.tailleXdeb=self.gestSim.tailleX
        self.nbZoom=0

        self.canvas = self.gestSim.CanvasCarte
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))
        
        # Mouse bindings to the canvas
        self.canvas.bind("<ButtonPress-1>", self.move_start)
        self.canvas.bind("<B1-Motion>", self.move_move)
        self.canvas.bind("<MouseWheel>", self.zoom)
        self.canvas.bind("<Button-2>", self.resetZoom)

    # move
    def move_start(self, event):
        self.canvas.scan_mark(event.x, event.y)
        self.canvas.configure(scrollregion = (self.canvas.bbox("all")[0]+4,self.canvas.bbox("all")[1]+4,self.canvas.bbox("all")[2],self.canvas.bbox("all")[3]))
        
    def move_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)
        self.canvas.configure(scrollregion = (self.canvas.bbox("all")[0]+4,self.canvas.bbox("all")[1]+4,self.canvas.bbox("all")[2],self.canvas.bbox("all")[3]))
        

    def resetZoom(self, event):
        scale=self.tailleXdeb/self.gestSim.tailleX
        self.canvas.scale("all", self.gestSim.origX, self.gestSim.origY, scale, scale)
        self.canvas.scan_mark(2, 2)
        self.canvas.configure(scrollregion = (self.canvas.bbox("all")[0]+4,self.canvas.bbox("all")[1]+4,self.canvas.bbox("all")[2],self.canvas.bbox("all")[3]))
        self.gestSim.scale=1
        self.gestSim.tailleX=(650/self.gestSim.controlSimulation.simulation.carte.nx)*self.gestSim.scale

        return scale


    def resetZoom2(self):
        scale=self.tailleXdeb/self.gestSim.tailleX
        self.canvas.scale("all", self.gestSim.origX, self.gestSim.origY, scale, scale)
        self.canvas.scan_mark(2, 2)
        self.canvas.configure(scrollregion = (self.canvas.bbox("all")[0]+4,self.canvas.bbox("all")[1]+4,self.canvas.bbox("all")[2],self.canvas.bbox("all")[3]))
        self.gestSim.scale=1
        self.gestSim.tailleX=(650/self.gestSim.controlSimulation.simulation.carte.nx)*self.gestSim.scale
        return scale


    # zoom
    def zoom(self, event):
        true_x = self.canvas.canvasx(event.x)
        true_y = self.canvas.canvasy(event.y)
        #print('x :', event.x, 'y :', event.y, 'true_x :', true_x, 'true_y :', true_y)
        canvas=self.canvas
        scale=self.tailleXdeb/self.gestSim.tailleX
        if (event.delta > 0):
            self.nbZoom+=1
            self.canvas.scale("all", true_x, true_y, 1.1, 1.1)
            self.gestSim.scale *= 1.1
        elif (event.delta < 0 and self.nbZoom > 0):
            self.nbZoom-=1
            self.canvas.scale("all", true_x, true_y, scale, scale)
            self.gestSim.scale *= scale

        self.gestSim.tailleX=(650/self.gestSim.controlSimulation.simulation.carte.nx)*self.gestSim.scale
        self.canvas.configure(scrollregion = (self.canvas.bbox("all")[0]+4,self.canvas.bbox("all")[1]+4,self.canvas.bbox("all")[2],self.canvas.bbox("all")[3]))

        



