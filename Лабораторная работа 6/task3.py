def to_csv_file(filename='', headers=[], rows=[], delimiter=',', new_line='\n'):
    with open(filename, 'w+') as f:
        writer = csv.writer(f)
        writer.writerow(headers, delimiter=',')

    for i in rows:
        with open(filename, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(i, new_line='\n')
return f