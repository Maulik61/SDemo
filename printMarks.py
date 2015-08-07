print "Enter Subject number"
sub= int(raw_input("Enter :"))
local_Data = []
for i in range(0,int(sub)):
    subject=raw_input("Enter Subject Name: ")
    marks=int(raw_input("Enter Marks: "))
    local_dir={subject:marks}
    local_Data.append(local_dir)
print local_Data
