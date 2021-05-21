
class Jumper:
    def __init__(self):
        self.life = 0
        self.parachute = ["""
         ___  
        /___\ 
        \   / 
         \ /  
          0   
         /|\  
         / \  
                
       ^^^^^^^
        """, """
           
        /___\ 
        \   / 
         \ /  
          0   
         /|\  
         / \  
                
        ^^^^^^^
        ""","""
           
        /__ 
        \   / 
         \ /  
          0   
         /|\  
         / \  
                
        ^^^^^^^
        ""","""
           
         
        \   / 
         \ /  
          0   
         /|\  
         / \  
                
        ^^^^^^^
        """, """
          
          x   
         /|\  
         / \  
                
        ^^^^^^^
        """
        ]
    
    def display(self):
        print(self.parachute[self.life])

    def life (self, success):
      if success == False:
        self.life += 1




