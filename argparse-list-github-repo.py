import requests
import argparse


def main():
    parser = argparse.ArgumentParser(description="List Github repositories")
    parser.add_argument("-n", "--name", required=True, help="name of the user")
    args = vars(parser.parse_args())
    username = args["name"]
    res = requests.get("https://api.github.com/users/" + username + "/repos")
    json = res.json()
    for i in range(0, len(json)):
        print("Project Number: ", i + 1)
        print("Project Name: ", json[i]["name"])


if __name__ == "__main__":
    main()
