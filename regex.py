import re

str_list = [
    "This is a technical test for applying to backend position. The solution must be developed in Java and published to a GitHub repository",
    "What data structures and algorithms can be used for storing and filtering by pattern (or regex) a set of strings? Write the code using Java 8 functions and Stream API",
    "Write a function that returns the count of distinct case-insensitive alphabetic characters and numeric digits occurring more than once in an input string. Example",
    "Given the entity relationship diagram below, code SQL sentences for",
    "Get all buses for 'Concessionaire 1'",
    "Get all NVR devices for buses with type equal to 'Bi-articulado'",
    "Summarize the quantity of devices by status (Active / Inactive) and bus motor(Diesel / Gas / Electric / Hybrid)",
    "Design and code an API REST for accessing the resources in the above database",
    "What HTTP endpoints and methods would you enable for creation, reading, modification and deletion?",
    "hooHow can be a hierarchical access to enable the front-end for querying devices belonging to a specific bus?o",
    "hTest the API REST and attach the evidence. Postman is suggested.ooo"]

# Search uppercase words
regex = r"\s([A-Z]*)\s"

def run(str_list=str_list, regex=regex ):

    r = re.compile(regex)
    filter_list = list(filter(r.search, str_list))
    print(filter_list)


if __name__ == "__main__":
    run()