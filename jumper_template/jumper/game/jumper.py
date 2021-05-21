
class Jumper:
    def __init__(self):
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
        print(self.parachute[0])


