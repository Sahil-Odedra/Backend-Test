from flask import Flask, jsonify,request
from flasgger import Swagger
from models import All_Movies,Add_To_List,search,delete,update

app=Flask(__name__)
swagger=Swagger(app)

@app.route('/movies',methods=['POST'])
def add_movie():
    """
    New movie
    ---
    tags:
        - Movies
    parameters:
        - in: body
          name: body
          required: true
          schema:
            type: object
            properties:
                title: 
                    type: string
                director:
                    type: string
                genre:
                    type: string
                year:
                    type: integer
                rating:
                    type: number
    responses:
        default:
            description: Movie added
    """
    movie=Add_To_List(request.json)
    return jsonify(movie)


@app.route('/movies',methods=['GET'])
def all_movies():
    """
    All movies
    ---
    tags:
        - Movies
    responses:
        default:
            description: all movies
    """
    return jsonify(All_Movies())


@app.route('/movies/<id>',methods=['GET'])
def search_movie(id):
    """
    Search movie
    ---
    tags:
        - Movies
    parameters:
        - in: path
          name: id
          required: true
          type: string
    responses:
        default:
            description: Movie found
    """
    movie=search(id)
    if movie:
        return jsonify(movie)
    else:
        return jsonify({'message':'Movie not found'})
    

@app.route('/movies/<id>',methods=['DELETE'])
def delete_movie(id):
    """
    Delete
    ---
    tags:
        - Movies
    parameters:
        - in: path
          name: id
          required: true
          type: string
    responses:
        default:
            description: Movie deleted
    """
    x=delete(id)
    if x:
        return jsonify({'message':'Movie deleted'})
    else:
        return jsonify({'message':'Movie not found'})


@app.route('/movies/<id>', methods=['PUT'])
def update_movie(id):
    """
    Update movie
    ---
    tags:
        - Movies
    parameters:
        - in: path
          name: id
          required: true
          type: string
        - in: body
          name: body
          required: true
          schema:
            type: object
            properties:
                title: 
                    type: string
                director:
                    type: string
                genre:
                    type: string
                year:
                    type: integer
                rating:
                    type: number
    responses:
        default:
            description: Movie updated
    """
    movie=update(id,request.json)
    if movie:
        return jsonify(movie)
    else:
        return jsonify({'message':'Movie not found'})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)