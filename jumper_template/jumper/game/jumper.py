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
        
    
     \   / 
      \ /  
       0   
      /|\  
      / \  
            
    ^^^^^^^
    ""","""
        
      
        
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
    
 

  def life_tracker (self, success):
    if success == False:
      self.life += 1