
import jwt
import datetime
from functools import wraps
from flask import Flask, request, jsonify, make_response



from Database.DataBase import Database
from Repositories.FavoriteRepository import FavoriteRepository
from Repositories.ExcerptRepository import ExcerptRepository
from Repositories.TagsToFavoriteRepository import TagsToFavorite
from Repositories.TagRepository import TagRepository
from Repositories.CategoryRepository import CategoryRepository
from Repositories.UserRepository import UserRepository
from Config.configuration import CHAVE


data = Database()
app = Flask(__name__)

secret = app.config['SECRET_KEY'] = CHAVE


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            # Verifica se o formato está correto
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]
            else:
                return jsonify({'Erro': 'Formato do token inválido!'}), 401
        else:
            return jsonify({'Erro': 'Token é necessário!'}), 401

        try:
            data = jwt.decode(token, secret, algorithms=["HS256"])
            current_user = data['user_id']
        except jwt.ExpiredSignatureError:
            return jsonify({'Erro': 'Token expirado!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'Erro': 'Token inválido!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

def create_jwt_token(user_id):
    token = jwt.encode({
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, app.config['SECRET_KEY'], algorithm="HS256")
    return token


@app.route("/login",methods=['POST'])
def SignInAccount():
    try:
        data = request.get_json(force=True)
        UserRep = UserRepository(data)
        response, message = UserRep.ValidUser()
        if not response:
            return jsonify({'Erro': message}), 400
        user_list = UserRep.FindUser()

        if user_list and isinstance(user_list, list) and len(user_list) > 0:
            user = user_list[0]
            user_id = user.get('USUid')
            token = create_jwt_token(user_id)

            return jsonify({
                'Mensagem': 'Usuário encontrado com sucesso',
                'token': token
            }), 200
        else:
            return jsonify({'Erro': 'Usuário não encontrado'}), 400

    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500

    
    
@app.route("/create/user",methods=['POST'])

def RegisterAccount():
    try:
        data = request.get_json(force=True)
        UserRep = UserRepository(data)
        response,message = UserRep.CreateUser()
        if response == 400:
            return jsonify({'Erro': message}), 400
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
            return jsonify({'Erro': message}), 400
        else:
            return jsonify({'Mensagem': f'Usuário cadastrado com sucesso'}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
    
    
    
    
    
    
    
    
    
    
    
@app.route("/create/category",methods=['POST'])
@token_required
def CreateCategory(current_user):
    try:
        data = request.get_json(force=True)
        CategoryRep = CategoryRepository(data)
        response,message = CategoryRep.CreateCategory()
        if response == 400:
            return jsonify({'Erro': message}), 400
        else:
            return jsonify({'Mensagem': f'Categoria cadastrado com sucesso'}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
@app.route("/update/category",methods=['PUT'])
@token_required
def UpdateCategory(current_user):
    try:
        data = request.get_json(force=True)
        CategoryRep = CategoryRepository(data)
        response,message = CategoryRep.UpdateCategory()
        if response == 400:
            return jsonify({'Erro': message}), 400
        else:
            return jsonify({'Mensagem': f'Categoria alterada com sucesso.'}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
    
@app.route("/list/categories",methods=['GET'])
@token_required
def ListCategories(current_user):
    try:
        CategoryRep = CategoryRepository('')
        response,source = CategoryRep.ListAllCategories()
        if response == 400:
            return jsonify({'Erro': source}), 400
        else:
            return jsonify({'Data': [category.to_dict() for category in source]}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
















@app.route("/create/tag",methods=['POST'])
@token_required
def CreateTag(current_user):
    try:
        data = request.get_json(force=True)
        tagRep = TagRepository(data)
        response,message = tagRep.CreateTag()
        if response == 400:
            return jsonify({'Erro': message}), 400
        else:
            return jsonify({'Mensagem': f'Tag cadastrado com sucesso'}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500

    
@app.route("/list/tags/<int:userId>",methods=['GET'])
@token_required
def ListUserTags(current_user,userId):
    try:
        data = {"tagIdUser": userId}
        tagRep = TagRepository(data)
        response,source = tagRep.ListAllTagForUserId()
        if response == 400:
            return jsonify({'Erro': source}), 400
        else:
            return jsonify({'Data': [tag.to_dict() for tag in source]}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
@app.route("/update/tag",methods=['PUT'])
@token_required
def UpdateTag(current_user):
    try:
        data = request.get_json(force=True)
        tagRep = TagRepository(data)
        response,message = tagRep.UpdateTag()
        if response == 400:
            return jsonify({'Erro': message}), 400
        else:
            return jsonify({'Mensagem': f'Tag alterada com sucesso.'}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
@app.route("/delete/tag/<int:idTag>",methods=['DELETE'])
@token_required
def DeleteTag(current_user,idTag):
    try:
        data = {"tagId": idTag}
        tagRep = TagRepository(data)
        response,message = tagRep.DeleteTag()
        if response == 400:
            return jsonify({'Erro': message}), 400
        else:
            return jsonify({'Mensagem': f'Tag deletada com sucesso'}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
    
    
    
    
    
    
    
@app.route("/create/favorite",methods=['POST'])
@token_required
def CreateFavorite(current_user):
    try:
        data = request.get_json(force=True)
        favoriteRep = FavoriteRepository(data)
        response,message = favoriteRep.CreateFavorite()
        if response == 400:
            return jsonify({'Erro': message}), 400
        else:
            return jsonify({'Mensagem': f'Favorito cadastrado com sucesso'}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
@app.route("/list/favorites/<int:userId>",methods=['GET'])
@token_required
def ListUserFavorites(current_user,userId):
    try:
        data = {"userId": userId}
        favoritesRep = FavoriteRepository(data)
        response,source = favoritesRep.ListAllFavoriteForUser()
        if response == 400:
            return jsonify({'Erro': source}), 400
        else:
            return jsonify({'Data': [favorite.to_dict() for favorite in source]}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
@app.route("/list/favorite/<int:idFavorite>", methods=['GET'])
@token_required
def ListUserFavorite(current_user,idFavorite):
    try:
        data = {"favoriteId": idFavorite}
        favoritesRep = FavoriteRepository(data)
        response, source = favoritesRep.ListAFavorite()
        if response == 400:
            return jsonify({'Erro': source}), 400
        else:
            return jsonify({'Data': [favorite.to_dict() for favorite in source]}), 200 
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500

    
    
@app.route("/delete/favorite/<int:idFavorite>",methods=['DELETE'])
@token_required
def DeleteFavorite(current_user,idFavorite):
    try:
        data = {"favoriteId": idFavorite}
        favoriteRep = FavoriteRepository(data)
        response,message = favoriteRep.DeleteFavorite()
        if response == 400:
            return jsonify({'Erro': message}), 400
        else:
            return jsonify({'Mensagem': f'Favorito deletado com sucesso'}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    

@app.route("/update/favorite",methods=['PUT'])
@token_required
def UpdateFavorite(current_user):
    try:
        data = request.get_json(force=True)
        favoriteRep = FavoriteRepository(data)
        response,message = favoriteRep.UpdateFavorite()
        if response == 400:
            return jsonify({'Erro': message}), 400
        else:
            return jsonify({'Mensagem': f'Favorito alterada com sucesso.'}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    

    
    
    
    
    
    
    
    
@app.route("/create/excerpt",methods=['POST'])
@token_required
def CreateExcerpts(current_user):
    try:
        data = request.get_json(force=True)
        excerptRep = ExcerptRepository(data)
        response,message = excerptRep.CreateExcerpt()
        if response == 400:
            return jsonify({'Erro': message}), 400
        else:
            return jsonify({'Mensagem': f'Comentário cadastrado com sucesso'}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
@app.route("/list/ExcerptsFavorite/<int:idFavorite>",methods=['GET'])
@token_required
def ListFavoritesExcerpts(current_user,idFavorite):
    try:
        data = {"idFavorite": idFavorite}
        excerptRep = ExcerptRepository(data)
        response,source = excerptRep.ListExcerptsOfFavorite()
        if response == 400:
            return jsonify({'Erro': source}), 400
        else:
            return jsonify({'Data': [excerpt.to_dict() for excerpt in source]}), 200 
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
    
@app.route("/delete/excerpt/<int:idExcerpt>",methods=['DELETE'])
@token_required
def DeleteExcerpts(current_user,idExcerpt):
    try:
        data = {"idExcerpt": idExcerpt}
        excerptRep = ExcerptRepository(data)
        response,message = excerptRep.DeleteExcerpt()
        if response == 400:
            return jsonify({'Erro': message}), 400
        else:
            return jsonify({'Mensagem': f'Comentário deletado com sucesso'}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
    
    
@app.route("/update/excerpt",methods=['PUT'])
@token_required
def UpdateExcerpts(current_user):
    try:
        data = request.get_json(force=True)
        excerptRep = ExcerptRepository(data)
        response,message = excerptRep.UpdateExcerpt()
        if response == 400:
            return jsonify({'Erro': message}), 400
        else:
            return jsonify({'Mensagem': f'Comentário alterado com sucesso.'}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    