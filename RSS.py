#1. Export "Exported Items.ris" from Zotero to a directory
#2. Run "python RSS.py" in that directory
#3. Examine journals.log
#4. Find up to 20 rss feed of the most relevant journals and combine them at rssunify.com
#5. Filter the combined feed with regex or by a keyword at siftrss.com
#6. Start reading the refined feed in the UT cloud RSS reader or Zotero


f = open("Exported Items.ris").readlines()
results={}
for line in f:
  if len(line.split())>0 and line.split()[0]=="T2":
    name=" ".join(line.split()[2:])
    if name in results:
      results[name]+=1
    else:
      results[name]=1

f=open("journals.log","w")
for result in results:
  f.write("%s %d\n"%(result,results[result]))

#checksum=0
#for result in results:
#  checksum+=results[result]

