#[1,1,2,2,4]-> [1,2,4]
def remove_duplicates(some_list):
    without_dupliates=[]
    for element in some_list:
        if element not in without_dupliates:
            without_dupliates.append(element)
    return without_dupliates

def  remove_duplicates_sets(some_list):
    return list(set(some_list))
def run():
    random_list=[1,1,2,2,4]
    #print(remove_duplicates(random_list))
    print(remove_duplicates_sets(random_list))

if __name__ == "__main__":
    run()