import analyze_data
import request_data


def main():
    request_data.request_tournaments()
    print("Obtained the tournaments!")
    request_data.request_matches()
    print("Obtained the matches!")
    analyze_data.analyze_matches()
    print("Analyzed the mathces!")
    analyze_data.draw_graphs()


if __name__ == '__main__':
    main()
