import dendropy
from dendropy import Tree, TaxonNamespace
from dendropy.calculate import treecompare


# From a string
s1 = "[&R] (E, ((A, B),(C, D)));"
s2 = "[&R] (B, ((A, E),(C, D)));"

tns = dendropy.TaxonNamespace()
t1 = Tree.get(data=s1, schema="newick", taxon_namespace=tns)
t2 = Tree.get(data=s2, schema="newick", taxon_namespace=tns)

t1.encode_bipartitions()
t2.encode_bipartitions()
#print(treecompare.euclidean_distance(t1, t2))
print(treecompare.false_positives_and_negatives(t1, t2, False))
#Unweighted RF
print(treecompare.symmetric_difference(t1, t2, False))

print(t1)
t1.print_plot()
print(t2)
t2.print_plot()

