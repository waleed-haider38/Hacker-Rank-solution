# f = open("content.txt" , "w")
# f.write("Assalam o Alaikum! I am starting file handling today")
# f.close()

# f = open("content.txt" , "r")
# print(f.read())
# f.close()

# with open("content.txt", "r") as f:
#     print(f.read())

# import os

# cwd = os.getcwd()
# print("Current working directory:", cwd)

# import os

# def script_dir():
#     # agar __file__ available hai (means script run ho rhi hai)
#     if "__file__" in globals():
#         return os.path.dirname(os.path.abspath(__file__))
#     else:
#         # interactive mode (REPL / Jupyter)
#         return os.getcwd()
    
# print("Script directory:", script_dir())

import os

# # 1) Current directory
# print("Current dir:", os.getcwd())

# # 2) List items in current directory
# print("Items in current dir:", os.listdir())

# # 3) Make new folder
# os.mkdir("demo_folder")
# print("After mkdir:", os.listdir())

# # 4) Change into that folder
# os.chdir("demo_folder")
# print("Now inside:", os.getcwd())

# # 5) Go back (parent directory)
# os.chdir("..")
# print("Back to:", os.getcwd())

# # 6) Remove foldera
# os.rmdir("demo_folder")
# print("After remove:", os.listdir())

import os

def make_and_chng(folder_name):
    # 1) Agar folder exist nahi karta to banao
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    
    # 2) Absolute path nikalo
    path = os.path.abspath(folder_name)
    
    # 3) Folder ke andar ki items list karo
    items = os.listdir(folder_name)
    
    # 4) Print + return
    print("Folder path:", path)
    print("Items inside:", items)
    return path

    
