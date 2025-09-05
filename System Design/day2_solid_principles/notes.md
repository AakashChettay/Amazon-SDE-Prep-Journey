1. **Single Responsibility Principe(SRP)**
    __Defination:__ A class should have only one responsibilty to change.
    __Benefits:__
    * Improved Maintainability
    * Better test coverage
    * Easy debugging
    * Good Readability
    * Lower Risk in changes
    __Common mistakes when violating SRP:__
    * Putting DB logic and bussiness logic together
    * UI code coupled with logic
    __Is SRP just for classes?__
    The answer is __no__. SRP can be applied to methods, modules, microservices and even entire systems. The key is to ensure that each component has a single responsibility and that changes in one area do not affect others unnecessarily.
    Hence, SRP is not just for classes. It's a mindset you can apply from the smallest method to the largest system design.

2. **Open/Closed Principle(OCP)** 
    __Defination:__ Software entities should be open for extension, but closed for modification.
    __When should apply OCP:__
    * When bussiness rules are likely to change as expand.
    * When you are building a plugin system.
    * When your codebase is becoming God Class with lots of conditionals.