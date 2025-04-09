class Line:
    start: Point
    end: Point

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def __str__(self) -> str:
        """Magic method to print string representation of Line object"""
        return f"Line from {self.start} to {self.end}"

    def get_length(self) -> float:
        x_diffs: float = self.end.x - self.start.x
        y_diffs: float = self.end.y - self.start.y
        return (x_diffs**2 + y_diffs**2) ** 0.5

    def get_slope(self) -> float:
        x_diffs: float = self.end.x - self.start.x
        y_diffs: float = self.end.y - self.start.y

        return y_diffs / x_diffs
