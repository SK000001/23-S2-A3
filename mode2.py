from island import Island

class Mode2Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, n_pirates: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.n_pirates = n_pirates

    def add_islands(self, islands: list[Island]):
        """
        Student-TODO: Best/Worst Case
        """
        raise NotImplementedError()

    def simulate_day(self, crew: int) -> list[tuple[Island|None, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        raise NotImplementedError()

if __name__ == "__main__":
        a = Island("A", 400, 100)
        b = Island("B", 300, 150)
        c = Island("C", 100, 5)
        d = Island("D", 350, 90)
        e = Island("E", 300, 100)
        islands = [
            a, b, c, d, e
        ]