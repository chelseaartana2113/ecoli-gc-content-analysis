with open ("C:\\Users\\Thinkpad\\Downloads\\genome_ecoli.txt") as f:
    genome=f.read()
genome=genome.upper()
total=len(genome)
print('Genome length:', total)
window=5000
step=500
import matplotlib.pyplot as plt
positions=[]
GC_values=[]
for c in range(0,len(genome)- window + 1, step):
    segment=genome[c:c+window]
    G= segment.count('G')
    C=segment.count('C')
    GC_content=((G+C)/len(segment))*100
    positions.append(c)
    GC_values.append(GC_content)
print("Total windows analyzed:", len(GC_values))
average_GC= sum(GC_values)/len(GC_values)
print('Average GC Content:', round(average_GC,2), '%')
min_GC= min(GC_values)
max_GC= max(GC_values)
print("Minimum GC:", min_GC,'%')
print("Maximum Gc:", max_GC,'%')
plt.figure(figsize=(12,12))
#plot 1
plt.subplot(3,1,1)
plt.plot(positions, GC_values)
plt.xlabel('Genome Position(bp)')
plt.ylabel('Gc content (%)')
plt.title('GC Content Across Genome E.Coli')
#plot 2
plt.subplot(3,1,2)
plt.hist(GC_values, bins=50)
plt.xlabel('GC Content (%)')
plt.ylabel('Frequency')
plt.title('GC Content Distribution Across Genome E.Coli')
#plot 3
plt.subplot(3,1,3)
plt.scatter(positions, GC_values, s=1)
plt.title('GC Content Scatter')
plt. xlabel('Genome position')
plt.ylabel('GC content(%)')
plt.axhline(average_GC, color='red', linestyle='--' )
plt.tight_layout()
plt.subplots_adjust(hspace=0.5)
plt.savefig("gc_analysis.png", dpi=300)
plt.show()