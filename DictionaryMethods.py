marks={1:[1,2,3,4,5,6,7],
2:[1,2,3,4,5,6,7],
3:[1,2,3,4,5,6,7],
"Names":{"Sriram","Rajesh","Sai"}}
print(marks.items())
marks.update({"age":23})
print(marks)
print(marks.get("no"))#Throws none when doesn't find the required key value
print(marks["no"])#Throws error when doesn't find the required key value
 