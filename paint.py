import sys, pygame, math, random
from pygame.locals import *

class draw_item:
    
    def __init__(self):
        self.surface = None
        self.left = 0
        self.top = 0

    def add(self,surface,left,top):
        self.surface = surface
        self.left = left
        self.top = top



class paint:

    def __init__(self):
        pygame.init()
        
        self.WHITE = 0,0,0
        self.BLACK = 255,255,255
        self.GREY1 = 100,100,100
        self.RED = 255,0,0
        self.GREEN = 0,255,0
        self.BLUE = 0,0,255
        self.color = self.WHITE
        self.QUIT = False
        self.mousebutton = None
        self.mousedown = False
        self.toolset = ["Line","Circle","Rect","Freehand","Eraser","image"]
        self.mouse_buttons = ["Left Button"]
        self.draw_list = []
        self.mouseX = self.mouseY = 0
        self.draw_tool = "Freehand"
        self.drawstartX = -1
        self.drawendX = -1
        self.drawstartY = -1
        self.drawendY = -1
        self.bgimg="None"
        self.background="None"
        self.draw_toggle = False
        
    
        #initialize system
        self.initialize()

        
    def initialize(self):
        
        #the pygame screen
        self.screen_width = 1200
        self.screen_height = 700
        self.screen_size = (self.screen_width, self.screen_height)    
        self.screen = pygame.display.set_mode(self.screen_size)

        #generic drawing surface
        self.canvas = pygame.Surface((self.screen_width, self.screen_height))
        self.canvas.fill((self.BLACK))
        pygame.display.set_caption("Paint- Press ESC to quit")

        
        self.work_canvas = pygame.Surface((self.screen_width, self.screen_height))
        self.work_canvas.set_colorkey(self.BLACK)

        
        self.paint_canvas = pygame.Surface((self.screen_width, self.screen_height))
        self.paint_canvas.fill((self.BLACK))

    def radius(self,rectangle):
        x1,y1,x2,y2 = rectangle
        x = (x2-x1)
        y = (y2-y1)
        if x >= y:
            rad = x
        else:
            rad = y
        if rad < 3:
            rad = 3
        return rad/2

    def center(self,rectangle):
        x1,y1,x2,y2 = rectangle
        x = abs(x1-x2)
        y = abs(y1-y2)
        x1 += x/2
        y1 += y/2
        return (x1,y1)

    
        

    def mouse_handler(self,events): 

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mousedown = True
                self.mousebutton = event.button  
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mousedown = False
                self.mousebutton = event.button
            self.mouseX, self.mouseY = pygame.mouse.get_pos()

        
        if self.draw_tool == "Line":
            self.draw_line_template()
        if self.draw_tool == "Circle":
            self.draw_circle_template()
        if self.draw_tool == "Rect":
            self.draw_rect_template()
        if self.draw_tool == "Freehand":
            self.draw_freehand_template()
        if self.draw_tool == "Eraser":
            self.draw_eraser_template()
        
        if self.draw_tool == "image":
            self.draw_image_template()
        

        
        self.show_mousestate()


    def draw_image_template(self):
        path=raw_input()
        print path
        
        
        bgimg = pygame.image.load(path).convert()
        #self.background=self.canvas.blit(self.bgimg, (0,0))
        #self.background=self.work_canvas.blit(self.bgimg, (0,0))
        self.paint_canvas.blit(bgimg, (0,0))
        print "debahish"
        
        
        


    
    def draw_eraser_template(self):
        
        if self.draw_toggle == False and self.mousedown and self.mousebutton == 1:
            self.drawstartX = self.mouseX
            self.drawendX = self.mouseX
            self.drawstartY = self.mouseY
            self.drawendY = self.mouseY
            self.draw_toggle = True

        
        elif self.draw_toggle == True and self.mousedown and self.mousebutton == 1:
            self.drawstartX = self.drawendX
            self.drawstartY = self.drawendY
            self.drawendX = self.mouseX
            self.drawendY = self.mouseY
            
            self.work_canvas.fill(self.BLACK)
            
            pygame.draw.line(self.paint_canvas,
                             (self.BLACK),
                             (self.drawstartX,self.drawstartY),
                             (self.drawendX,self.drawendY),
                             18)
            
            self.draw_tool_template()

        
        elif self.draw_toggle == True and not self.mousedown and self.mousebutton == 1:
            self.draw_toggle = False
            
            pygame.draw.line(self.paint_canvas,
                             (self.BLACK),
                             (self.drawstartX,self.drawstartY),
                             (self.drawendX,self.drawendY),
                             18)




    def draw_freehand_template(self):
        
        if self.draw_toggle == False and self.mousedown and self.mousebutton == 1:
            self.drawstartX = self.mouseX
            self.drawendX = self.mouseX
            self.drawstartY = self.mouseY
            self.drawendY = self.mouseY
            self.draw_toggle = True

        
        elif self.draw_toggle == True and self.mousedown and self.mousebutton == 1:
            self.drawstartX = self.drawendX
            self.drawstartY = self.drawendY
            self.drawendX = self.mouseX
            self.drawendY = self.mouseY
        
            self.work_canvas.fill(self.BLACK)
            
            pygame.draw.line(self.paint_canvas,
                             (self.color),
                             (self.drawstartX,self.drawstartY),
                             (self.drawendX,self.drawendY),
                             2)
            
            self.draw_tool_template()

        
        elif self.draw_toggle == True and not self.mousedown and self.mousebutton == 1:
            self.draw_toggle = False
            
            pygame.draw.line(self.paint_canvas,
                             (self.color),
                             (self.drawstartX,self.drawstartY),
                             (self.drawendX,self.drawendY),
                             2)


        

    def draw_rect_template(self):
        
        if self.draw_toggle == False and self.mousedown and self.mousebutton == 1:
            self.drawstartX = self.mouseX
            self.drawendX = self.mouseX
            self.drawstartY = self.mouseY
            self.drawendY = self.mouseY
            self.draw_toggle = True

        
        elif self.draw_toggle == True and self.mousedown and self.mousebutton == 1:
            self.drawendX = self.mouseX
            self.drawendY = self.mouseY
            
            self.work_canvas.fill(self.BLACK)
            
            pygame.draw.line(self.work_canvas,
                             (self.GREY1),
                             (0,self.drawstartY),
                             (2000,self.drawstartY),
                             1)
            pygame.draw.line(self.work_canvas,
                             (self.GREY1),
                             (self.drawstartX,0),
                             (self.drawstartX,2000),
                             1)

            
            try:
               pygame.draw.rect(self.work_canvas,
                             (self.GREY1),
                             (self.drawstartX,self.drawstartY,abs(self.drawstartX- self.drawendX), abs( self.drawstartY - self.drawendY)),
                             1)
            except: 
                pass
            
            self.draw_tool_template()

        
        elif self.draw_toggle == True and not self.mousedown and self.mousebutton == 1:
            self.draw_toggle = False
            
            try:
               pygame.draw.rect(self.paint_canvas,
                             (self.color),
                             Rect(self.drawstartX,self.drawstartY,abs(self.drawstartX- self.drawendX),abs(self.drawstartY- self.drawendY)),
                             2)
            except:  
                pass

        


    def draw_circle_template(self):
        
        if self.draw_toggle == False and self.mousedown and self.mousebutton == 1:
            self.drawstartX = self.mouseX
            self.drawendX = self.mouseX
            self.drawstartY = self.mouseY
            self.drawendY = self.mouseY
            self.draw_toggle = True

        
        elif self.draw_toggle == True and self.mousedown and self.mousebutton == 1:
            self.drawendX = self.mouseX
            self.drawendY = self.mouseY
            
            self.work_canvas.fill(self.BLACK)
            #draw guide lines
            pygame.draw.line(self.work_canvas,
                             (self.GREY1),
                             (0,self.drawstartY),
                             (2000,self.drawstartY),
                             1)
            pygame.draw.line(self.work_canvas,
                             (self.GREY1),
                             (self.drawstartX,0),
                             (self.drawstartX,2000),
                             1)

            
            try:
               pygame.draw.circle(self.work_canvas,
                             (self.GREY1),
                             self.center((self.drawstartX,self.drawstartY,self.drawendX,self.drawendY)),
                             self.radius((self.drawstartX,self.drawstartY,self.drawendX,self.drawendY)),
                             1)
            except:  
                pass
            
            self.draw_tool_template()

        
        elif self.draw_toggle == True and not self.mousedown and self.mousebutton == 1:
            self.draw_toggle = False
            
            try:
               pygame.draw.circle(self.paint_canvas,
                             (self.color),
                             self.center((self.drawstartX,self.drawstartY,self.drawendX,self.drawendY)),
                             self.radius((self.drawstartX,self.drawstartY,self.drawendX,self.drawendY)),
                             2)
            except:  
                pass



            
    def draw_line_template(self):

        
        if self.draw_toggle == False and self.mousedown and self.mousebutton == 1:
            self.drawstartX = self.mouseX
            self.drawendX = self.mouseX
            self.drawstartY = self.mouseY
            self.drawendY = self.mouseY
            self.draw_toggle = True

        
        elif self.draw_toggle == True and self.mousedown and self.mousebutton == 1:
            self.drawendX = self.mouseX
            self.drawendY = self.mouseY
            
            self.work_canvas.fill(self.BLACK)
            
            pygame.draw.line(self.work_canvas,
                             (self.GREY1),
                             (self.drawstartX,self.drawstartY),
                             (self.drawendX,self.drawendY),
                             1)
            
            self.draw_tool_template()

        
        elif self.draw_toggle == True and not self.mousedown and self.mousebutton == 1:
            self.draw_toggle = False
            
            pygame.draw.line(self.paint_canvas,
                             (self.color),
                             (self.drawstartX,self.drawstartY),
                             (self.drawendX,self.drawendY),
                             2)

    def show_mousestate(self):
        """Show the mouse position and button press on the screen"""
        if self.mousebutton and self.mousedown:
            info = "Space->clear, L->lines, C->Circles, E->Eraser, R->Rectangle, F->Freehand || Colors 1->Red, 2->Green, 3->Blue, 4->Black, 5->Random"
            info += " ...Mouse: "+str(self.mouse_buttons[self.mousebutton-1])
        else:
            info = "Space->clear, L->lines, C->Circles, E->Eraser, R->Rectangle, F->Freehand || Colors 1->Red, 2->Green, 3->Blue, 4->Black, 5->Random "
        info += " ...Mouse X= "+str(self.mouseX)+" Y: "+str(self.mouseY)
        info += " LeftButtonDown: " + str(self.draw_toggle)

    
        font = pygame.font.Font(None, 20)        
        textimg = font.render(info, 1, self.WHITE)

        
        item = draw_item()
        item.add(textimg,10,10)
        self.draw_list.append(item)
        
    def draw_tool_template(self):
       
        item = draw_item()
        item.add(self.work_canvas,0,0)
        self.draw_list.append(item)

    def canvas_draw(self):
        
        self.canvas.fill(self.BLACK)        
        self.canvas.blit(self.paint_canvas,(0,0))        
        for i in self.draw_list:
            self.canvas.blit(i.surface,(i.left,i.top))
        

    def draw(self):
        
        self.canvas_draw()
        self.screen.blit(self.canvas, (0, 0))

    def clear(self):
        
        self.draw_list = []

    def run(self):
        
        while 1:

            #we clear and prepare the draw_list for the canvas
            self.clear()
            events = pygame.event.get()
            for e in events:
            
                if e.type == pygame.QUIT :
                    self.QUIT = True
                if e.type == KEYDOWN:                    
                    if e.key == K_ESCAPE:
                        self.QUIT = True                    
                    if e.key == K_l:
                        self.draw_tool = "Line"         
                    if e.key == K_c:
                        self.draw_tool = "Circle"
                    if e.key == K_f:
                        self.draw_tool="Freehand"
                    if e.key == K_r:
                        self.draw_tool="Rect"
                    if e.key == K_e:
                        self.draw_tool="Eraser"
                    if e.key == K_5:
                        self.color=(random.randrange(256), random.randrange(256), random.randrange(256))
                    if e.key == K_4:
                        self.color=self.WHITE
                    if e.key == K_3:
                        self.color=self.BLUE
                    if e.key == K_2:
                        self.color=self.GREEN
                    if e.key == K_1:
                        self.color=self.RED
                    if e.key == K_i:
                        self.draw_tool="image"
                    if e.key == K_SPACE:
                        self.canvas.fill((255,255,255))
                        self.work_canvas.fill((255,255,255))
                        self.paint_canvas.fill((255,255,255))
                        
                        
                                    
            if self.QUIT:
                pygame.quit()
                sys.exit(0)

            #call the mouse handler with current events
            self.mouse_handler(events)
            self.draw()
            pygame.display.flip()

            

if __name__ == "__main__":
    mypaint = paint()
    mypaint.run()
    

    
