import os

def index_directory(directory):
    index = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    words = f.read().split()
                    for word in words:
                        if word in index:
                            index[word].append(filepath)
                        else:
                            index[word] = [filepath]
            except:
                print(f"Could not read file: {filepath}")
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
