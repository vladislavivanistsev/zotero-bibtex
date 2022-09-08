# Create a dictionary
results={}

# Parse the given ris file to count Journals
file = open("Exported Items.ris", "r")
for line in file.readlines():
    if len(line.split())>0 and line.split()[0]=="T2":
        name = " ".join(line.split()[2:])
        if name in results:
            results[name]+=1
        else:
            results[name]=1
file.close()

# Write log file with sorted journal names
results = dict(sorted(results.items(), key=lambda result: result[0]))
out = open("journals-names.log","w")
for result in results:
     out.write("{0} {1}\n".format(results[result],result))
out.close

# Write log file with sorted journal names
results = dict(sorted(results.items(), key=lambda result: result[1]), reverse=True)
out = open("journals-counts.log","w")
for result in results:
     out.write("{0} {1}\n".format(results[result],result))
out.close
