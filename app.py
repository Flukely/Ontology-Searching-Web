from flask import Flask, render_template, request, jsonify
import rdflib

app = Flask(__name__)

# โหลดไฟล์ RDF (Ontology)
graph = rdflib.Graph()
graph.parse("mytourism.owl", format="xml")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    
    # สร้างการค้นหาจาก RDF Graph
    result = []
    for subj, pred, obj in graph:
        # เปรียบเทียบการค้นหากับข้อมูลใน triple
        if query in str(subj).lower() or query in str(pred).lower() or query in str(obj).lower():
            result.append([str(subj), str(pred), str(obj)])

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
