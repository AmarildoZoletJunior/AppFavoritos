from flask import Flask, request, jsonify
from Database.DataBase import Database
from Config import configuration


data = Database()
app = Flask(__name__)


@app.route("/login",methods=['POST'])
def SignInAccount():
    try:
        data = request.get_json(force=True)
        login = data.get('login')
        password = data.get('password')
        if login:
            print('passou login')
        else:
            return jsonify({'error': 'Login ausentes ou inválidos.'}), 400

        if password:
            print('passou password')
        else:
            return jsonify({'error': 'password ausentes ou inválidos.'}), 400
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
@app.route("/register",methods=['POST'])
def RegisterAccount():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
@app.route("/resetpassword",methods=['POST'])
def ResetPassword():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
    
    
    
    
    
    
    
    
    
    
    
@app.route("/resetpassword",methods=['POST'])
def CreateCategory():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
@app.route("/resetpassword",methods=['POST'])
def ListCategories():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
   







@app.route("/resetpassword",methods=['POST'])
def CreateTag():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500

    
@app.route("/resetpassword",methods=['POST'])
def ListUserTags():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
@app.route("/resetpassword",methods=['POST'])
def UpdateTag():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
@app.route("/resetpassword",methods=['POST'])
def DeleteTag():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
    
    
    
    
    
    
    
@app.route("/resetpassword",methods=['POST'])
def CreateFavorite():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
@app.route("/resetpassword",methods=['POST'])
def ListUserFavorites():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
@app.route("/resetpassword",methods=['POST'])
def DeleteFavorite():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500

@app.route("/resetpassword",methods=['POST'])
def UpdateFavorite():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
    
    
    
    
    
    
@app.route("/resetpassword",methods=['POST'])
def CreateExcerpts():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
@app.route("/resetpassword",methods=['POST'])
def ListFavoritesExcerpts():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
@app.route("/resetpassword",methods=['POST'])
def DeleteExcerpts():
    try:
        return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
@app.route("/resetpassword",methods=['POST'])
def UpdateExcerpts():
    try:
      return 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500