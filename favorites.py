print("ඞSUSSY birb")
print("   _____   ")
print("  (' v ')  ")
print(" ((_____)) ")
print("    ^ ^    ")

import random
#import time
inventory =[" ", " ", " ", " ", " ", " "]
PlayerHealth = 100

def BossBattle(PlayerHealth):#This is my battle system in which I will have my fights with robots
    RobotHealth = 50
    import winsound
    winsound.Beep(500,500)
    while PlayerHealth > 0 and RobotHealth > 0:
        if inventory[1]=="laser arm":#I made it so if you have the laser arm you do more damage 
            damage = random.randrange(10,41)
        else:  
            damage = random.randrange(5,11)
        print("You hit the robot for", damage, "HP")
        RobotHealth -= damage
        damage = random.randrange(10, 41)
        print("The robot attacks back for", damage, "HP")
        PlayerHealth -= damage
        
        print("you have now", PlayerHealth, "HP left, the robot has", RobotHealth, "HP left ")
        choice = input("press h for hyper elixir or press b for butter finger, any other key to continue")
        if choice == "h":
            if inventory[2]=="hyper elixir":#I added a hyper elixir or potion that will heal you if you press h
                print("drinking noises, ahhh, (xp+40)")#this item will grant you health if you press h but you need to get it first
                PlayerHealth +=40
                inventory[2]= " "#once after you use it, it goes away
            else:
                print("sorry in canadian accent, you haven no potion")
        if choice == "b":
            if inventory[0]=="butter finger":#a butter finger as a final result, instant kill to you or greg #This is just a butter finger
                print("you pull out a butter finger and throw it at Greg, they catch it and an alien apperas ripping it to shreds leaving nothing behind but a mangaled machine and leaves saying, no one puts a finger on my butter finger")
                RobotHealth = 0
            else:
                print("the robot does not catch the butter finger and smacks you to the wall")
                PlayerHealth = 0
        print()
    if PlayerHealth <=0:#if my health is less than or equal 0 then I die
        print("you died")
    else:
        print("you deafeated the robot")
        
    return PlayerHealth    
#-------- -------------------------------------
def FloorFall(newhealth):
    num = random.randrange(0,100)
    if inventory[1]=="hover boots":#this item will help decrease your chances of falling to you death
        if num < 50:
          print("you fell and died")
          PlayerHealth = 0
          return PlayerHealth
        elif num < 40:
          print("the floor is jammed and you proceed forward")
          PlayerHealth = 100
          return PlayerHealth
        else:
          print("nothing happened")
          PlayerHealth = 100
          return PlayerHealth
    else:
        if num < 70:
          print("you fell and died")
          PlayerHealth = 0
          return PlayerHealth
        elif num < 10:
          print("the florr is jammed and you proceed forward")
          PlayerHealth = 100
          return PlayerHealth 
        else:
          print("nothing happened")
          PlayerHealth = 100
          return PlayerHealth
#-----------------------------------------
DoExit = False
room = 1
while DoExit == False and PlayerHealth>0:#This is so you can print your inventory and health whevener you want
    print("--------------------")
    print("your health is", PlayerHealth)
    print("your inventory:", end = " ")
    for i in range (len(inventory)):
        print(inventory[i], end = " ")
    print()
  
    if room == 1:
        choice = input("hello human, my name is Greg, your friends thought it would be funny to put you in a robotic death chamber while you were asleep. The only way to get is through one of the two pathways. Once you get to the final room you need to defeat me. You can go south or east Good Luck!")
        print("there's a butter finger in your pocket, you decide to keep it, it may come in handy later on")
        inventory[0]!= "butter finger"
        inventory[0]="butter finger"
        if choice == 'south':
            room = 2
        elif choice == 'east':
            room = 12
    if room == 2:
        choice = input("You've chosen the first pathway, I guess this is a good time to mention that you will have to fight some deadly robots before you can reach me, you can go north or west")
        if choice == 'north':
            room = 1
        elif choice == 'west':
            room = 3
    if room == 3:
        print("you enter a dark and silent room, you can go east or south")
        print("a bright light appears from the ground a weapon has been granted to you")
        choice = input()
        if choice == 'grab weapon':
          print("you got a laser arm")
          inventory[1]="laser arm"
        if choice == 'east':
            room = 2
        elif choice == 'south':
            room = 4
    if room == 4:
        choice = input("you have entered a room where you notice the number of people who have been inside this death chamber, none have survived, you may proceed north or south")
        if choice == 'north':
            room = 3
        elif choice == 'south':
            room = 5          
    if room == 5:
        print("you have entered a room full of crates, go north or east")
        print("theres a crate with a unique design in the middle you can open crate")
        choice = input()
        if choice == 'open crate':
            print("there's a hyper elixir *the sauce* inside")
            inventory[2]="hyper elixir"
        if choice == 'north':
            room = 4
        elif choice == 'east':
            room = 6    
          
    if room == 6:#Mini Boss 
      print("A robot has emerged from the floor")
      PlayerHealth =  BossBattle(PlayerHealth) 
      choice = input("you stand on top of the robot you have deafeated, the door opens, proceed west or east")
      if choice == 'west':
          room = 5
      elif choice == 'east':
          room = 7
      #break
    if room == 7:
        choice = input("Greg appears from the ceiling in shock, well you survived that well congrats it would definetly be a shame if another robot pops us, proceed west or east")
        if choice == 'west':
            room = 6
        elif choice == 'east':
            room = 8           
    if room == 8:
        choice = input("you enter a room similar to the one filled with all the last people who up to that point but in this room there is nothing, no one has made it this far, proceed west or north")
        if choice == 'west':
            room = 7
        elif choice == 'north':
            room = 9            
    if room == 9:#Mini Boss
        print("A robot has emerged from the floor")
        PlayerHealth =  BossBattle(PlayerHealth) 
        #break
        choice = input("Greg springs up filled with rage, NOO THAT CANT BE YOU SHOULD BE DEAD BY NOW, proceed south or east")
        if choice == 'south':
            room = 8
        elif choice == 'east':
            room = 10      
    if room == 10:
        choice = input("Greg sitll in the same spot as the other room, YOU WILL NOT SURVIVE AGAINST ME MARK MY WORDS HUMAN, proceed west or east")
        if choice == 'west':
            room = 9
        elif choice == 'east':
            room = 11    

          
    if room == 11:#Final Boss
      print("Greg with all his might appears in front of you ready to end you once and for all")
      PlayerHealth = BossBattle(PlayerHealth)
      break#I added a break here so both the function and the game ends all together
        
            
    if room == 12:
        choice = input("You've chosen the second pathway, good choice this pathway is the least hardest if you're able to survive the death traps and random teleportation have fun, you may proceed west or east")
        if choice == 'west':
            room = 1
        elif choice == 'east':
            room = 13      
    if room == 13:
        print("you enter a dark and silent room, you can go west or north")
        print("the floor opens and smoke comes out, once cleared out you notice a pair of boots appear before you")
        choice = input()
        if choice == 'grab boots':
          print("you got hover boots")
          inventory[1]="hover boots"
        if choice == 'west':
            room = 12
        elif choice == 'north':
            room = 14            
    if room == 14:
      #print("a blue portal appears out of nowhere you are sucked into it")
      #RoomRandimizer()
      #choice = input()
        choice = input("you enter a room where you see all the people who have been inside this death chamber so far most have made it this far but their fate is still to be known, you may proceed south or east")
        if choice == 'south':
            room = 13
        elif choice == 'east':
            room = 15       
    if room == 15:
        print("you're in the next room and you look around, you notice that there is nothing on the walls, no one has survived up to this point, the floor is going to open")
        print("you may proceed west or east")
        choice = input()
        PlayerHealth = FloorFall(PlayerHealth) 
        if PlayerHealth == 0:
          break
        if choice == 'west':
            room = 14
        elif choice == 'east':
            room = 16            
    if room == 16:
        choice = input("Greg appers from the ceiling laughing, well that was pretty impressive human it would be a shame if this room is similar to the last one, you may proceed west or south")
        PlayerHealth = FloorFall(PlayerHealth) 
        if PlayerHealth == 0:
          break
        if choice == 'west':
            room = 15
        elif choice == 'south':
            room = 17
    if room == 17:
        choice = input("Greg emergers in anger, HOW DID YOU SRVIVE THAT IT CANT BE, proceed north or south")
        if choice == 'north':
            room = 16
        elif choice == 'south':
            room = 18
    if room == 18: 
        choice = input("still outraged Greg screams, YOUR LUCK ENDS NOW HUMAN, proceed north or south")
        if choice == 'north':
            room = 17 
        elif choice == 'south':
            room = 11      
#---------------------------------------------------------------------
if PlayerHealth <= 0:
  print("You lost")
else:
  print("YOU WON, you have survived the death chamber")
