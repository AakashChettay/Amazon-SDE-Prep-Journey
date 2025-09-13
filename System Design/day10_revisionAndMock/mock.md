**SOLID & Creational Patterns Deep Dive Quiz**<br><br>
**Questions & Answers**
**Score:10/10**<br><br>
1. Question: A class Shape has a method calculateArea() that needs to be modified every time a new shape (e.g., Circle, Rectangle) is added to the system. Which design principle is being violated?

Your Answer: Open/Closed Principle

Correct Answer: Open/Closed Principle

Result: Correct

2. Question: Which creational design pattern is most suitable when a system needs to create a family of related or dependent objects without specifying their concrete classes?

Your Answer: Abstract Factory

Correct Answer: Abstract Factory

Result: Correct

3. Question: A Car class has a method startEngine() and a method startEngineUsingKey() that overrides the base class method. If the startEngineUsingKey() method throws a new InvalidKeyException, which principle might be violated?

Your Answer: Interface Segregation Principle

Correct Answer: Liskov Substitution Principle

Result: Incorrect

4. Question: Which design pattern is most appropriate for a system where a single object, such as a logger or a database connection pool, needs to be shared across the entire application and have a single point of access?

Your Answer: Singleton

Correct Answer: Singleton

Result: Correct

5. Question: A class FileProcessor has methods for reading a file, processing its contents, and saving the results to a database. Which design principle is being violated?

Your Answer: Single Responsibility Principle

Correct Answer: Single Responsibility Principle

Result: Correct

6. Question: Which design pattern is used to encapsulate a family of algorithms, each of which can be interchanged to solve the same problem?

Your Answer: Factory Method

Correct Answer: Strategy

Result: Incorrect

7. Question: In a system, a Logger class uses a concrete FileLogger class directly. To allow for DatabaseLogger or CloudLogger, you should change the dependency to an ILogger interface. Which SOLID principle is this an example of?

Your Answer: Dependency Inversion Principle

Correct Answer: Dependency Inversion Principle

Result: Correct

8. Question: Which of the following best describes the purpose of the Factory Method design pattern?

Your Answer: To define an interface for creating an object, but let subclasses decide which class to instantiate.

Correct Answer: To define an interface for creating an object, but let subclasses decide which class to instantiate.

Result: Correct

9. Question: You have a large IPayment interface with a dozen methods for all types of payment processing. A new client only needs to call a single processPayment method. Which design principle is being violated?

Your Answer: Interface Segregation Principle

Correct Answer: Interface Segregation Principle

Result: Correct

10. Question: You want to create a Computer object with various optional components (e.g., a graphics card, extra RAM, a specific type of keyboard). The final product can be very different based on user choice. Which creational design pattern would be most suitable?

Your Answer: Builder

Correct Answer: Builder

Result: Correct

**LLD & Design Patterns Mock Test**<br><br>
**Questions & Answers**
**Score: 8/10**<br><br>
1. Question: Which OOP concept is violated when a subclass cannot be substituted for its base class without altering the correctness of the program?

Your Answer: Liskov Substitution Principle

Correct Answer: Liskov Substitution Principle

Result: Correct

2. Question: A class has multiple methods that are each responsible for a single, distinct task. A change to one method does not require changing any other method in the class. Which principle does this adhere to?

Your Answer: Single Responsibility Principle

Correct Answer: Single Responsibility Principle

Result: Correct

3. Question: You have a ReportGenerator class that directly creates an instance of a PDFPrinter class. When you need to support HTMLPrinter, you have to modify the ReportGenerator class. Which SOLID principle is being violated?

Your Answer: Open/Closed Principle (OCP)

Correct Answer: Open/Closed Principle (OCP)

Result: Correct

4. Question: Which creational design pattern is used to create a complex object step by step, allowing you to produce different types and representations of an object using the same construction process?

Your Answer: Builder

Correct Answer: Builder

Result: Correct

5. Question: In a software system, a high-level module depends on an abstraction (an interface), and a low-level module also depends on that same abstraction. Which design principle does this describe?

Your Answer: Dependency Inversion Principle

Correct Answer: Dependency Inversion Principle

Result: Correct

6. Question: Which creational design pattern defines an interface for creating an object, but lets the subclasses decide which class to instantiate?

Your Answer: Factory Method

Correct Answer: Factory Method

Result: Correct

7. Question: You have a single Payment interface with methods for payByCreditCard(), payByPayPal(), and payByCrypto(). A new client only needs to use payByCreditCard(). Which SOLID principle is being violated?

Your Answer: Interface Segregation Principle

Correct Answer: Interface Segregation Principle

Result: Correct

8. Question: In Object-Oriented Programming, the ability of an object to take on many forms is known as:

Your Answer: Polymorphism

Correct Answer: Polymorphism

Result: Correct

9. Question: Which creational design pattern ensures a class has only one instance and provides a global point of access to that instance?

Your Answer: Singleton

Correct Answer: Singleton

Result: Correct

10. Question: Which of the following best describes the purpose of Low-Level Design (LLD)?

Your Answer: To create a detailed implementation plan for individual components.

Correct Answer: To create a detailed implementation plan for individual components.

Result: Correct