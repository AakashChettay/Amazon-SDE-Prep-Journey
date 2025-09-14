MAANG-Style Creational Patterns Quiz Analysis
Date: September 14, 2025
Score: 3/5

Questions & Correct Answers
1. Question: A global configuration manager for an application needs to be initialized only once, and that single instance must be easily accessible from any part of the codebase. It also needs to be thread-safe to avoid race conditions during its initialization in a multi-threaded environment. Which creational pattern is the best fit, and what is a common implementation detail to ensure thread-safety?

Correct Answer: Singleton; use Double-Checked Locking with a volatile variable.✅

2. Question: You are building a game that has a variety of enemies (e.g., Orc, Goblin, Troll). Each enemy type has a base health, speed, and attack power, but they can be customized with different armor and weapons. Creating each enemy object is computationally expensive. When a player needs to spawn 100 goblins with different armor, which creational pattern should you use for efficiency?

Correct Answer: Prototype✅

3. Question: An e-commerce platform needs to support multiple payment gateways (e.g., PayPal, Stripe, Visa). The specific payment gateway to use is determined at runtime based on the user's country or a configuration setting. A PaymentProcessor class should be able to work with any payment gateway without needing to know its concrete type. Which creational pattern would best solve this problem by decoupling the client from concrete payment gateways?

My Answer: Abstract Factory Method ❌
Correct Answer: Factory Method 

4. Question: A software suite for architects needs to support different rendering engines (e.g., OpenGL, DirectX, Vulkan) for different project types. The application should be able to create an entire suite of related rendering objects (e.g., a Renderer, a Shader, and a TextureLoader) for a chosen engine without needing to know the engine's concrete implementation details. Which creational pattern is the most robust solution for this?

My Answer: Factory Method ❌
Correct Answer: Abstract Factory

5. Question: You are designing an order system for a restaurant. A user can build a custom Pizza object by selecting a base crust, adding toppings, and choosing a sauce. The order of these selections can vary, and some ingredients might be optional. Which creational design pattern would allow you to create different kinds of pizzas with the same construction process, while also providing a simple API for the user?

Correct Answer: Builder ✅