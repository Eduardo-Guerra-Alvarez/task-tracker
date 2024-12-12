from os import path
import argparse
import json
import datetime

current_datetime = datetime.datetime.now()

parse = argparse.ArgumentParser()
parse.add_argument('action', nargs='?')
parse.add_argument('status', nargs='?')
parse.add_argument('updated', nargs='?')

args = parse.parse_args()

filename = 'trackerFile.json'

def check_ifExcist_file():
    if path.isfile(filename) is False:
        writeJson()

def list():
    data = readJson()
    if(args.status is not None):
        data = [obj for obj in data if obj['status'] == args.status]
    for obj in data:
        print(obj)

def addTask():
    data = readJson()
    id = 1 if len(data) == 0 else data[-1]["id"] + 1
    data.append({
        'id': id,
        'description': args.status,
        'status': 'todo',
        'createdAt': str(current_datetime),
        'updatedAt': ''

    })
    writeJson(data)
def updateTask():
    data = readJson()
    for obj in data:
        if(obj['id'] == int(args.status)):
            obj['description'] = args.updated
            obj['updatedAt'] = str(current_datetime)
    writeJson(data)   

def deleteTask():
    data = readJson()
    if any(obj['id'] == int(args.status) for obj in data) :
        data = [obj for obj in data if obj['id'] != int(args.status)]
    else:
        print('id not found')

    writeJson(data)

def markTask(value):
    data = readJson()
    for obj in data:
        if(obj['id'] == int(args.status)):
            obj['status'] = value
    writeJson(data)

def arguments():
    if args.action == 'add':
        addTask()
    elif args.action == 'delete':
        deleteTask()
    elif args.action == 'list':
        list()
    elif args.action == 'update':
        updateTask()
    elif args.action == 'mark-in-progress':
        markTask('in progress')
    elif args.action == 'mark-done':
        markTask('done')
    else: 
        print("Please choice a correct option: add, delete, update, list")

def writeJson(data = []) :
    with open(filename, 'w') as file:
        json.dump(data, file)

'''
def writeJson():
    with open(filename, 'w') as json_file:
        json.dump(listObj, json_file, indent=4, separators=(',',': '))
'''
def readJson():
    with open(filename) as fp:
        return json.load(fp)

check_ifExcist_file()
arguments()
