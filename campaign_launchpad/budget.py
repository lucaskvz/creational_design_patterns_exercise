class GlobalBudget:
    """
    One shared marketing budget across the system.
    """
    # I keep a single class-level reference to enforce the singleton.
    _instance = None 

    def __new__(cls, initial_amount: float = 0.0):
        # I implement the singleton in __new__: I create the instance once and reuse it thereafter.
        if cls._instance is None:
            inst = super().__new__(cls)
            # I set the starting balance only on first creation.
            inst._balance = float(initial_amount)  
            cls._instance = inst
        # I always return the same instance.
        return cls._instance  

    def allocate(self, amount: float) -> None:
        # I reject non-positive allocations to prevent invalid operations.
        if amount <= 0:
            raise ValueError("Allocation amount must be positive.")
        # I ensure the balance never goes below zero.
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        # I deduct the allocation from the shared balance.
        self._balance -= amount

    def remaining(self) -> float:
        # I report the current shared balance.
        return self._balance

    def __repr__(self) -> str:
        # I provide a concise debug representation showing the remaining funds.
        return f"<GlobalBudget remaining={self._balance}>"