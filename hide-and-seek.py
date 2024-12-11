print("Welcome to hide-and-seek.")
print("Your mission is to find the cat.")

choice1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right".\n ').lower()

if choice1 == "left":
    # Continue in game
    choice2 = input('you\'ve come to a lake. '
                    'There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across\n').lower()
    if choice2 == "wait":
        choice3 = input('You\'ve arrive at the island unharmed. '
                        'There is a house with 3 doors. '
                        'One "red", one "yellow" and one "blue". '
                        'Which colour do you choose?\n' )
        if choice3 == "red":
            print("It's a room full of fire. Game Over!" )
        elif choice3 == "blue":
            print("It's a room full of sharks. Game Over!" )
        if choice3 == "yellow":
            print("You find the cat!")
            print(r'''
                   .                .                    
                   :"-.          .-";                    
                   |:`.`.__..__.'.';|                    
                   || :-"      "-; ||                    
                   :;              :;                    
                   /  .==.    .==.  \                    
                  :      _.--._      ;                   
                  ; .--.' `--' `.--. :                   
                 :   __;`      ':__   ;                  
                 ;  '  '-._:;_.-'  '  :                  
                 '.       `--'       .'                  
                  ."-._          _.-".                   
                .'     ""------""     `.                 
               /`-                    -'\                
              /`-                      -'\               
             :`-   .'              `.   -';              
             ;    /                  \    :              
            :    :                    ;    ;             
            ;    ;                    :    :             
            ':_:.'                    '.;_;'             
               :_                      _;                
               ; "-._                -" :`-.     _.._    
               :_          ()          _;   "--::__. `.  
                \"-                  -"/`._           :  
               .-"-.                 -"-.  ""--..____.'  
              /         .__  __.         \               
             : / ,       / "" \       . \ ;         
              "-:___..--"      "--..___;-"
            ''')

    else:
        print("You got attacked by an angry trout. Game Over." )
else:
    print("You fell in to a hole. Game Over." )
