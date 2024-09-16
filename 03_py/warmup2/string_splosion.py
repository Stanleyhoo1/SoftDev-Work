def string_splosion(str):
  new_str = ""
  for i in range(len(str)):
    new_str += str[0:i+1]
  return new_str

