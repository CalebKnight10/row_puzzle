def row_puzzle(row, token=0):
    max_length = len(row)
#Check if the given token is bigger than the length
if row[token] >= max_length:
    return False
#Check if the token is the length of the row
if row[token] == max_length:
  print(row[token])
  print(max_length)
  return True
#Check if the token will exceed the length
if max_length - row[token] == 1:
    return True
#Check if the length of the row is 0, if so False
if max_length == 0:
    return False
    if row[token] == 0:
        max_length = row[1: max_length:]
    else:
        print("row token:" + str(row[token]))
        print("row length:" + str(max_length))
  #Create an array adding the tokens that have been checked
  new_row = row[row[token]: max_length:]
  max_length = len(row)
        #print(new_row)
    #return row_puzzle(new_row, token)

    row_puzzle([2, 3, 4, 1, 3, 4, 0])
    print( )
    row_puzzle([2, 4, 5, 3, 1, 3, 1, 4, 0])
    print()
    row_puzzle([3, 4, 1, 1, 0])
    print()
