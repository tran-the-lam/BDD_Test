from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Init todo list
todo_list = []

@app.route('/')
def index():
    return render_template('index.html', todos=todo_list)

@app.route('/add', methods=['POST'])
def add():
    # Get data from form
    task = request.form.get('task')
    if task:
        # Add task to list
        todo_list.append(task) 
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    # Delete task from list
    if 0 <= task_id < len(todo_list):
        todo_list.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)