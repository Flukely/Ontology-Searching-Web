import rdflib

# โหลดไฟล์ RDF (Ontology)
graph = rdflib.Graph()
graph.parse("mytourism.owl", format="xml")

# ดึงข้อมูลทั้งหมดจาก RDF graph
triples = list(graph)

# แสดงจำนวนข้อมูลที่โหลด
print(f"📊 จำนวนข้อมูลที่โหลดได้: {len(triples)} triples")

# แสดงข้อมูลที่ได้จาก triples
for triple in triples:
    print(f"{triple[0]} {triple[1]} {triple[2]}")
