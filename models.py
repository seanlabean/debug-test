class BaseProcessor:
    def __init__(self, name):
        self.name = name
        self.execution_count = 0

    def process(self, data):
        # Good spot to show "Step Into" from the child class
        self.execution_count += 1
        return f"Processed {data} via {self.name}"

    def __repr__(self):
        return f"Processor({self.name})"

class DataEnricher(BaseProcessor):
    def process(self, data):
        # Add a breakpoint here to show the Call Stack (DataEnricher -> BaseProcessor)
        result = super().process(data)
        return f"{result} + Enriched ✨"