#Import Library
import sys

#Assuming middle of Mic1 & Mic2 is North
#Layout:
#         Mic1    Mic2
#             Mic5
#         Mic3    Mic4

# Main argument that tells the distance range and the direction of the bird sounds 
def main(mic_one, mic_two, mic_three, mic_four, mic_five):
    if mic_one and mic_two and mic_three and mic_four and mic_five == True:
        print("0-20 ft")
        print("Center")
    elif mic_one and mic_two and mic_four and mic_five == True:
        print("15-35 ft")
        print("NorthEast")
    elif mic_two and mic_three and mic_four and mic_five == True:
        print("15-35 ft")
        print("SouthEast")
    elif mic_one and mic_three and mic_four and mic_five == True:
        print("15-35 ft")
        print("SouthWest")
    elif mic_one and mic_two and mic_three and mic_five == True:
        print("15-35 ft")
        print("NorthWest")
    #Error Mic 5 should detect presence  
    elif mic_one and mic_two and mic_three and mic_four == True:
        print("0-20 ft")
        print("Center")
    #Error Mic 5 should detect presence and possbily Mic 4. 
    elif mic_one and mic_two and mic_three == True:
        print("0-35 ft")
        print("Center to NorthWest")
    #Error Mic 5 should detect presence and possbily Mic 4.
    elif mic_one and mic_three and mic_four == True:
        print("0-35 ft")
        print("Center to SouthWest")
    #Error Mic 5 should detect presence and possbily Mic 4.
    elif mic_two and mic_three and mic_four == True:
        print("0-35 ft")
        print("Center to SouthEast")
    #Error Mic 5 should detect presence and possbily Mic 4.
    elif mic_one and mic_two and mic_four == True:
        print("0-35 ft")
        print("Center to NorthEast")
    elif mic_one and mic_two and mic_five == True:
        print("20-45 ft")
        print("North")
    elif mic_two and mic_four and mic_five == True:
        print("20-45 ft")
        print("East")
    elif mic_three and mic_four and mic_five == True:
        print("20-45 ft")
        print("South")
    elif mic_one and mic_three and mic_five == True:
        print("20-45 ft")
        print("West")
    elif mic_one and mic_two == True:
        print("45-55 ft")
        print("North")
    elif mic_two and mic_five == True:
        print("35-45 ft")
        print("NorthEast")
    elif mic_two and mic_four == True:
        print("45-55 ft")
        print("East")
    elif mic_four and mic_five == True:
        print("35-45 ft")
        print("SouthEast")
    elif mic_three and mic_four == True:
        print("45-55 ft")
        print("South")
    elif mic_three and mic_five == True:
        print("35-45 ft")
        print("SouthWest")
    elif mic_one and mic_three == True:
        print("45-55 ft")
        print("West")
    elif mic_one and mic_five == True:
        print("35-45 ft")
        print("NorthWest")
    elif mic_two == True:
        print("45-75 ft")
        print("NorthEast")
    elif mic_four == True:
        print("45-75 ft")
        print("SouthEast")
    elif mic_three == True:
        print("45-75 ft")
        print("SouthWest")
    elif mic_one == True:
        print("45-75 ft")
        print("NorthWest")
    #Error 1 or more other mics should be detected
    elif mic_five == Ture:
        print ("0-45 ft")
        print ("Center")
        
# calling the main functions 
if __name__ == "__main__":
  # Take in the arugments from the Backend as sys arguments 
  system_input = sys.argv[1]
  system_input = system_input.split(' ')
  
  mic_one = True if system_input[0] == '1' else False
  mic_two = True if system_input[1] == '1' else False
  mic_three = True if system_input[2] == '1' else False
  mic_four = True if system_input[3] == '1' else False
  mic_five = True if system_input[4] == '1' else False 

  # passing the sys arguments to the main function 
  main(mic_one, mic_two, mic_three, mic_four, mic_five)










 
    
