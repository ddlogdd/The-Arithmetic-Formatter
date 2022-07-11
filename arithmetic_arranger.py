def arithmetic_arranger(problems, Solve = False):
  First =''
  Second = ''
  Seperator = ''
  Addition = ''
  Demacation =''

  if (len(problems)>5):
      return("Error: Too many problems.")
   

  
  for a in problems:
    
    
    First_number = a.split(" ")[0]
    Operator = a.split(" ")[1]
    Second_number = a.split(" ")[2]
    
    if((len(First_number)>= 5 or len(Second_number) >=5)):
      return("Error: Numbers cannot be more than four digits.")
    
    if  Operator == "/" or Operator == "*":
      return("Error: Operator must be '+' or '-'.")

    try:
      a_1 = int(First_number)
      a_2 = int(Second_number)
    except ValueError:
      return("Error: Numbers must only contain digits.")
        
    Sum=''
    dash = "-"
    if Operator == "+":
      Sum = str(int(First_number) + int(Second_number))
    elif Operator =="-":
      Sum = str(int(First_number) - int(Second_number))
        
    largest = max(len(First_number), len(Second_number))
    bal = largest +2
    line = dash *(largest + 2)

        

    Top = f"{First_number:>{bal}}"
    Bottom = f"{Operator}{Second_number:>{bal-1}}"
    Addition = f"{Sum:>{bal}}"
        

    if a != problems[-1]:
      First = First + Top + "    "
      Second = Second + Bottom + "    "
      Seperator = Seperator + line + "    "
      Demacation = Demacation + Addition + "    "
    else:
      First =  First + Top 
      Second =  Second +Bottom
      Seperator =  Seperator + line
      Demacation =  Demacation + Addition

  if Solve:

    Output = f"{First}\n{Second}\n{Seperator}\n{Demacation}"
            
  else:
             
    Output = f"{First}\n{Second}\n{Seperator}"

  return(Output)

