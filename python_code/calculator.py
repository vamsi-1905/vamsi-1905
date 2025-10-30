from mesa import Agent, Model

class CalculatorAgent(Agent):
    def __init__(self, unique_id, model, a, b):
        super().__init__(unique_id, model)
        self.a = a
        self.b = b

    def step(self):
        pass

class AddAgent(CalculatorAgent):
    def step(self):
        result = self.a + self.b
        print(f"[AddAgent-{self.unique_id}] {self.a} + {self.b} = {result}")

class SubAgent(CalculatorAgent):
    def step(self):
        result = self.a - self.b
        print(f"[SubAgent-{self.unique_id}] {self.a} - {self.b} = {result}")

class MulAgent(CalculatorAgent):
    def step(self):
        result = self.a * self.b
        print(f"[MulAgent-{self.unique_id}] {self.a} * {self.b} = {result}")

class DivAgent(CalculatorAgent):
    def step(self):
        if self.b != 0:
            result = self.a / self.b
            print(f"[DivAgent-{self.unique_id}] {self.a} / {self.b} = {result:.2f}")
      
class CalculatorModel(Model):
    def __init__(self, a, b, operations):
        super().__init__()
        self.schedule = []
        self.agent_classes = {
            1: AddAgent,
            2: SubAgent,
            3: MulAgent,
            4: DivAgent
        }
        self._create_agents(a, b, operations)

    def _create_agents(self, a, b, operations):
        for idx, op in enumerate(operations):
            cls = self.agent_classes[op]
            agent = cls(idx, self, a, b)
            self.schedule.append(agent)

    def step(self):
        for agent in self.schedule:
            agent.step()

def get_user_input():
    print("=== Mesa Calculator Agent Model ===")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Select operations to run (separate choices with commas):")
    print("  1. Addition")
    print("  2. Subtraction")
    print("  3. Multiplication")
    print("  4. Division")
    print("  5. All operations")
    choices = input("Your choice(s): ")

    if "5" in choices:
        operations = [1, 2, 3, 4]


    return a, b, operations

def main():
    a, b, operations = get_user_input()
    model = CalculatorModel(a, b, operations)
    model.step()

if __name__ == "__main__":
    main()
