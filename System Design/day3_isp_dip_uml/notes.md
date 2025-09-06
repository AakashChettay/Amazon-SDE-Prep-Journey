4. **Interface Segeration Principle(ISP)**
    __Defination:__ Clients should not be forced to implement the interfaces they didn't use.
    __Dont's:__
    * Don't create large and bloated interfaces.
    __Do's:__
    * Break them into smaller and specific one's.
    __Benefits:__
    * Modularity & flexibility.
    * Imporves testability.
    * Prevents accedental implementation of irrevelent methods
    * Makes code easier to unnderstand.
    __When to apply ISP?__
    * When your interface is doing to many things. 
        -> Before applying ISP -> After applying ISP
        -> interface **x** -> interface **x**, interface **y**
        -> A implements x -> A implements **x, y**
    * When some classes implementing interfaces throwing errors.

5. **Dependency Inversion Principle(DIP)**
    __Defination:__ High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.
    __Benefits:__
    * Flexibility: Easily swap out implementations without modifying high-level code.
    * Testability: You can mock or stub the abstractions during testing.
    * Reusability: Code becomes reusable since it's not tightly bound to one specific implementation.
    * Maintainability: Makes it easier to change one part of the system without affecting others.
    * Scalability: You can scale or upgrade parts of your codebase     without a massive rewrite.
