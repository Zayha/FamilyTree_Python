from presenter.presenter import Presenter
from view.console import Console


def main():
    p1 = Presenter()
    c1 = Console(p1)
    c1.start()


if __name__ == "__main__":
    main()
