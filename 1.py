text = open("1.txt", "r")
topsum = 0
int_sum = 0
for line in text:
    if (line == "\n"):
        if (topsum < int_sum):
            topsum = int_sum
            int_sum = 0
    int_sum += int(line) 
    
print(topsum)