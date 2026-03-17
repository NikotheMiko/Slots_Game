import time 
import random 
import keyboard as KT

pip_count = [1,2,3,4,5,6]

score = 100 


#logic for slots game hold array of images and randomizes them 


class slots_logic:
    #slot machine spin function 
    def spin(count):
        global score
        

        # a pip is the slots for the machine 
        pip1 = random.choice(pip_count)
        pip2 = random.choice(pip_count)
        pip3 = random.choice(pip_count)
        
        
         
        if pip1 == pip2 == pip3:
           print(f"jackpot!")
           print(f"\n | {pip1} | {pip2} | {pip3} |")
           score += 1000
           if pip1 == 3 and pip2 == 3 and pip3 == 3 :
            print(f"MEGA JACKPOT!!!!!")
            score += 1000 * 1000         

        elif pip1 == pip2 or pip1 == pip3 or pip2 == pip3:
            print("great!")
            print(f"\n | {pip1} | {pip2} | {pip3} |")
            score += 25
           
            
        else:
            print("Next time :( ")
            print(f"\n | {pip1} | {pip2} | {pip3} |")
            score -= 100
            
           
    def roll():
         
         while True:
            global score

            if score <= -1000:
                print(f"better luck next time ")
                break
            if KT.is_pressed('p'):
                slots_logic.spin(score)     
                time.sleep(0.2)
            if KT.is_pressed('s'):
                print(score)
                time.sleep(.3)
            
             
            
  
                
       

  
#main method entry point to program
def main():
  slots_logic.roll()
 
  
 

      
   
   
        


if __name__ == "__main__":
    main()


