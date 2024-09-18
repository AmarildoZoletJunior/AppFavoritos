from flask import Flask, request, jsonify
from Database.DataBase import Database
from Repositories.UserRepository import UserRepository


data = Database()
app = Flask(__name__)


@app.route("/login",methods=['POST'])
def SignInAccount():
    try:
        data = request.get_json(force=True)
        UserRep = UserRepository(data)
        response,message = UserRep.ValidUser()
        if not response:
            return jsonify({'error': message}), 400
        else:
            response = UserRep.FindUser()
            if len(response) > 0:
                return jsonify({'Mensagem': f'Usuário encontrado com sucesso'}), 200
            else:
                return jsonify({'error': 'Usuário não encontrado'}), 400
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro'}), 500
    
    
@app.route("/create/user",methods=['POST'])
def RegisterAccount():
    try:
        data = request.get_json(force=True)
        UserRep = UserRepository(data)
        response,message = UserRep.CreateUser()
        if response == 400:
            return jsonify({'error': message}), 400
        else:
            return jsonify({'Mensagem': f'Usuário cadastrado com sucesso'}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
@app.route("/update/password",methods=['PUT'])
def ResetPassword():
    try:
        data = request.get_json(force=True)
        UserRep = UserRepository(data)
        response,message = UserRep.ResetPassword()
        if response == 400:
            return jsonify({'error': message}), 400
        else:
            return jsonify({'Mensagem': f'Usuário cadastrado com sucesso'}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
    
    
    
    
    
    
    
    
    
    
    
@app.route("/create/category",methods=['POST'])
def CreateCategory():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
@app.route("/list/categories",methods=['GET'])
def ListCategories():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
   







@app.route("/create/tag",methods=['POST'])
def CreateTag():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500

    
@app.route("/list/tags",methods=['GET'])
def ListUserTags():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
@app.route("/update/tag",methods=['PUT'])
def UpdateTag():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
@app.route("/delete/tag",methods=['DELETE'])
def DeleteTag():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
    
    
    
    
    
    
    
@app.route("/create/favorite",methods=['POST'])
def CreateFavorite():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
@app.route("/list/favorites",methods=['GET'])
def ListUserFavorites():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
@app.route("/delete/favorite",methods=['DELETE'])
def DeleteFavorite():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500

@app.route("/update/favorite",methods=['PUT'])
def UpdateFavorite():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
    
    
    
    
    
    
@app.route("/create/excerpt",methods=['POST'])
def CreateExcerpts():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
@app.route("/list/FavoritesExcerpts",methods=['GET'])
def ListFavoritesExcerpts():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
@app.route("/delete/excerpt",methods=['DELETE'])
def DeleteExcerpts():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
@app.route("/update/excerpt",methods=['PUT'])
def UpdateExcerpts():
    try:
      return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500