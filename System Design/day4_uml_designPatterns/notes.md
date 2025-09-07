**UML**
* At first we shouldn't write any code. It's not preferable. Building class diagrams is advisable. 
__Class Notation:__
    __Class Representation__
        __Class Name:__ (Top)
        __Attributes:__ (Middle)
        __Operations:__ (Bottom)    
        __Figure:__<br>
        ![Fig 1](image-1.png)
    __Visibility Markers:__
        Public +
        Private -
        Protected #
        Package ~
    __Attribute & Method Syntax:__
        __Attribute:__ visibility name: Type [multiplicity] = DefaultValue (Ex: + age: int = 21)
        __Method:__ visibility name(parameterName1: Type1,...): ReturnType (Ex: - isAdult(age:int): boolean)
        __Interface Representation:__
        // Interface for classes that can calculate pay
        public interface Payable {
            
            // Method to calculate pay
            double calculatePay();
        }
                        |
                        |
                        |
                        V
        ![Interface Rep](image-4.png)

      __Abstract Class Representation:__

        // Abstract class representing an Animal
        public abstract class Animal {

            // Abstract method to make sound
            public abstract void makeSound();
        }
                        |
                        |
                        |
                        V
            ![Abs Class Rep](image-2.png)
        
        * Abstract class is denoted in italic foramt



