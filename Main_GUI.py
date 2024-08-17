from tkinter import *
from tkinter import ttk
from Graph_visualization import visualize
from ChessMain import main


def chess():
    main()
    
'''
the command that get executed when the user click start
it get the method chosen by the user from the combobox
get the entry of the graph textarea and fill it in the text file
as well as the heuristic valuesof the nodes fron the second textarea
'''
def start():
    method=method_combobox.get()
    print(method)
    with open('heuristic.txt', 'w') as txt_file:
        txt_file.write(heuristic_text_area.get(1.0, END))
    with open('graph.txt', 'w') as text_file:
        text_file.write(text_area.get(1.0, END))
    visualize(start_state,goal_state,method)

root= Tk()
root.title("IntelliSolver")
root.iconbitmap('icon.ico')
root.geometry("550x620")


#input frame
input= Frame(root)
input.grid(row=0,column=1)

# first frame
graph_info_frame=LabelFrame(input,text="Enter Problem",padx=10,pady=10)
graph_info_frame.grid(row=0,column=0,sticky="news")

start_state_label=Label(graph_info_frame,text="Start State: ")
start_state_label.grid(row=0,column=0)

goal_state_label=Label(graph_info_frame,text="Goal State: ")
goal_state_label.grid(row=1,column=0)

input_tree= Label(graph_info_frame,text="Input Your Graph: ")
input_tree.grid(row=2,column=0)

text_area= Text(graph_info_frame,width=20,height=12,font=("Helvetica",10))
text_area.grid(row=2,column=1)

'''
the start state entry needs to be modified from the IDE because of networkx library errors
the right way to get the start state from the user is
start_state=start_state_entry.get()
but this last is conflicting with some functions in the networkx library
'''
start_state_entry=Entry(graph_info_frame)
start_state_entry.grid(row=0,column=1)
start_state=1

#the goal state entry needs to be modified from the IDE because of networkx library errors
goal_state_entry=Entry(graph_info_frame)
goal_state_entry.grid(row=1,column=1)
goal_state=13

for widget in graph_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=10)

# second frame
search_method_frame=LabelFrame(input,text="Search Algorithm",padx=10,pady=10)
search_method_frame.grid(row=1,column=0,sticky="news")

method=Label(search_method_frame,text="Search Algorithm: ")
method.grid(row=0,column=0)

method_combobox= ttk.Combobox(search_method_frame,values=["A* Search","Breadth First Search","Deapth First Search","Uniform Cost Search"])
method_combobox.current(0) 
method_combobox.grid(row=0,column=1)
method_combobox.bind("<<ComboboxSelected>>")

heuristic_values= Label(search_method_frame,text="Input Hueristic values: ")
heuristic_values.grid(row=1,column=0)

heuristic_text_area= Text(search_method_frame,width=18,height=8,font=("Helvetica",10))
heuristic_text_area.grid(row=1,column=1)

Start=Button(search_method_frame,text="   Start   ",command=start)
Start.grid(row=2,column=2)


#add the padding in all the elements of the frame instaed of writing it each time
for widget in search_method_frame.winfo_children():
    widget.grid_configure(padx=10,pady=10)

#third frame 
game_frame=LabelFrame(input,text="Play",padx=10,pady=10)
game_frame.grid(row=0,column=1,sticky="news")

Choose=Label(game_frame,text="Choose a game :")
Choose.grid(row=0,column=0)

chess_botton=Button(game_frame,text="Chess", command=chess)
chess_botton.grid(row=1,column=0)


for widget in game_frame.winfo_children():
    widget.grid_configure(padx=10,pady=10)


root.mainloop()