# HIGH LEVEL PROGRAMMING

## AirBnB Clone

---

### Description
This project is entails the following:
- A _command interpreter__ to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A _website_ (the front-end) that shows the final product to everybody: static and dynamic
- A _database_ or _files_ that store data (data = objects)
- An _API_ that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

---

__Command Interpreter__
The command interpreter part of the this clone allows us to do the following:
- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

__how to start it__
You start the program by running the executable _console.py_.
```bash
mr_robertamoah@DESKTOP-7BU5GMJ:~/alx/AirBnB_clone$ ./console.py
(hbnb) 
```

__how to use it__
You type in you commands in the commandline. The table below shows some of the commands and what it does.
| Commands                                                            | What they do                                           | Usage                                                               |
|---------------------------------------------------------------------|--------------------------------------------------------|---------------------------------------------------------------------|
| create < class name >                                               | this create data models and shows id of model          | create BaseModel                                                    |
| help < command >                                                    | this gives the help message for a command              | help create                                                         |
| show < id >                                                         | this shows the a data model based on its id            | show BaseModel c9450437-fbdc-4076-be88-04d6f5410f2c                 |
| < class name >.show()                                               |                                                        | BaseModel.show(c9450437-fbdc-4076-be88-04d6f5410f2c)                |
| destroy < class name > < id >                                       | this deletes model and remove it from file based on id | destroy BaseModel c9450437-fbdc-4076-be88-04d6f5410f2c              |
| < class name >.destroy()                                            |                                                        | BaseModel.destroy(c9450437-fbdc-4076-be88-04d6f5410f2c)             |
| all                                                                 | this shows all models or all models of a class         | all / all BaseModel                                                 |
| < class name >.all()                                                |                                                        | BaseModel.all()                                                     |
| < class name >.count()                                              | this shows the number of models of a class created     | BaseModel.count()                                                   |
| update < class name > < id > < attribute > < attribute value >      | this allows updating attributes of a model with a value| update BaseModel c9450437-fbdc-4076-be88-04d6f5410f2c name "Robert" |
| < class name >.update(< id >, < attribute >, < attribute value >)   | this allows updating attributes of a model with a value| update BaseModel c9450437-fbdc-4076-be88-04d6f5410f2c name "Robert" |
| < class name >.update(< id >, {< attribute >: < attribute value >}) | this allows updating attributes of a model with a value| update BaseModel c9450437-fbdc-4076-be88-04d6f5410f2c name "Robert" |
| quit / EOF                     | exit from the program                                                                       | quit / ctrl + D                                                     |

__examples__
The following are some examples of the program
```
mr_robertamoah@DESKTOP-7BU5GMJ:~/alx/AirBnB_clone$ ./console.py
(hbnb) 
(hbnb) 
(hbnb) all
[]
(hbnb) 
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) 
(hbnb) quit
mr_robertamoah@DESKTOP-7BU5GMJ:~/alx/AirBnB_clone$
```

---
