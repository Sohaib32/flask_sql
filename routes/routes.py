# routes.py
from flask import request, jsonify, Blueprint
from models.models import db, Doc

routes_app = Blueprint('routes', __name__)

# Create doc
@routes_app.route('/doc', methods=['POST'])
def create_doc():
    path = request.args.get('path')
    file = request.args.get('file')
    created_by = request.args.get('created_by')

    if path and file and created_by:
        doc = Doc(path=path, file=file, created_by=created_by)
        db.session.add(doc)
        db.session.commit()
        return jsonify({'message': 'Doc created successfully'})
    else:
        return jsonify({'message': 'Incomplete data provided'}, 400)

# Retrieve a doc by ID
@routes_app.route('/doc/<int:doc_id>', methods=['GET'])
def get_doc(doc_id):
    doc = Doc.query.get(doc_id)
    if doc:
        return jsonify({
            'id': doc.id,
            'path': doc.path,
            'file': doc.file,
            'created_at': doc.created_at,
            'updated_at': doc.updated_at,
            'created_by': doc.created_by
        })
    else:
        return jsonify({'message': 'Doc not found'}, 404)

# Update a doc by ID using query parameters
@routes_app.route('/doc/<int:doc_id>', methods=['PUT'])
def update_doc(doc_id):
    doc = Doc.query.get(doc_id)
    if doc:
        path = request.args.get('path', doc.path)
        file = request.args.get('file', doc.file)
        created_by = request.args.get('created_by', doc.created_by)

        doc.path = path
        doc.file = file
        doc.created_by = created_by

        db.session.commit()
        return jsonify({'message': 'Doc updated successfully'})
    else:
        return jsonify({'message': 'Doc not found'}, 404)

# Delete a doc by ID
@routes_app.route('/doc/<int:doc_id>', methods=['DELETE'])
def delete_doc(doc_id):
    doc = Doc.query.get(doc_id)
    if doc:
        db.session.delete(doc)
        db.session.commit()
        return jsonify({'message': 'Doc deleted successfully'})
    else:
        return jsonify({'message': 'Doc not found'}, 404)
