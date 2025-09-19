**Purpose / Problem:**<br><br>
* For typical application existing of multiple instances is so common, but there were some special tasks which requires creation of only single instance of that class.
* Tasks like logger, DBconnections needs only a single instance to handle them. Using multiple instances in these tasks leads to inconsistency, overwritten logs, and can also leads to critical breakdown of the services.
* Hence, Singleton Pattern allows us to maintain thoses services while using just a Single instance.
**What is Singleton Pattern?**<br><br>
Singleton pattern is one of the Creational Design Patterns, which ensures that a class will have only one object created and deals with it's maintaince.<br><br>
**Implementation:**<br><br>
1. **Eager Loading:**<br>
Object of the class is created when the class is loaded.
* Pro: Easy to implement, simple to debug, Thread safe<br>
* con: Leads to potential memory wastage of resources when not used.<br><br>
2. **Lazy Loading:**<br>
Object will be created only when getInstance() method is called.
* Pro: Instance created only when getInstance() is called, Memory efficient
* con: 
    1. Complex code included like synchronising, double checking, inner class if thread safety is implemented
    2. Not Thread safe by default.
**Thread Safety in Lazy Loading:**<br><br>
1. Double Check Locking.
2. Synchronised 
3. Bull Heigh Locking (Synchronise only while creation)
4. Using inner Helper class
5. Eager loading (Not prefered and inefficient)