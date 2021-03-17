import networkx as nx


def main():
    f = "input2.txt"
    rows = 6
    cols = 7
    board = []
    graph = nx.Graph

    with open(f, 'r') as file:
        for _ in range(rows):
            row = file.readline()
            board.append([char for char in row.strip()])
        next_player = file.readline().strip()


if __name__ == "__main__":
    main()
