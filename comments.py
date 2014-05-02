class PyCodeFile:
  
  #Class Constructor
  
  def __init__(self, fileobject):

    #Calls the non_comments function
    count = self.non_comments(fileobject)

    #Resets the pointer to the starting of the file
    fileobject.seek(0)

    #Calls the comments function
    comments_count = self.comments(fileobject)
  
    print "Comment lines:", comments_count
    print "Total number of lines:", comments_count + count
  
  
  def comments(self,fileobject):
    comment_count =0
    for line in fileobject:
      li=line.strip()
      if li.startswith("#"):
        comment_count +=1 
    return comment_count
  
  def non_comments(self, fileobject):
    count = 0
    for line in fileobject:
      li=line.strip()
      if not li.startswith("#"):
        count +=1
    return count
    
  def ratio(self, number1, number2):
    num1= number1
    num2 = number2
    while num1 != num2:  
        if num1 > num2:  
            num1 -= num2  
        elif num2 > num1:  
            num2 -= num1
                
    if num1 == 0:
      print "Ratio:", number1,":",number2
    else:
      print "Ratio:", number1/num1, ":", number2/num1
    print '\n'
    

  
