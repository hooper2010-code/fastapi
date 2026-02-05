from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

tasks = []
id_counter = 1

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    global id_counter
    data = request.get_json()

    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400

    new_task = {
        'id': id_counter,
        'title': data['title'],
        'description': data.get('description', ''),
        'status': 'todo',
        'created_at': datetime.utcnow().isoformat(),
        'updated_at': datetime.utcnow().isoformat()
    }

    tasks.append(new_task)
    id_counter += 1

    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()

    for task in tasks:
        if task['id'] == task_id:
            task['title'] = data.get('title', task['title'])
            task['description'] = data.get('description', task['description'])
            task['status'] = data.get('status', task['status'])
            task['updated_at'] = datetime.utcnow().isoformat()
            return jsonify(task)

    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            deleted = tasks.pop(i)
            return jsonify(deleted)
    return jsonify({'error': 'Task not found'}), 404
@app.route('/')
def home():
    return jsonify({"message": "Task API is running"})

if __name__ == '__main__':
    app.run(port=3000, debug=True)