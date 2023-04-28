import csv

header = ['videoid']


with open('newone.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)
    file1 = open('/Users/akash/Desktop/nlp/segments', 'r')
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        line = str(line)
        videoid = line[:11]
        data = [videoid]
        writer.writerow(data)

    file1.close()

    # write the data





