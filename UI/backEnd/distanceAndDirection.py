#Import Library
import sys

#Assuming middle of Mic1 & Mic2 is North
#Layout:
#         Mic1    Mic2
#             Mic5
#         Mic3    Mic4

# Main argument that tells the distance range and the direction of the bird sounds 
def main(mic_one, mic_two, mic_three, mic_four, mic_five):
    if mic_one and mic_two and mic_three and mic_four and mic_five:
        print("0-20")
        print("Center")
    elif mic_one and mic_two and mic_four and mic_five:
        print("15-35")
        print("NorthEast")
    elif mic_two and mic_three and mic_four and mic_five:
        print("15-35")
        print("SouthEast")
    elif mic_one and mic_three and mic_four and mic_five:
        print("15-35")
        print("SouthWest")
    elif mic_one and mic_two and mic_three and mic_five:
        print("15-35")
        print("NorthWest")
    #Error Mic 5 should detect presence  
    elif mic_one and mic_two and mic_three and mic_four:
        print("0-20")
        print("Center")
    #Error Mic 5 should detect presence and possibly Mic 4. 
    elif mic_one and mic_two and mic_three:
        print("0-35")
        print("Center to NorthWest")
    #Error Mic 5 should detect presence and possibly Mic 4.
    elif mic_one and mic_three and mic_four:
        print("0-35")
        print("Center to SouthWest")
    #Error Mic 5 should detect presence and possibly Mic 4.
    elif mic_two and mic_three and mic_four:
        print("0-35")
        print("Center to SouthEast")
    #Error Mic 5 should detect presence and possibly Mic 4.
    elif mic_one and mic_two and mic_four:
        print("0-35")
        print("Center to NorthEast")
    elif mic_one and mic_two and mic_five:
        print("20-45")
        print("North")
    elif mic_two and mic_four and mic_five:
        print("20-45")
        print("East")
    elif mic_three and mic_four and mic_five:
        print("20-45")
        print("South")
    elif mic_one and mic_three and mic_five:
        print("20-45")
        print("West")
    elif mic_one and mic_two:
        print("45-55")
        print("North")
    elif mic_two and mic_five:
        print("35-45")
        print("NorthEast")
    elif mic_two and mic_four:
        print("45-55")
        print("East")
    elif mic_four and mic_five:
        print("35-45")
        print("SouthEast")
    elif mic_three and mic_four:
        print("45-55")
        print("South")
    elif mic_three and mic_five:
        print("35-45")
        print("SouthWest")
    elif mic_one and mic_three:
        print("45-55")
        print("West")
    elif mic_one and mic_five:
        print("35-45")
        print("NorthWest")
    elif mic_two:
        print("45-75")
        print("NorthEast")
    elif mic_four:
        print("45-75")
        print("SouthEast")
    elif mic_three:
        print("45-75")
        print("SouthWest")
    elif mic_one:
        print("45-75")
        print("NorthWest")
    #Error 1 or more other mics should be detected
    elif mic_five:
        print ("0-45")
        print ("Center")
        
# calling the main functions 
if __name__ == "__main__":
  # Take in the arguments from the Backend as sys arguments 
  system_input = sys.argv[1]
  system_input = system_input.split(' ')
  
  mic_one = True if system_input[0] == '1' else False
  mic_two = True if system_input[1] == '1' else False
  mic_three = True if system_input[2] == '1' else False
  mic_four = True if system_input[3] == '1' else False
  mic_five = True if system_input[4] == '1' else False 

  # passing the sys arguments to the main function 
  main(mic_one, mic_two, mic_three, mic_four, mic_five)










 
    
