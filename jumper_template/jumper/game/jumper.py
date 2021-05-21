class Jumper:
  """ 
  Keeps track of parachute. Removes lines if needed and also keeps track of lives.
  
  Stereotype: Info Holder
  """
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