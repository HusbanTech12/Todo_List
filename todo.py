import click # To create a cli
import os  # To save and load tasks from a file
import json # To check the file exists

TODO_FILE = "todo.json"

def load_tasks():
 if os.path.exists(TODO_FILE):
     return []
 
 with open(TODO_FILE , 'r') as file: # file is a varaible
     return json.load(file)
 
def save_tasks(tasks):
     with open(TODO_FILE , 'w') as file:
       json.dump(tasks, file , indent=4)      
       
       
  # @ means decoratore     
@click.group() # Main work of click       

def cli():
    """Simple Todo List Manager"""
    
@click.command()    
@click.argument('task') # argument take task from a user and then send 

def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()
    tasks.append({'task' : task , 'done' : False})
    save_tasks(tasks)
    click.echo(f"Task Added Completely : {task}")
    
cli.add_command(add)

if __name__ == "__main__":
    cli()    