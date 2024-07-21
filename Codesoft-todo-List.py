import tkinter as tk


#below array is used as a array to carry the todolist throughout the program
tasks_array = []


#this function is used to add a task  to the todolist
def add_task_todolist():
    task = entry.get()
    if task:
        tasks_array.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)


#this function is used to mark a task as completed in the todolist
def complete_task_todolist():
    try:
        index = listbox.curselection()[0]
        tasks_array.pop(index)
        listbox.delete(index)
    except IndexError:#possibly we can only have the indexError in the above function so we have added a try and except block but intetionally left the except block and kept as "pass"
        pass



#this function is used to delete a task from the todolist
def delete_task_todolist():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:#possibly we can only have the indexError in the above function so we have added a try and except block but intetionally left the except block and kept as "pass"
        pass


root = tk.Tk()
root.title("Tharun's To-Do List App")


entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task_todolist)
add_button.pack(pady=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

complete_button = tk.Button(root, text="Mark as Completed", command=complete_task_todolist)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task_todolist)
delete_button.pack(pady=5)

root.mainloop()