from functions.read_file import read_file

if __name__ == "__main__":

    lines_of_interest = read_file(
        file_path="./data/DailyDelhiClimateTrain.csv",
        skip=10,
        limit=10
    )

    final_result = list()

    for line in lines_of_interest:
        final_result.append(line)

    print(final_result)
