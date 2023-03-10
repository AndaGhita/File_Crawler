import os

def index_directory(directory):
    index = {}
    for item in os.listdir(directory):
        item_path = os.path.join(directory,item)
        if os.path.isfile(item_path):
            try:
                with open(item_path, 'r', encoding='utf-8') as f:
                    words = f.read().split()
                    for word in words:
                        if word in index:
                            index[word].append(item_path)
                        else:
                            index[word] = [item_path]
            except:
                print(f"Could not read file: {item_path}")
        elif os.path.isdir(item_path):
            sub_index = index_directory(item_path)
            for word in sub_index:
                if word in index:
                    index[word] += sub_index[word]
                else:
                    index[word] = sub_index[word]
    return index

def search_index(keyword, index):
    if keyword in index:
        for filepath in index[keyword]:
            print(filepath)
    else:
        print("Keyword not found in any file.")

if __name__ == "__main__":
    print("Enter a search term:")
    keyword = input()
    current_directory = os.getcwd()
    index = index_directory(current_directory)
    search_index(keyword, index)
