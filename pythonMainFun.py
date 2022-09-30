"""
if we think in Java, C and other languages our program is starting from main functions...
C:
    #include<studio.h>
        void main(){
            // Do something...
            }
Java:
        public static void main(String args[]){
            // Do something...
            }
similarly in python _ _name_ _ is a free define variable which set to main and 'if _ _ name == "_ _main_ _"' is used
an entry point for any python program.
"""
print("the output of '_ _name_ _' is: ", __name__)

def calculate_area(base, height):
    print("Something...")
    return 1/2 * (base * height)
if __name__ == "__main__":
    area = calculate_area(4,5)
    print("The calculated area is: ", area)

# now the question is, when the value of _ _name_ _ is something other than _ _main_ _ ?