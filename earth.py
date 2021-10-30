import numpy as np

def add_drop(Original, Add, Delete):
    List = np.append(Original,Add)
    for num in Delete:
        List = np.delete(List, np.argwhere(List == num))
    List = np.unique(List)
    List = sorted(List, key=len, reverse=True)
    for i in range(len(List)-1):
        d1 = List[i]
        d2 = List[i+1]
        if len(d1) == len(d2):
            if List[i+1] > List[i]:
                List[i] = d2
                List[i+1] = d1
    return List


if __name__ == "__main__":
    dict = {
    "Original": ["one", "two", "three"],
    "Add": ["one", "two", "five", "six"],
    "Delete": ["two", "five"]}
    Result = ["three", "six", "one"]

    Output = add_drop(**dict)
    assert Result == Output

