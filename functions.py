
def get_todos(filepath = "todos.txt"):
    ''' Read a text file and return the list of 
    To-do items.
    '''
    with open(filepath,'r') as local_file:
        local_todos = local_file.readline()
    return local_todos

def write_todos(todos_arg,filepath = "todos.txt"):
    ''' Write the To-do items list in the text file.
    '''
    with open(filepath,'w') as file:
        file.writelines(todos_arg)