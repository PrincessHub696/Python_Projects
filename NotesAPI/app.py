from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

notes = []

@app.route("/api/notes", methods=["GET"])
def get_notes():
    return jsonify(notes)

@app.route("/api/notes", methods=["POST"])
def add_note():
    data = request.json
    note = {
        "id": len(notes) + 1,
        "title": data["title"],
        "text": data["text"]
    }
    notes.append(note)
    return jsonify(note), 201

@app.route("/api/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    global notes
    notes = [n for n in notes if n["id"] != note_id]
    return jsonify({"status": "deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)