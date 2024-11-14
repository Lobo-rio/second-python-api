from flask import Flask, jsonify, request
from flask_restx import Api, Resource

from server.instance import server, db
from server.models.books import model_books
from server.sqlite import Books

app, api = server.app, server.api

booksNS = api.namespace('books', description='Books operations')

@booksNS.route('/', endpoint='Books')
class BookList(Resource):
    @booksNS.doc('list_books')
    @booksNS.marshal_list_with(model_books)
    def get(self):
        books = Books.query.all()
    
        return [book.to_dict() for book in books]
    
    @booksNS.doc('create_book')
    @booksNS.expect(model_books)
    @booksNS.marshal_list_with(model_books)
    def post(self):
        title = request.json['title']
        author = request.json['author']
        description = request.json['description']

        book_existed = Books.query.filter_by(title = title).first()
        if book_existed:
            return jsonify({'error': 'Book already exists!'}), 400
    
        book = Books(title=title, author=author, description=description)
        db.session.add(book)
        db.session.commit()

        return book.to_dict(), 201
    
@booksNS.route('/<int:id>')
@booksNS.response(404, 'Book not found')
@booksNS.param('id', 'The book identifier')
class Book(Resource):
    @booksNS.doc('get_book')
    @booksNS.marshal_with(model_books)
    def get(self, id):
        book_existed = Books.query.get(id)
        if not book_existed:
            return jsonify({'error': 'Book does not exist!'}), 404
    
        return book_existed.to_dict(), 200

    @booksNS.doc('delete_book')
    @booksNS.response(204, 'Book deleted')
    def delete(self, id):
        book_existed = Books.query.get(id)
        if not book_existed:
            return jsonify({'error': 'Book does not exist!'}), 404
    
        db.session.delete(book_existed)
        db.session.commit()

        return '', 204

    @booksNS.doc('update_book')
    @booksNS.expect(model_books)
    @booksNS.marshal_with(model_books)
    def put(self, id):
        book_existed = Books.query.get(id)
        if not book_existed:
            return jsonify({'error': 'Book does not exist!'}), 404
    
        book_existed.title = request.json['title']
        book_existed.author = request.json['author']
        book_existed.description = request.json['description']
        db.session.commit()

        return book_existed.to_dict(), 200