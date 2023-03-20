class ConsoleGameGui:
  def __init__(self, w, h, logic) -> None:
     self.main_w = w
     self.main_h = h
     self.logic = logic
    
  def run(self):
    running = True
    while running:
       self.processEvent(GameEvent(GameEvent.Event_Tick, None))

       self.draw()

       print('------------------')
       print('0. exit')
       print('1. hit target')
       cmd = int(input())

       event = GameEvent(GameEvent.Event_None, None)

       if cmd == 0:
           running = False
           continue
    
       if cmd == 1:
           x = int(input('input X: '))
           y = int(input('input Y: '))
           event = GameEvent(GameEvent.Event_Hit, Pos(x, y))

 
       self.processEvent(event)

  def processEvent(self, event):
       self.logic.processEvent(event)

  def draw(self):
    score = self.logic.getScore()
    print('------------------')
    print(f'Your score: {score}')

    print('Aims:')
    marks = self.logic.getBoard()
    for index, mark in enumerate(marks):
       print(f'aim{index}[x = {mark.getPos().x},y={mark.getPos().y}, w = {mark.getWidth()}, h = {mark.getHeight()}]: {mark.getCost()}')

if __name__ == "__main__":
 width   = 800
 height  = 600
 gui = ConsoleGameGui(width,height, GameLogic(width, height))
 gui.run()