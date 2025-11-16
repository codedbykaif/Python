marks = {
  "kaif": 100, 
  "prashant": 89,
  "devansh": 84
}
print(marks, type(marks))
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"kaif": 99, "dreamer": 100})
print(marks)
print(marks.get("kaif2")) #if the element is not present in dictionary this function returns none instead of key error

print(marks["kaif"])   #if the element is not present in the dictionary it returns keyerror

