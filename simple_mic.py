#Import Library
import sys

# Main argument that tells the distance range and the direction of the bird sounds 
def main(mic_one, mic_two, mic_three, mic_four, mic_five):
    if mic_one and mic_two and mic_three and mic_four and mic_five == True:
        print("0-5 ft")
        print("Center")
    elif mic_one and mic_two and mic_four and mic_five == True:
        print("5-10 ft")
        print("NorthEast")
    elif mic_two and mic_three and mic_four and mic_five == True:
        print("5-10 ft")
        print("SouthEast")
    elif mic_one and mic_three and mic_four and mic_five == True:
        print("5-10 ft")
        print("SouthWest")
    elif mic_one and mic_two and mic_three and mic_five == True:
        print("5-10 ft")
        print("NorthWest")
    elif mic_one and mic_two and mic_three and mic_four == True:
        print("0-5 ft")
        print("Center")
    elif mic_one and mic_two and mic_three == True:
        print("0-10 ft")
        print("Center to NorthWest")
    elif mic_one and mic_three and mic_four == True:
        print("0-10 ft")
        print("Center to SouthWest")
    elif mic_two and mic_three and mic_four == True:
        print("0-10 ft")
        print("Center to SouthEast")
    elif mic_one and mic_two and mic_four == True:
        print("0-10 ft")
        print("Center to NorthEast")
    elif mic_one and mic_two and mic_five == True:
        print("5-20 ft")
        print("North")
    elif mic_two and mic_four and mic_five == True:
        print("5-20 ft")
        print("East")
    elif mic_three and mic_four and mic_five == True:
        print("5-20 ft")
        print("South")
    elif mic_one and mic_three and mic_five == True:
        print("5-20 ft")
        print("West")
    elif mic_one and mic_two == True:
        print("20-40 ft")
        print("North")
    elif mic_two and mic_five == True:
        print("10-20 ft")
        print("NorthEast")
    elif mic_two and mic_four == True:
        print("20-40 ft")
        print("East")
    elif mic_four and mic_five == True:
        print("10-20 ft")
        print("SouthEast")
    elif mic_three and mic_four == True:
        print("20-40 ft")
        print("South")
    elif mic_three and mic_five == True:
        print("10-20 ft")
        print("SouthWest")
    elif mic_one and mic_three == True:
        print("20-40 ft")
        print("West")
    elif mic_one and mic_five == True:
        print("10-20 ft")
        print("NorthWest")
    elif mic_two == True:
        print("20-50 ft")
        print("NorthEast")
    elif mic_four == True:
        print("20-50 ft")
        print("SouthEast")
    elif mic_three == True:
        print("20-50 ft")
        print("SouthWest")
    elif mic_one == True:
        print("20-50 ft")
        print("NorthWest")



# calling the main functions 
if __name__ == "__main__":
  # Take in the arugments from the Backend as sys arguments 
  mic_one = True if sys.argv[1] == '1' else False
  mic_two = True if sys.argv[2] == '1' else False 
  mic_three = True if sys.argv[3] == '1' else False 
  mic_four = True if sys.argv[4] == '1' else False
  mic_five = True if sys.argv[5] == '1' else False
  # passing the sys arguments to the main function 
  main(mic_one, mic_two, mic_three, mic_four, mic_five)










 
    
