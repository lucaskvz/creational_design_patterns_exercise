
class GlobalBudget:
    """
    One shared marketing budget across the system.
    """
    _instance = None

    def __new__(cls, initial_amount: float = 0.0):
      # TODO: Singleton pattern implementation
      pass

    def allocate(self, amount: float) -> None:
      # TODO: Allocate amount from the budget
      pass

    def remaining(self) -> float:
        return self._balance

    def __repr__(self) -> str:
        return f"<GlobalBudget remaining={self._balance}>"
