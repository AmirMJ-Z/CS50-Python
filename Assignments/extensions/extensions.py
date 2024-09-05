s = input('File name: ')
s = s.strip()
s = s.lower()
extension = s.split(".")[-1]

if extension == 'gif' or extension == 'png':
    print(f'image/{extension}')

elif extension == 'jpg' or extension == 'jpeg':
    print('image/jpeg')

elif extension == 'txt':
    print('text/plain')

elif extension == 'zip' or extension == 'pdf':
    print(f'application/{extension}')

else:
    print('application/octet-stream')

