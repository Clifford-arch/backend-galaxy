#import the requirements
from flask import Flask, jsonify, request

# creates the Flask instance.
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Book API"

# Sample data
books = [
    {"id": 1, "title": "Concept of Physics", "author": "H.C Verma"},
    {"id": 2, "title": "Gunahon ka Devta", "author": "Dharamvir Bharti"},
    {"id": 3, "title": "Problems in General Physsics", "author": "I.E Irodov"}
]

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Get a single book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    return jsonify(book) if book else (jsonify({"error": "Book not found"}), 404)

# Get book by name
@app.route('/books/title/<string:title>', methods=['GET'])
def get_book_by_title(title):
    data = next((book for book in books if book["title"].lower() == title.lower()), None)
    if not data:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(data), 200

#get book by id using POST method
@app.route('/book',methods=['POST'])
def get_by_post():
    data = request.get_json()  
    book_id = data.get('id')

    data1 = next((book for book in books if book["id"] == book_id), None)
    if not data1:
        return jsonify({"error": "Book not found"}), 404

    return jsonify(data1), 200


#Only run the server if this file is being executed directly
if __name__ == '__main__':
    app.run(debug=True)