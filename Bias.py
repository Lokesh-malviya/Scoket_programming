#initalising every 
instances=["X1","X2","X3","X4","X5","X6","X7","X8","X9"]
choiceby=["male","female","male","male","female","female","female","male","male"]
ranges=["100-500","500-1000","100-500","500-1000","100-500","100-500","1000-1500","1000-1500","500-1000"]
monthend=["yes","yes","no","yes","no","yes","no","no","no"]
whethertobuy=["yes","no","yes","no","yes","yes","yes","no","no"]
def table():
    print("S.no\tInstances\tChoiceBy\tRanges\t\tMonthEnd\tWhether to buy?")
    print("================================================================================")
    for i in range(9):
        print(str(i+1) + "\t" +instances[i] + "\t\t" +choiceby[i]+ "\t\t" +ranges[i]+ "\t\t" +str(monthend[i])+ "\t\t" +whethertobuy[i])
    
table()
       
yes_count = 0
no_count = 0

for i in range(9):
  if whethertobuy[i] == "yes":
    yes_count += 1
  elif whethertobuy[i] == "no":
    no_count += 1

print("total nummber of yes count: ",yes_count)
print("total number of no count: ",no_count)

def today(c,r,m):
  # Calculating conditional probability given yes
  c_yes = 0
  for i in range(9):
    if choiceby[i] == c and whethertobuy[i] == "yes":
      c_yes += 1

  r_yes = 0
  for i in range(9):
    if ranges[i] == r and whethertobuy[i] == "yes":
      r_yes += 1

  m_yes = 0
  for i in range(9):
    if monthend[i] == m and whethertobuy[i] == "yes":
      m_yes += 1
  
 

  conditional_p_yes_old = (yes_count/(yes_count + no_count))*(c_yes/yes_count)*(r_yes/yes_count)*(m_yes/yes_count)

  # Calculating conditional probability given no
  c_no = 0
  for i in range(9):
    if choiceby[i] == c and whethertobuy[i] == "no":
      c_no += 1

  r_no = 0
  for i in range(9):
    if ranges[i] == r and whethertobuy[i] == "no":
      r_no += 1

  m_no = 0
  for i in range(9):
    if monthend[i] == m and whethertobuy[i] == "no":
      m_no += 1
  


  conditional_p_no_old =   (no_count/(yes_count + no_count))*(c_no/no_count)*(r_no/no_count)*(m_no/no_count)
 

  # Final probabilities
  conditional_p_yes = conditional_p_yes_old/(conditional_p_yes_old + conditional_p_no_old)
  conditional_p_no = conditional_p_no_old/(conditional_p_yes_old + conditional_p_no_old)

  return [conditional_p_yes,conditional_p_no]

today("female","100-500","no")