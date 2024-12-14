## Design Patterns and Their Relation to SOLID Principles

### **1. Factory Method Pattern**

#### **Description**
The Factory Method Pattern abstracts the process of object creation. Instead of instantiating objects directly, a factory class is responsible for creating specific objects (e.g., different pizza types).

#### **Relation to SOLID Principles**
- **Single Responsibility Principle (SRP):**
  The Factory class handles only object creation. This ensures that other parts of the system remain focused on their specific tasks.

- **Open-Closed Principle (OCP):**
  New pizza types can be added without modifying the existing factory logic. Developers simply extend the factory by introducing new pizza subclasses.

- **Abstraction:**
  The client interacts with an abstract `Pizza` interface, not the concrete classes. This improves code maintainability and flexibility.

---

### **2. Decorator Pattern**

#### **Description**
The Decorator Pattern allows the dynamic addition of responsibilities (e.g., toppings) to an object at runtime without modifying its structure. Each topping extends the pizza's functionality while adhering to a common interface.

#### **Relation to SOLID Principles**
- **Single Responsibility Principle (SRP):**
  Each topping class is responsible for its specific behavior, such as adding cost and description.

- **Open-Closed Principle (OCP):**
  Toppings can be added or removed without altering existing pizza classes. The system is extensible for new toppings.

---

### **3. Singleton Pattern**

#### **Description**
The Singleton Pattern ensures that only one instance of a class (e.g., `InventoryManager`) exists in the system, providing a global point of access to shared resources.

#### **Relation to SOLID Principles**
- **Single Responsibility Principle (SRP):**
  The `InventoryManager` handles only inventory-related tasks, centralizing inventory management in a single location.

- **Encapsulation:**
  The inventory logic is hidden within the Singleton class, ensuring consistent state management across the application.

---

### **4. Strategy Pattern**

#### **Description**
The Strategy Pattern allows the dynamic selection of algorithms (e.g., payment methods) at runtime. Each payment method is implemented as a separate strategy class.

#### **Relation to SOLID Principles**
- **Open-Closed Principle (OCP):**
  New payment methods can be added without altering existing code. Each payment method implements the common `PaymentMethod` interface.

- **Encapsulation:**
  Payment logic is abstracted from the main application, making it easier to manage and extend.

---

### Conclusion
The design patterns applied in this project align strongly with the SOLID principles, improving the modularity, flexibility, and maintainability of the codebase.

