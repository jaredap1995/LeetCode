def StockPicker(arr):
  if len(arr) <= 1: 
    return -1

  possibles = []
  for i in range(len(arr)):
    sell_day = max(arr[i:])
    val = sell_day - arr[i]

  sol = max(possibles)
  return sol if sol > 0 else -1

# keep this function call here 
print(StockPicker(input()))