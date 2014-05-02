import os
from comments import PyCodeFile

def scan_folder(path):

    #Total number of comments and non comments of the entire directory

    total_comments = 0
    total_non_comments = 0
    file_count =0 

    #Traversing through the entire directory
    for file in os.listdir(path):
        if file.endswith(".py"):
            file_count +=1
            print file
            file_object= open(file)
            ob = PyCodeFile(file_object)

            #Reintilaizes the pointer from end of the file to the star
            file_object.seek(0)
            
            file_comment_count = ob.comments(file_object)

            #Reintilaizes the pointer from end of the file to the star
            file_object.seek(0)
            file_non_comment_count = ob.non_comments(file_object)

            ob.ratio(file_comment_count, file_non_comment_count);

            
            total_comments = total_comments + file_comment_count
            total_non_comments = total_non_comments + file_non_comment_count

    if file_count == 0:
        print " No .py files in the directory. Please chose another directory "
    else:
        print "Total comment lines in the directory:", total_comments
        print "Total non comment lines in the directory:", total_non_comments
            
        

def main():

    user_input = raw_input("Enter the directory path. Please make sure the path is of the format /users/...:")
    scan_folder(user_input)

main()
