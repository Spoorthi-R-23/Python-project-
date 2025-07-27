from difflib import SequenceMatcher

with open('Demo1.txt')as one_file, open('Demo2.txt')as two_file:
    data1=one_file.read()
    data2=two_file.read()
    matches=SequenceMatcher(None,data1,data2).ratio()
    print(f"The plagiarized content is : {matches}%")