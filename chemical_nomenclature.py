#copyright Lindsay Cheng (c) 2023
#imports
import time 

def welcome_message():
  #cover
  print("\n\nNaming Compounds: Atomic Labels")
  time.sleep(2)

  print("\n\n\n")

  #instructions/info
  time.sleep(2)
  print("Hello! \nYour friend, a chemist, has asked for help with a project. They are out of town and are hoping you can complete a few experiments for them.") 
  time.sleep(7)
  print("\nYou agree to help and let yourself into their lab. However, you quickly find that the jars don't all have proper labels--some have molecular diagrams instead of written names.")
  time.sleep(6)
  print("\nRegardless (though not recommended), you try to make use of background knowledge to figure out which compound is which.")
  time.sleep(6)
  print("\nFor help anytime, please type:")
  time.sleep(1)
  print("\n[Prefix] Prefix Help")
  time.sleep(1)
  print("[Covalent] Help with Covalent Compounds")
  time.sleep(1)
  print("[Ionic] Help with Ionic Compounds")
  time.sleep(3)

def prefix_help():
  print("\nPrefixes:")
  time.sleep(1)
  print("\n\n1 = either mono- or no prefix")
  time.sleep(1)
  print("2 = di-")
  time.sleep(1)
  print("3 = tri-")
  time.sleep(1)
  print("4 = tetra-")
  time.sleep(1)
  print("5 = penta-")
  time.sleep(1)
  print("6 = hexa-")
  time.sleep(1)
  print("7 = hepta-")
  time.sleep(1)
  print("8 = octa-")
  time.sleep(1)
  print("9 = nona-")
  time.sleep(1)
  print("10 = deca-")

def covalent_help():
  print("\nHelp with Covalent Compounds:")
  time.sleep(2)
  print("\nUse prefixes to indicate how many atoms of each element is in the compound.")
  time.sleep(2)
  print("\nEx: PF6 = Phosphorous hexafluoride")
  time.sleep(2)
  print("\nType 'Prefix' for help with prefixes.")

def ionic_help():
  print("\nHelp with Ionic Compounds:")
  time.sleep(2)
  print("\nFor ionic compounds, the format is cation + anion (e.g., ZnCl2 = zinc (cation) chloride (anion) --> zinc chloride")
  time.sleep(4)
  print("The name of the cation is kept, while the anion ends with -ide.")
  time.sleep(2)
  print("To determine the formula with subscripts, write the element with its charge, then use the criss cross method.")
  time.sleep(2)

#answer processing function
def answer_process(answer, correct):
  
  if answer.upper() == "PREFIX":
    prefix_help()
    return False
    
  elif answer.upper() == "COVALENT":
    covalent_help()
    return False
    
  elif answer.upper() == "IONIC":
    ionic_help()
    return False
  
  elif answer.upper() == correct:
     print("That is correct.")
     return True

  else: return False
    
#main function
welcome_message()

#question 1
time.sleep(2)
print("\nIn the first experiment, you combine one atom of xenon with four atoms of fluorine. What do you end up with?")
time.sleep(2)
print("\n[A] xenon fluoride")
print("[B] monofluoride xenon")
print("[C] tetraxenon fluoride")
print("[D] xenon tetrafluoride")

ans1 = input("\nWhich letter would you like to pick (type letter choice)? ")

while(answer_process(ans1, "D") == False):
  ans1 = input("\nPlease try again. Which letter would you like to pick? ")

#question 2
time.sleep(2)
print("\nYou then combine three atoms of calcium with two atoms of phosphorous. What do you end up with?")
time.sleep(2)
print("\n[A] diphosphate tricalcium")
print("[B] tricalcium diphosphate")
print("[C] calcium phosphate")
print("[D] phosphate calcium")

ans2 = input("\nWhich letter would you like to pick? ")

while(answer_process(ans2, "C") == False):
  ans2 = input("\nPlease try again. Which letter would you like to pick? ")

#question 3
time.sleep(2)
print("\nYou then come across a bottle with the compound written. What is Se2Cl2?")
time.sleep(2)
print("\n[A] selenium chloride")
print("[B] diselenium dichloride")
print("[C] dichloride diselenium")
print("[D] disulfur dichlorine")

ans3 = input("\nWhich letter would you like to pick? ")

while(answer_process(ans3, "B") == False):
  ans3 = input("\nPlease try again. Which letter would you like to pick? ")

#question 4
time.sleep(2)
print("\nYou've successfully completed the experiment when your friend emails about another test they're curious about. They ask if you could find a bottle of calcium iodide. What formula are you looking for?")
time.sleep(2)
print("\n[A] CaI2")
print("[B] Ca2I")
print("[C] CI")
print("[D] Ca2I2")

ans4 = input("\nWhich letter would you like to pick? ")

while(answer_process(ans4, "A") == False):
  ans4 = input("\nPlease try again. Which letter would you like to pick? ")

#question 5
time.sleep(2)
print("\nThey then ask you to find a bottle with this diagram: Two sulfur atoms bonded with ten fluorine atom. The bottle, they say, should read disulfur decafluoride. Which are you looking for?")
time.sleep(2)
print("\n[A] SF")
print("[B] F2S10")
print("[C] F10S2")
print("[D] FS")

ans5 = input("\nWhich letter would you like to pick? ")

while(answer_process(ans5, "B") == False):
  ans5 = input("\nPlease try again. Which letter would you like to pick? ")

#question 6
time.sleep(2)
print("\nOn the shelf, you also notice a bottle of CdS. Which compound is this?")
time.sleep(2)
print("\n[A] carbon sulfide")
print("[B] cadmium sulfate")
print("[C] sulfate cadmium")
print("[D] cadmium sulfide")

ans6 = input("\nWhich letter would you like to pick? ")

while(answer_process(ans6, "D") == False):
  ans6 = input("\nPlease try again. Which letter would you like to pick? ")

#question 7
time.sleep(2)
print("\nYou also notice several ampoules of a gas labeled 'flammable'. The molecular diagram shows two nitrogen atoms bonded to four oxygen atoms. Which compound is this?")
time.sleep(2)
print("\n[A] tetranitride dioxygen")
print("[B] dinitrogen tetroxide")
print("[C] tetranitrogen dioxygen")
print("[D] decanitrogen tetraoxide")

ans7 = input("\nWhich letter would you like to pick? ")

while(answer_process(ans7, "B") == False):
  ans7 = input("\nPlease try again. Which letter would you like to pick? ")

#question 8
time.sleep(2)
print("\nYou then notice pale brown crystals lying in another ampoule. The label reads Al4C3. Which compound is this?")
time.sleep(2)
print("\n[A] tetraluminum tricarbide")
print("[B] aluminum tetracarbon")
print("[C] tetraluminide trichloride")
print("[D] aluminum carbide")

ans8 = input("\nWhich letter would you like to pick? ")

while(answer_process(ans8, "D") == False):
  ans8 = input("\nPlease try again. Which letter would you like to pick? ")

#question 9
time.sleep(2)
print("\nYour friend thanks you for your help and also mentions that to show appreciation, they can guide you through the \"barking dog reaction\", which they think you will enjoy. The first compound is NO. Which compound is this?")
time.sleep(2)
print("\n[A] monoxygen mononitrogen ")
print("[B] nitrogen monoxide")
print("[C] nitride monoxide")
print("[D] nitroxide")

ans9 = input("\nWhich letter would you like to pick? ")

while(answer_process(ans9, "B") == False):
  ans9 = input("\nPlease try again. Which letter would you like to pick? ")

#question 10
time.sleep(2)
print("\nThe second compound is CS2, which is:")
time.sleep(2)
print("\n[A] dicarbon sulfide")
print("[B] dicesium ")
print("[C] carbon disulfide")
print("[D] carboxyl sulfide")

ans10 = input("\nWhich letter would you like to pick? ")

while(answer_process(ans10, "C") == False):
  ans10 = input("\nPlease try again. Which letter would you like to pick? ")

time.sleep(3)
print("Once you combine nitrogen monoxide and carbon disulfide in a tube, you see a blue flash and hear a loud barking sound. ")
time.sleep(2)
print("\nYour friend tells you over the phone that it has been a success.")
time.sleep(2)
print("Thank you!")
time.sleep(2)

