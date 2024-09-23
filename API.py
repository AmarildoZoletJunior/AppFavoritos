from flask import Flask, request, jsonify
from Database.DataBase import Database




from Repositories.FavoriteRepository import FavoriteRepository
from Repositories.ExcerptRepository import ExcerptRepository
from Repositories.TagsToFavoriteRepository import TagsToFavorite
from Repositories.TagRepository import TagRepository
from Repositories.CategoryRepository import CategoryRepository
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
            return jsonify({'Erro': message}), 400
        response = UserRep.FindUser()
        if response: 
            return jsonify({'Mensagem': f'Usuário encontrado com sucesso'}), 200
        else:
            return jsonify({'Erro': 'Usuário não encontrado'}), 400
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro:{e}'}), 500
    
    
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
def CreateCategory():
    try:
        data = request.get_json(force=True)
        print("aqui api 03")
        CategoryRep = CategoryRepository(data)
        print("aqui api01")
        response,message = CategoryRep.CreateCategory()
        print("aqui api02")
        if response == 400:
            return jsonify({'Erro': message}), 400
        else:
            return jsonify({'Mensagem': f'Categoria cadastrado com sucesso'}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
@app.route("/update/category",methods=['PUT'])
def UpdateCategory():
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
def ListCategories():
    try:
        CategoryRep = CategoryRepository('')
        response,source = CategoryRep.ListAllCategories()
        if response == 400:
            return jsonify({'Erro': source}), 400
        else:
            return jsonify({'Categorias':source}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
















@app.route("/create/tag",methods=['POST'])
def CreateTag():
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
def ListUserTags(userId):
    try:
        data = {"tagIdUser": userId}
        tagRep = TagRepository(data)
        response,source = tagRep.ListAllTagForUserId()
        if response == 400:
            return jsonify({'Erro': source}), 400
        else:
            return jsonify({'Tags':source}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
@app.route("/update/tag",methods=['PUT'])
def UpdateTag():
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
def DeleteTag(idTag):
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
def CreateFavorite():
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
def ListUserFavorites(userId):
    try:
        data = {"userId": userId}
        favoritesRep = FavoriteRepository(data)
        response,source = favoritesRep.ListAllFavoriteForUser()
        if response == 400:
            return jsonify({'Erro': source}), 400
        else:
            return jsonify({'Favoritos':source}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
@app.route("/list/favorite/<int:idFavorite>",methods=['GET'])
def ListUserFavorite(idFavorite):
    try:
        data = {"favoriteId": idFavorite}
        favoritesRep = FavoriteRepository(data)
        response,source = favoritesRep.ListAFavorite()
        if response == 400:
            return jsonify({'Erro': source}), 400
        else:
            return jsonify({'Favorito':source}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
@app.route("/delete/favorite/<int:idFavorite>",methods=['DELETE'])
def DeleteFavorite(idFavorite):
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
def UpdateFavorite():
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
def CreateExcerpts():
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
def ListFavoritesExcerpts(idFavorite):
    try:
        data = {"idFavorite": idFavorite}
        excerptRep = ExcerptRepository(data)
        response,source = excerptRep.ListExcerptsOfFavorite()
        if response == 400:
            return jsonify({'Erro': source}), 400
        else:
            return jsonify({'Favorito':source}), 200
    except Exception as e:
        return jsonify({'Erro': f'Ocorreu um erro, erro: {e}'}), 500
    
    
    
@app.route("/delete/excerpt/<int:idExcerpt>",methods=['DELETE'])
def DeleteExcerpts(idExcerpt):
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
def UpdateExcerpts():
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
    