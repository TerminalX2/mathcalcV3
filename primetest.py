import time

def division(p: int) -> bool:
  if p <= 1:
    return False 
  elif p <= 3:
    return True
  elif p % 2 == 0 or p % 3 == 0:
    return False
    
  limit = int(p**0.5) + 1
  for i in range(5, limit, 6):
    if p % i == 0 or p % (i + 2) == 0:
      return False
  return True

while True:
  print("------------------------------------------")
  print("|          zTerminal : PrimeTest         |")
  print("------------------------------------------")
  print()

  print("Input an integer to be tested.")
  print()

  p = input(">>> ")

  if p.lower() == 'exit':
    break

  try:
    p = int(p)
    start_time = time.time()
    print()

    if division(p):
      print(f"{p} is prime.")
    else:
      print(f"{p} is not prime.")

    end_time = time.time()
    elapsed = end_time - start_time
    print(f"({elapsed:.8f} seconds)")
    print()

  except ValueError:
    print(f"{p} is an invalid input. Enter an integer.")
